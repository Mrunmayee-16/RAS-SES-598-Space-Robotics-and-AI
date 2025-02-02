from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    pkg_share = FindPackageShare('inverted_pendulum_optimal_control').find('inverted_pendulum_optimal_control')
    urdf_model_path = os.path.join(pkg_share, 'models', 'inverted_pendulum', 'model.urdf')
    
    # Create and return launch description
    return LaunchDescription([
        # Gazebo (headless mode)
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', '-s', 'empty.sdf'],  # -s for headless mode
            output='screen'
        ),

        # Spawn robot in Gazebo
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-topic', 'robot_description',
                '-name', 'inverted_pendulum',
                '-allow_renaming', 'true'
            ],
            output='screen'
        ),

        # Direct topic bridges
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='bridge',
            output='screen',
            arguments=[
                # Cart force command (ROS -> Gazebo)
                '/model/inverted_pendulum/joint/cart_to_base/cmd_force@std_msgs/msg/Float64]gz.msgs.Double',
                # Joint states (Gazebo -> ROS)
                '/world/empty/model/inverted_pendulum/joint_state@sensor_msgs/msg/JointState[ignition.msgs.Model',
                # Clock (Gazebo -> ROS)
                '/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock'
            ],
        ),

        # Robot state publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['cat ', urdf_model_path]),
                'publish_frequency': 50.0,  # Increased update frequency
                'use_tf_static': True,
                'ignore_timestamp': True
            }]
        ),

        # State Republisher
        Node(
            package='inverted_pendulum_optimal_control',
            executable='state_republisher',
            name='state_republisher',
            output='screen'
        ),

        # Force Visualizer
        Node(
            package='inverted_pendulum_optimal_control',
            executable='force_visualizer',
            name='force_visualizer',
            output='screen'
        ),

        # LQR Controller
        Node(
            package='inverted_pendulum_optimal_control',
            executable='lqr_controller',
            name='lqr_controller',
            output='screen'
        ),

        # Earthquake Force Generator
        Node(
            package='inverted_pendulum_optimal_control',
            executable='earthquake_force_generator',
            name='earthquake_force_generator',
            output='screen',
            parameters=[{
                'base_amplitude': 15.0,  # Increased from 5.0N to 15.0N
                'frequency_range': [0.5, 4.0],  # Increased upper frequency to 4.0 Hz
                'update_rate': 50.0  # Keep update rate the same
            }]
        ),

        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(pkg_share, 'config', 'cart_pole.rviz')],
            parameters=[{
                'update_rate': 50.0  # Match the publish frequency
            }]
        )
    ]) 