#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(1, 'mavlink/pymavlink')

import mavutil

from mavlink_common import *

# from argparse import ArgumentParser

def main():
    mavDisp = mavutil.mavlink_connection("/dev/ttyACM0", 57600)
    
    mavDisp.wait_heartbeat()
    
    print("Heartbeat from APM (system %u component %u)\n" % (mavDisp.target_system, mavDisp.target_component ))

    cin = ''
    while cin is not 's':
        msg = mavDisp.recv_msg()
        
        # print msg

        msg_id = msg.get_type()

        if msg_id == None: 
            print "NoneType"
            continue

        print '\n%s:' % msg_id

        if msg_id == 'NAMED_VALUE_FLOAT':
            print 'name =', msg.name
            print 'value =', msg.value

        elif msg_id == 'NAMED_VALUE_INT':
            print 'name =', msg.name
            print 'value =', msg.value

        elif msg_id == 'DEBUG_VECT':
            print 'x =', msg.x
            print 'y =', msg.y
            print 'z =', msg.z

        elif msg_id == 'OPTICAL_FLOW':
            print 'flow_x =', msg.flow_x
            print 'flow_y =', msg.flow_y
            print 'flow_comp_m_x =', msg.flow_comp_m_x
            print 'flow_comp_m_y =', msg.flow_comp_m_y
            print 'quality =', msg.quality
            print 'ground_distance =', msg.ground_distance

        elif msg_id == 'OPTICAL_FLOW_RAD':
            print 'integrated_x =', msg.integrated_x
            print 'integrated_y =', msg.integrated_y
            print 'integrated_xgyro =', msg.integrated_xgyro
            print 'integrated_ygyro =', msg.integrated_ygyro
            print 'integrated_zgyro =', msg.integrated_zgyro
            print 'temperature =', msg.temperature
            print 'quality =', msg.quality
            print 'time_delta_distance_us =', msg.time_delta_distance_us
            print 'distance =', msg.distance

        else:
            print msg.get_fieldnames()

        cin = raw_input('\nSair? (s/n): ')

if __name__ == '__main__':
    main()


