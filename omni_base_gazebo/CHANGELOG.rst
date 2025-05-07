^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package omni_base_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.8.0 (2025-05-07)
------------------
* add use_sim_time to robot_info
* Contributors: antoniobrandi

2.7.0 (2025-05-06)
------------------
* rviz use_sim_time
* Contributors: antoniobrandi

2.6.2 (2025-05-05)
------------------
* update maintainer
* fix deps
* Contributors: andreacapodacqua

2.6.1 (2025-04-09)
------------------
* rviz_typo
* Contributors: salvatorepiccolo

2.6.0 (2025-04-03)
------------------
* store robot_info in tmp
* Contributors: antoniobrandi

2.5.0 (2025-04-03)
------------------
* pal_configuration adoption
* Contributors: antoniobrandi

2.4.0 (2025-01-23)
------------------
* support camera model
* Contributors: antoniobrandi

2.3.0 (2024-12-02)
------------------
* Merge branch 'abr/feat/docking' into 'humble-devel'
  using docking arg
  See merge request robots/omni_base_simulation!28
* always start docking with adv navigation
* using docking arg
* Contributors: antoniobrandi

2.2.1 (2024-11-15)
------------------

2.2.0 (2024-10-16)
------------------
* Merge branch 'man/feat/advanced-nav' into 'humble-devel'
  added advanced nav launch arg to navigation
  See merge request robots/omni_base_simulation!25
* added advanced nav launch arg to navigation
* Contributors: antoniobrandi, martinaannicelli

2.1.0 (2024-09-03)
------------------
* Remove twist relay from simulation and launch in mobile_base_controller
* Contributors: David ter Kuile

2.0.10 (2024-08-19)
-------------------
* Merge branch 'abr/fix/twist' into 'humble-devel'
  using relay_field for twist message
  See merge request robots/omni_base_simulation!22
* use relay_field only for private sim
* typo
* using relay_field for twist message
* Contributors: antoniobrandi

2.0.9 (2024-07-08)
------------------
* Merge branch 'abr/feat/advanced-navigation' into 'humble-devel'
  added advanced navigation
  See merge request robots/omni_base_simulation!20
* added advanced navigation
* Contributors: antoniobrandi, davidterkuile

2.0.8 (2024-07-05)
------------------
* Add slam argument for navigation
* Contributors: Noel Jimenez

2.0.7 (2024-06-28)
------------------
* Merge branch 'dtk/add-on-module' into 'humble-devel'
  Change rgbd sensors to add-on-module
  See merge request robots/omni_base_simulation!19
* Change rgbd sensors to add-on-module
* Contributors: David ter Kuile, davidterkuile

2.0.6 (2024-06-26)
------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Dtk/move robot args
  See merge request robots/omni_base_simulation!18
* Change import for launch args
* Contributors: David ter Kuile, davidterkuile

2.0.5 (2024-06-25)
------------------
* Merge branch 'dtk/standardize-pkg' into 'humble-devel'
  Dtk/standardize pkg
  See merge request robots/omni_base_simulation!17
* Fix linters
* Remove unnecessary dependency
* Updat launch structure
* Contributors: David ter Kuile, davidterkuile

2.0.4 (2024-05-08)
------------------
* Merge branch 'man/omni-base-gazebo-spawn' into 'humble-devel'
  added pose conifiguration in spawn_entity args
  See merge request robots/omni_base_simulation!16
* added pose configration in spawn entity
* added pose variables in spawn entity
* added pose arguments in spawn_entity
* added pose conifiguration in spawn_entity args
* Contributors: antoniobrandi, martinaannicelli

2.0.3 (2024-04-15)
------------------
* Merge branch 'omm/feat/public_sim_control' into 'humble-devel'
  is_public_sim check
  See merge request robots/omni_base_simulation!15
* Using new launch action
* Contributors: Oscar, davidterkuile

2.0.2 (2024-04-10)
------------------
* Merge branch 'feat/ros2-pipelines' into 'humble-devel'
  Feat/ros2 pipelines
  See merge request robots/omni_base_simulation!14
* cosmetic and update readme
* removed slam arg
* navigation pipeline integration for private sim
* Contributors: andreacapodacqua

2.0.1 (2024-02-02)
------------------
* Merge branch 'feat/register-components' into 'humble-devel'
  use single entry point for navigation
  See merge request robots/omni_base_simulation!13
* use single entry point for navigation
* Merge branch 'abr/fix/world-name' into 'humble-devel'
  move world_name to pal_gazebo_worlds
  See merge request robots/omni_base_simulation!12
* move world_name to pal_gazebo_worlds
* Contributors: Noel Jimenez, antoniobrandi

2.0.0 (2023-11-22)
------------------
* Merge branch 'fix/use_sim_time' into 'humble-devel'
  Set use_sim_time true
  See merge request robots/omni_base_simulation!10
* Set use_sim_time true
* omni_base ROS 2
* fix launch nav_sim
* ROS 2 omni_base simulation
* enable controller and 2dnav
* omnibase gazebo to ROS 2:
  + colcon
  + launch.py
* Contributors: Noel Jimenez, YueErro, andreacapodacqua

0.0.7 (2023-02-23)
------------------

0.0.6 (2023-01-30)
------------------

0.0.5 (2023-01-27)
------------------

0.0.4 (2022-08-08)
------------------

0.0.3 (2022-02-23)
------------------

0.0.2 (2021-11-24)
------------------
* removing the needs for pid values for the wheels
* Contributors: antoniobrandi

0.0.1 (2021-09-30)
------------------
* preparing release
* adapting to the new version of omni_base_robot
* omni base simulation initial commit
* Contributors: antoniobrandi
