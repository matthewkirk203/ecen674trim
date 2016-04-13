#!/usr/bin/env python

import sys
import rospy
from trim.srv import *
import Trim

def compute_trim_client(Va, R, gamma):
    rospy.wait_for_service('compute_trim')
    try:
        compute_trim = rospy.ServiceProxy('compute_trim', ComputeTrim)
        resp1 = compute_trim(Va, R, gamma)
        return resp1.x_trim,resp1.u_trim
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [Va R gamma]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        Va = float(sys.argv[1])
        R = float(sys.argv[2])
        gamma = float(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    print "Requesting trim with Va: %s, R: %s, gamma: %s"%(Va, R, gamma)
    x_trim, u_trim = compute_trim_client(Va, R, gamma)
    print('\n\n x trim')
    print('pn',x_trim[0])
    print('pe',x_trim[1])
    print('pd',x_trim[2])
    print('u',x_trim[3])
    print('v',x_trim[4])
    print('w',x_trim[5])
    print('phi',x_trim[6])
    print('theta',x_trim[7])
    print('psi', x_trim[8])
    print('p',x_trim[9])
    print('q',x_trim[10])
    print('r',x_trim[11])

    print('\n\n u trim')
    print('delta e', u_trim[0])
    print('delta t', u_trim[1])
    print('delta a', u_trim[2])
    print('delta r', u_trim[3])