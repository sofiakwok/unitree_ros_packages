Packages for running mocap on Ubuntu 18 with Ros Melodic. The two packages are ```natnet_ros_cpp``` (altered from https://github.com/L2S-lab/natnet_ros_cpp to be compatible with Ros Melodic) for publishing poses and ```optitrack``` for subscribing to poses. This is a standard ROS1 workspace, with the root directory ```unitree_ros_packages```.

Installation instructions:
1. Install Ros Melodic
2. Source /opt/ros/melodic/setup.bash
3. Install natnet_ros_cpp dependencies: ```sudo apt install -y ros-$ROS_DISTRO-tf2* wget```
4. Clone this repository
5. ```cd unitree_ros_packages```
6. Use catkin build or catkin_make (for ROS1, always run this command in the root directory, i.e. unitree_ros_packages). You should have two packages that build successfully. 
8. Source /devel/setup.bash
9. To run mocap publisher: ```roslaunch natnet_ros_cpp natnet_ros.launch```
10. To run mocap subscriber: ```rosrun optitrack listener```

Note: For people using the MuJoCo-control-estimation repository, the ```optitrack``` package should never need to be actually launched to access pose data - just the publisher needs to be launched. 
