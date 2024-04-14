from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument , SetEnvironmentVariable, IncludeLaunchDescription
import os
from os import pathsep ##to seperate paths from both model_paths
from ament_index_python.packages import get_package_share_directory, get_package_prefix ##instead of mentioning the full path in the default_Value instance
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command,LaunchConfiguration# to change from xacro to urdf
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    rbtc_description = get_package_share_directory("rbtc_arm_description")
    brbtc_description_prefix = get_package_prefix("rbtc_arm_description")

    model_path = os.path.join(rbtc_description, "models")
    model_path += pathsep + os.path.join(brbtc_description_prefix, "share") 

    env_variable = SetEnvironmentVariable("GAZEBO_MODEL_PATH", model_path)

    model_arg = DeclareLaunchArgument(  #declares an argument for the launch file unlike LaunchCOnfiguartion which reading the content of the DeclareLaunchArgument
        name="model", #choose the name of the file of your robot 
        default_value=os.path.join(rbtc_description, "urdf", "rbtc_arm.urdf.xacro"), #it will automatically search for the bumperbot_description package and get the directory following it
        description = "Absolute path to robot URDF file"
    )
    robot_description = ParameterValue(Command(["xacro ", LaunchConfiguration("model")]), value_type=str) ##converts xacro to plain urdf (takes parameter value in xacro and applies the command method on it)
   ###################################################^needed space here


    robot_state_publisher = Node(
        package="robot_state_publisher", ##what you want to execute
        executable='robot_state_publisher', ##what executable file, it is named the same in this case in some other cases it might differ
        parameters=[{"robot_description": robot_description}] ##remember the command you used on the xacro file to run it as urdf
    )

    start_gazebo_server = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(
        get_package_share_directory("gazebo_ros"), "launch", "gzserver.launch.py"
    ))) #creates an instance of the server to launch it
    start_gzebo_client = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(
        get_package_share_directory("gazebo_ros"), "launch", "gzclient.launch.py"

    ))) #creates an instance of the client to launch it

    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-entity", "Robotic_Arm", "-topic", "robot_description"], #same topic used in rviz use in gazebo
        output="screen"
    )
    return LaunchDescription([
    env_variable,
    model_arg,
    robot_state_publisher,
    start_gazebo_server,
    start_gzebo_client,
    spawn_robot
    ])