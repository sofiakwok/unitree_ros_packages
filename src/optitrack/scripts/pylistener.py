#!/usr/bin/env python

# Import required Python code.
import roslib
import rospy
from geometry_msgs.msg import PoseStamped

# Create a callback function for the subscriber.
def callback(data):
    # Simply print out values in our custom message.
    rospy.loginfo(rospy.get_name() + " I heard %s", data.message)
    rospy.loginfo(rospy.get_name() + " a + b = %d", data.a + data.b)

# This ends up being the main while loop.
def listener():
    # Get the ~private namespace parameters from command line or launch file.
    topic = rospy.get_param('~topic', 'chatter')
    # Create a subscriber with appropriate topic, custom message and name of callback function.
    rospy.Subscriber(topic, PoseStamped, callback)
    # Wait for messages on topic, go to callback function when new messages arrive.
    rospy.spin()

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('pylistener', anonymous = True)
    # Go to the main loop.
    listener()