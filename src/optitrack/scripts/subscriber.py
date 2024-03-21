#!/usr/bin/env python
import rospy

import numpy as np
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import PoseStamped

# RigidBody data specs:
# std_msgs/Header header
# uint32 frame_number
# mocap4r2_msgs/RigidBody[] rigidbodies

#Biped: streaming ID 1049
# rigid_body publishes information type [mocap4r2_msgs/msg/RigidBodies]

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.last_pose = np.array([0, 0, 0, 0, 0, 0, 0])
        self.streaming_id = "1049"
        self.subscription = self.create_subscription(
            PoseStamped,
            'natnet_ros/Biped/pose',
            self.listener_callback,
            10)  #queue list
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.pose)
        position = np.array([msg.pose.position.x, msg.pose.position.y, msg.pose.position.z])
        orientation = np.array([msg.pose.orientation.w, msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z])
        # self.get_logger().info('position: "%s"' % position)
        # self.get_logger().info('orientation: "%s"' % orientation)
        self.last_pose = np.concatenate((position, orientation), axis=None)
 
    def signal(self):
        return self.last_pose
    
    def velocity(self):
        velocity = self.vel_filter()
        return velocity
    
    def vel_filter(self):
        return None

    def main(args=None):
        rclpy.init(args=args)

        minimal_subscriber = MinimalSubscriber()

        rclpy.spin(minimal_subscriber)

        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        minimal_subscriber.destroy_node()
        rclpy.shutdown()

# rclpy.Node.Subscriber('/mocap4r2_optitrack_driver/RigidBody/pose', Pose, some_callback)

def main(args=None):
    rospy.init_node()
    subscriber = rospy.Subscriber("natnet_ros/Biped/pose")
    
    minimal_subscriber = MinimalSubscriber()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()