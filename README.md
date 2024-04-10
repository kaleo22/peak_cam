# ids_peak_cam

A Linux [ROS2 C++ Node](https://wiki.ros.org/peak_cam) that wraps the driver API for IDS vision cameras using IDS peak software. Tested on Ubuntu 22.04 LTS.

## How to run

### Before running the code

1. install [ROS2 Humble](https://docs.ros.org/en/humble/Installation.html)
2. install [IDS peak](https://de.ids-imaging.com/download-vision-lin64.html)

### Running the code

0. Clone the repository to your Linux computer

1. Generate a ROS2 workspace

    `$ mkdir -p camera_ws/src/` 

1. Copy the peak_cam package into your ROS2 workspace and build it
    
    `$ cp -r peak_cam/ camera_ws/src/`
    
    `$ cd camera_ws/ && colcon build && source install/setup.bash`

2. Set parameters such as ROS topic and acquisition rate under `launch/params/peak_cam_params.yaml`

3. Plug the IDS vision camera and launch the node 

    `$ ros2 launch peak_cam peak_cam.launch.py`
    
4. Stop the node with `Ctrl-C` (SIGINT) for controlled shutdown 

For multiple cameras, create a `.launch` and a `.yaml` file for each camera.

> Hint: Sometimes the cameras are only accesible as root. Try ` sudo -s` in your terminal and launch the node again.


All rights reserved.

BSD license: see LICENSE file
