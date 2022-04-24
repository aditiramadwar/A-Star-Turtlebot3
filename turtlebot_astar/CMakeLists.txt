cmake_minimum_required(VERSION 3.0.2)
project(turtlebot_astar)

#add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  gazebo_ros
)
catkin_python_setup()
catkin_package()
catkin_install_python(PROGRAMS
   src/main.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )
 
include_directories(
 #utils
  ${catkin_INCLUDE_DIRS}
)
