#!/usr/bin/env python

from trim.srv import *
import rospy
import Trim

def compute_trim(req):
	Va = float(req.Va)
	R = float(req.R)
	gamma = float(req.gamma)
	return Trim.ComputeTrim(Va,R,gamma)

def compute_trim_server():
    rospy.init_node('compute_trim_server')
    s = rospy.Service('compute_trim', ComputeTrim, compute_trim)
    # print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    compute_trim_server()