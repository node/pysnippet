#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# TCP client 
#
# BY nodexy@gmail @201508 @SZ 
__version__ = 0.1
__author__ = 'Chris Yang'
__email__ = 'nodexy@gmail.com'

import socket
import time
import random

def log(*s):
    print time.strftime('%Y-%m-%d %H:%M:%S.%s'),
    for ss in s:
        print ss,
    print

def think(n): # think n seconds 
    time.sleep(n)


def action_login(sock):
    sock.send('your username and password')

def action_1(sock):
    sock.send('your message 1')

def action_2(sock):
    sock.send('your message 2')

def action_3(sock):
    sock.send('your message 3')

def action_logout(sock):
    sock.send('quit')

def get_reply(sock):
    return sock.recv(1024)

def open_port(server_host,server_port,local_port):  
    log('connect to server:',server_host,server_port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('',local_port))
    sock.connect((server_host, server_port))
    sname = sock.getsockname() 
    log('connect ok: fileno=',sock.fileno(),'sockname=',sname)

    think(60 * random.randint(1,3)) # n minutes ?
    log(' I am socket ',sname ,' I am so boring >x<')

    sock.send('Hello Mr. server ,I am ' + str(sname))
    think(60 * random.randint(1,5))
    print get_reply(sock) 


    action_login(sock)

    action_1(sock)
    think(2)
    print get_reply(sock)

    action_2(sock)
    think(2)

    action_3(sock)

    #think(60 * random.randint(1,5))

    log('I am quit.')
    think(random.randint(1,5))
    action_logout()

    log('close sock',sname)
    sock.close()
    #end    

import threading
def main(host,port,num):
    st = time.strftime('%Y-%m-%d %H:%M:%S.%s')
    print '>>>start: ',st
    tlist = []
    for i in range(1,num+1):
        t = threading.Thread(target=open_port,args=(host,port,10000+i))
        t.setDaemon(True)
        tlist.append(t)
        t.start()
        time.sleep(0.1)

    for t in tlist:
        t.join()

    print '>>>from :',st
    print '<<<end  :',time.strftime('%Y-%m-%d %H:%M:%S.%s')

import sys
from optparse import OptionParser
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-H', '--host', action='store',default='localhost',
                      type='string', dest='host', help='server hostname or ip')
    parser.add_option('-p', '--port', action='store',
                      type='int', dest='port', help='server port')
    parser.add_option('-n', '--number', action='store',
                      type='int', dest='number',
                      help='produce NUMBER TCP clients')

    options, args = parser.parse_args()

    if not options.port:
        print("Port is required!")
        parser.print_help()
        sys.exit(1)
    if not options.number:
        print("Number is required!")
        parser.print_help()
        sys.exit(1)

    main(options.host,options.port,options.number)
#end
