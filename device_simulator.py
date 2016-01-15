#!/usr/bin/python
# coding: utf-8 
#
# Device simulator 
#
# BY nodexy@gmail @201411 @SZ 
__version__ = 0.1
__author__ = 'Chris Yang'
__email__ = 'nodexy@gmail.com'

import socket
import time

class TcpClient:
     
    BUFSIZ=1024 * 4

    def __init__(self,host,port):
        print('I: Connect to %s:%s' %(host,port))
        socket.setdefaulttimeout(10) # timeout 
        self.ADDR=(host, port)  
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
            self.client.connect(self.ADDR)
	except Exception ,e:
	    print 'E: Connect failed. ',e 
	    return None
        print('I: Connect OK.')
        print('I: Please input command:')

        while True:
            data=raw_input('>>>')
            if not data:
                print('I: Input nothing.')
                continue
            if data.upper() in ["Q","QUIT","EXIT"]:
                print('I: Quit ...')
                break
            # utf-8 encode 
            print('> SEND：%s' %(data))
            self.client.sendall(data+'\r\n')
            time.sleep(0.01)
            data=self.client.recv(self.BUFSIZ)
            if not data:
                print('I: No response.')
            else:
            	print('< RECV：%s' %(data))
        #end while
    #end init 
    
    def close(self):
        self.client.close()
#end class

import sys
if __name__ == '__main__':
    print('')
    print '  Device Simulator v', __version__,' by ',__author__
    print('  _____ ___ ___ ')
    print(' |_   _/ __| _ \\')
    print('   | || (__|  _/')
    print('   |_| \___|_|  ')
    print('')
    print('For quit: q | quit | exit')
    host,port = None,None
    if (len(sys.argv)<2 or len(sys.argv)>3):
        print('')
	print 'USAGE: python',sys.argv[0] ,'[HOST|127.0.0.1] <PORT>'
        print('')
	sys.exit()
    if (len(sys.argv)==2):
        host = '127.0.0.1'
	port = int(sys.argv[1])
    if (len(sys.argv)==3):
        host = sys.argv[1]
        port = int(sys.argv[2])

    print('I: Start ...')
    client=TcpClient(host,port)
    client.close()
    print('I: Exit！')

#END
