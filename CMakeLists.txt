cmake_minimum_required(VERSION 2.8.3)
project(shelly_wifi_relay_module_ros1)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_srvs
)

catkin_package()

catkin_python_setup()

catkin_install_python(PROGRAMS
  scripts/shelly_relay_client.py
  scripts/shelly_relay_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  # Add tests here if needed
endif()
