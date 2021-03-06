#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015/02/26

@author: spiralray
'''

import sys
import yaml
import roslib
roslib.load_manifest("kondo");

import rospy
from kondo.msg import servo

import serial
import struct
import time
import threading
import math

class kondo(serial.Serial):
    def setAngle(self, id, value):
        self.cmd = chr(0x80 | id) + chr(int(value)/128) + chr(int(value)%128)
        self.write( self.cmd )
        self.rec = self.read(6)
        return ord(self.rec[4])*0x80 + ord(self.rec[5])

def callback(msg):
    pubmsg = servo()
    pubmsg.stamp = rospy.get_rostime()
    pubmsg.id = msg.id
    try:
        pubmsg.angle = (k.setAngle(msg.id, 7500 + msg.angle/(0.000589049) )-7500) * (0.000589049)
        pub.publish( pubmsg )

    except:
        rospy.logerr("Communication error")

if __name__ == '__main__':
    argv = rospy.myargv(sys.argv)
    rospy.init_node('kondo')

    try:
        port = rospy.get_param('~port')
        rospy.loginfo('Parameter %s has value %s', rospy.resolve_name('~port'), port)
    except:
        rospy.logerr("Set correct port to %s", rospy.resolve_name('~port'))
        exit()

    k = kondo(port, 115200, timeout=0.15, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)

    pub = rospy.Publisher('/servo/rx', servo, queue_size=100)
    rospy.Subscriber("/servo/tx", servo, callback)
    rospy.spin()

    k.close()
