#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(1, 'mavlink/pymavlink')

import mavutil
from mavlink_common import *

from argparse import ArgumentParser

def main():

    port = '/dev/ttyACM0'
    baud = 57600

    parser = ArgumentParser(description = 'Aquisição de dados PX4Flow')

    parser.add_argument('--device', '-d', action = 'store', dest = 'port',
                           default = '/dev/ttyACM0', required = False,
                           help = 'Configura porta serial (padrão: /dev/ttyACM0)')

    parser.add_argument('--baud', '-b', action = 'store', dest = 'baud',
                           default = 57600, required = False,
                           help = 'Configura baud rate (padrão: 57600)')

    arguments = parser.parse_args()

    mavDisp = mavutil.mavlink_connection(port, baud) 
    mavDisp.wait_heartbeat()
    print("Heartbeat from APM (system %u component %u)\n" % (mavDisp.target_system, mavDisp.target_component ))

    cin = ''

    while cin is not 's':
        msg = mavDisp.recv_msg()
        
        # print msg

        if msg is None: 
            print "NoneType"
            continue

        msg_id = msg.get_type()

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

        elif msg_id == 'DATA_TRANSMISSION_HANDSHAKE':
            print 'type =', msg.type
            print 'size =', msg.size
            print 'width =', msg.width
            print 'height =', msg.height
            print 'packets =', msg.packets
            print 'payload =', msg.payload
            print 'jpg_quality =', msg.jpg_quality

        elif msg_id == 'ENCAPSULATED_DATA':
            print 'seqnr =', msg.seqnr
            print 'data =', msg.data
            print 'len:', len(msg.data)

        elif msg_id == 'BAD_DATA':
            print 'data =', msg.data
            print 'reason =', msg.reason

        else:
            print msg
            # print msg.get_fieldnames()

        # if msg_id != 'BAD_DATA' and msg_id != 'ENCAPSULATED_DATA':
            # cin = raw_input('\nSair? (s/n): ')

        cin = raw_input('\nSair? (s/n): ')

if __name__ == '__main__':
    main()

    '''
    PARAM_VALUE:
    ['param_id', 'param_value', 'param_type', 'param_count', 'param_index']

    '''