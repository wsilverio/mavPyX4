#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(1, 'mavlink/pymavlink')

import mavutil
# from mavlink_common import *

from argparse import ArgumentParser

def main():

    port, baud = '/dev/ttyACM0', 57600

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

    while cin != 's':
        msg = mavDisp.recv_msg()
        
        # print msg

        if msg is None: 
            print "NoneType"

        elif msg.get_type() == 'BAD_DATA' or msg.get_type() == 'ENCAPSULATED_DATA':
            print msg.get_type()

        else:
            print '\n'
            dic = msg.to_dict()

            for field in msg.get_fieldnames():
                print field, ': ', dic[field]

            cin = raw_input('\nSair? (s/n): ')

        # ex.
        # if msg.get_type() == 'ENCAPSULATED_DATA':
        #     print 'seqnr =', msg.seqnr
        #     print 'data =', msg.data
        #     print 'len:', len(msg.data)


        # Traceback (most recent call last):
        # File "./teste_modo_texto.py", line 61, in <module>
        #     main()
        # File "./teste_modo_texto.py", line 35, in main
        #     msg = mavDisp.recv_msg()
        # File "mavlink/pymavlink/mavutil.py", line 286, in recv_msg
        #     s = self.recv(n)
        # File "mavlink/pymavlink/mavutil.py", line 730, in recv
        #     ret = self.port.read(n)
        # File "/usr/lib/python2.7/dist-packages/serial/serialposix.py", line 453, in read
        #     buf = os.read(self.fd, size-len(read))
        # OSError: [Errno 11] Resource temporarily unavailable

if __name__ == '__main__':
    main()