#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def main():
	rospy.init_node('avoiding_random', anonymous=False)

	sub=rospy.Subscriber("/scan",LaserScan,callback)

	rospy.spin()
	
def callback(distances):
	move=Twist()

	thr1 = 0.8
	thr2 = 0.4
	if distances.ranges[0] > thr1:
		if distances.ranges[25] > thr2 and distances.ranges[335] > thr2:
			move.linear.x = 0.5
			move.angular.z=0.0
		elif distances.ranges[25] > thr2 and distances.ranges[335] < thr2:
			move.linear.x = 0.0
			move.angular.z = 0.65
		elif distances.ranges[25] < thr2 and distances.ranges[335] > thr2:
			move.linear.x = 0.0
			move.angular.z = -0.65
		else:
			move.linear.x = 0.0
			move.angular.z = 0.65
	else:
		move.linear.x=0.0
		move.angular.z = 0.7


	pub=rospy.Publisher("/cmd_vel",Twist,queue_size=10)	
	pub.publish(move)


if __name__=='__main__':
	main()