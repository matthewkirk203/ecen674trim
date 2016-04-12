#!/usr/bin/env python

from trim.srv import *
import rospy
import Trim

def compute_trim(req):
	Va = float(req.Va)
	gamma = float(req.gamma)
	R = float(req.R)
	return Trim.ComputeTrim(Va,gamma,R)

def compute_trim_server():
    rospy.init_node('compute_trim_server')
    s = rospy.Service('compute_trim', ComputeTrim, compute_trim)
    # print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    compute_trim_server()