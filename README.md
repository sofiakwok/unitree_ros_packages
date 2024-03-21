Packages for running mocap on Ubuntu 18 with Ros Melodic. The two packages are natnet_ros_cpp (https://github.com/L2S-lab/natnet_ros_cpp) for publishing poses and optitrack for subscribing to poses.

Installation instructions:
1. Install Ros Melodic
2. Source /opt/ros/melodic/setup.bash
3. Install natnet_ros_cpp dependencies: '''sudo apt install -y ros-$ROS_DISTRO-tf2* wget'''
4. Clone this repository
5. '''cd catkin_ws'''
6. Use catkin build in root directory (catkin_ws)
7. Source /devel/setup.bash
8. To run mocap publisher: roslaunch natnet_ros_cpp natnet_ros.launch
9. To run mocap subscriber: rosrun optitrack listener (should not need to run this. Should be handled in unitree code.)
