#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("Move_Robot_Node")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
rate = rospy.Rate(2)
move = Twist()
move.angular.z = 0.5
move.linear.x = 0.5

while not rospy.is_shutdown():
    pub.publish(move)
    rate.sleep()