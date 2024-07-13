cmake_minimum_required(VERSION 3.5)
project(bot)

# 找到必要的包
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(xacro REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(gazebo_ros REQUIRED)

# 其他CMake配置，包含库、可执行文件等

# 安装launch文件
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# 安装urdf目录
install(
  DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
