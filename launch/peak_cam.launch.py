import launch
from launch import LaunchDescription
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
import yaml
from launch_ros.actions import Node


def generate_launch_description():
    parameters_file_path = Path(get_package_share_directory('peak_cam'), 'params', 'settings', 'cam1.yaml')
    camera_info_path = Path(get_package_share_directory('peak_cam'), 'params', 'intrinsics', 'cam_1_camera_info.yaml')
    camera_info_path_4 = Path(get_package_share_directory('peak_cam'), 'params', 'intrinsics', 'cam_4_camera_info.yaml')
    parameters_file_path_2 = Path(get_package_share_directory('peak_cam'), 'params', 'settings', 'cam2.yaml')
    parameters_file_path_3 = Path(get_package_share_directory('peak_cam'), 'params', 'settings', 'cam3.yaml')
    parameters_file_path_4 = Path(get_package_share_directory('peak_cam'), 'params', 'settings', 'cam4.yaml')

    with open(parameters_file_path, 'r') as f:
        params = yaml.safe_load(f)['/**']['ros__parameters']
    print(params)

    container = ComposableNodeContainer(
        name='peak_cam_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='peak_cam',
                plugin='peak_cam::PeakCamNode',
                name='peak_cam',
                parameters=[
                    params,
                    {'camera_info_url': 'file://' + str(camera_info_path)}])
        ],
        output='screen'
    )

    with open(parameters_file_path_2, 'r') as f:
        params_2 = yaml.safe_load(f)['/**']['ros__parameters']
    print(params_2)

    container_2 = ComposableNodeContainer(
        name='peak_cam_container2',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='peak_cam',
                plugin='peak_cam::PeakCamNode',
                name='peak_cam_2',
                parameters=[
                    params_2,
                    {'camera_info_url': 'file://' + str(camera_info_path)}])
        ],
        output='screen'
    )

    with open(parameters_file_path_3, 'r') as f:
        params_3 = yaml.safe_load(f)['/**']['ros__parameters']
    print(params_3)

    container_3 = ComposableNodeContainer(
        name='peak_cam_container3',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='peak_cam',
                plugin='peak_cam::PeakCamNode',
                name='peak_cam_3',
                parameters=[
                    params_3,
                    {'camera_info_url': 'file://' + str(camera_info_path_4)}])
        ],
        output='screen'
    )

    # with open(parameters_file_path_4, 'r') as f:
    #     params_4 = yaml.safe_load(f)['/**']['ros__parameters']
    # print(params_4)

    # container_4 = ComposableNodeContainer(
    #     name='peak_cam_container4',
    #     namespace='',
    #     package='rclcpp_components',
    #     executable='component_container',
    #     composable_node_descriptions=[
    #         ComposableNode(
    #             package='peak_cam',
    #             plugin='peak_cam::PeakCamNode',
    #             name='peak_cam_4',
    #             parameters=[
    #                 params_4,
    #                 {'camera_info_url': 'file://' + str(camera_info_path)}])
    #     ],
    #     output='screen'
    # )


    return launch.LaunchDescription([container, container_2, container_3])