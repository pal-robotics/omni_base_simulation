cmake_minimum_required(VERSION 3.0.2)
project(omni_base_2dnav_gazebo)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir launch)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)