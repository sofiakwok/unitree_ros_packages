#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
import numpy as np

class MinimalSubscriber():

    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        self.last_pose = np.array([0, 0, 0, 0, 0, 0, 0])
        self.subscription = rospy.Subscriber("/natnet_ros/Wildfire_ORDv1/pose", PoseStamped, self.callback)

    def callback(self, data):
        # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.pose.position.x)
        position = np.array([data.pose.position.x, data.pose.position.y, data.pose.position.z])
        orientation = np.array([data.pose.orientation.w, data.pose.orientation.x, data.pose.orientation.y, data.pose.orientation.z])
        # self.get_logger().info('position: "%s"' % position)
        # self.get_logger().info('orientation: "%s"' % orientation)
        self.last_pose = np.concatenate((position, orientation), axis=None)
        
    def pose(self):
        return self.last_pose

    def listener(self):

        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber("/natnet_ros/Biped/pose", PoseStamped, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    node = MinimalSubscriber()

    i = 0
    while i < 1000:
        pose = node.pose()
        print(pose)
        i += 1

    # rospy.spin()