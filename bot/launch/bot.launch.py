from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # 获取包的共享目录路径
    package_share_directory = FindPackageShare(package='bot').find('bot')
    
    # 拼接xacro文件的绝对路径
    default_xacro_file = PathJoinSubstitution(
        [package_share_directory, 'urdf', 'robot.xacro']
    )

    # 声明launch参数
    declare_xacro_file_cmd = DeclareLaunchArgument(
        'xacro_file',
        default_value=default_xacro_file,
        description='Full path to the xacro file to be converted to URDF'
    )

    # 使用xacro命令将xacro文件转换为URDF
    robot_description_content = Command(
        ['xacro ', LaunchConfiguration('xacro_file')]
    )
    
    # 创建robot_state_publisher节点
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_content}]
    )

    # 启动Gazebo并加载机器人模型
    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'my_robot'],
        output='screen'
    )

    return LaunchDescription([
        declare_xacro_file_cmd,
        robot_state_publisher_node,
        gazebo,
        spawn_entity
    ])
