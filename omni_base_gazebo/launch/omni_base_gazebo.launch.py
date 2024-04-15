# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from os import environ, pathsep

from ament_index_python.packages import get_package_prefix, get_package_share_directory
from launch_pal.actions import CheckPublicSim
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():

    navigation_arg = DeclareLaunchArgument(
        'navigation', default_value='False',
        description='Specify if launching Navigation2'
    )

    is_public_sim = DeclareLaunchArgument(
        name='is_public_sim',
        default_value='false',
        description='Enable public simulation.',
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('pal_gazebo_worlds'), 'launch'), '/pal_gazebo.launch.py']),
    )

    check_public_sim = CheckPublicSim()

    omni_base_spawn = include_launch_py_description(
        'omni_base_gazebo', ['launch', 'omni_base_spawn.launch.py'])
    omni_base_bringup = include_launch_py_description(
        'omni_base_bringup', ['launch', 'omni_base_bringup.launch.py'],
        launch_arguments={'use_sim_time': 'True'}.items())

    navigation = include_launch_py_description(
        pkg_name='omni_base_2dnav',
        paths=['launch', 'omni_base_nav_bringup.launch.py'],
        condition=IfCondition(LaunchConfiguration('navigation')))

    pkg_path = get_package_prefix('omni_base_description')
    model_path = os.path.join(pkg_path, 'share')
    resource_path = pkg_path

    if 'GAZEBO_MODEL_PATH' in environ:
        model_path += pathsep + environ['GAZEBO_MODEL_PATH']
    if 'GAZEBO_RESOURCE_PATH' in environ:
        resource_path += pathsep + environ['GAZEBO_RESOURCE_PATH']

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(SetEnvironmentVariable('GAZEBO_MODEL_PATH', model_path))
    # Using this prevents shared library from being found
    # ld.add_action(SetEnvironmentVariable('GAZEBO_RESOURCE_PATH', omni_base_resource_path))

    ld.add_action(is_public_sim)
    ld.add_action(check_public_sim)
    ld.add_action(gazebo)
    ld.add_action(omni_base_spawn)
    ld.add_action(omni_base_bringup)

    ld.add_action(navigation_arg)
    ld.add_action(navigation)

    return ld
