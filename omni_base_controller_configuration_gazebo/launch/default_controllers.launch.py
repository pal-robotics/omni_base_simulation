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

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():
    declare_tf_prefix = DeclareLaunchArgument(
        'tf_prefix', default_value='',
        description='tf_prefix for mobile_base_controller param')

    # <param name="mobile_base_controller/base_frame_id" value="$(arg tf_prefix)/base_footprint"/>
    # <param name="mobile_base_controller/odom_frame_id" value="$(arg tf_prefix)/odom"/>


    mobile_base_controller_launch = include_launch_py_description(
        'omni_base_controller_configuration', ['launch', 'mobile_base_controller.launch.py'])

    # joint_state_broadcaster_launch = include_launch_py_description(
    #     'omni_base_controller_configuration', ['launch', 'joint_state_broadcaster.launch.py'])


    ld = LaunchDescription()

    ld.add_action(declare_tf_prefix)
    ld.add_action(mobile_base_controller_launch)
    # ld.add_action(joint_state_broadcaster_launch)

    return ld
