#!/usr/bin/python
# coding: utf-8 
#
# TCP客户端模拟器，基于文本协议 
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
        print('I: 正在连接到 %s:%s' %(host,port))
        socket.setdefaulttimeout(10) # timeout 
        self.ADDR=(host, port)  
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
            self.client.connect(self.ADDR)
	except Exception ,e:
	    print 'E: 连接失败 ',e 
	    return None
        print('I: 连接成功')
        print('I: 请输入指令:')

        while True:
            data=raw_input('>>>')
            if not data:
                print('I: 输入为空')
                continue
            if data.upper() in ["Q","QUIT","EXIT"]:
                print('I: 开始退出 ...')
                break
            # utf-8 encode 
            print('> 发送：%s' %(data))
            self.client.sendall(data+'\r\n')
            time.sleep(0.01)
            data=self.client.recv(self.BUFSIZ)
            if not data:
                print('I: 没有返回数据')
            else:
            	print('< 返回：%s' %(data))
        #end while
    #end init 
    
    def close(self):
        self.client.close()
#end class

import sys
if __name__ == '__main__':
    print('')
    print ' 欢迎使用TCP客户端模拟器 v', __version__,' by ',__author__
    print('  _____ ___ ___ ')
    print(' |_   _/ __| _ \\')
    print('   | || (__|  _/')
    print('   |_| \___|_|  ')
    print('')
    print('退出指令: q | quit | exit')
    ip = None
    port = None
    if (len(sys.argv)<2 or len(sys.argv)>3):
        print('')
	print '用法: python',sys.argv[0] ,'[IP] <PORT>'
        print('')
	sys.exit()
    if (len(sys.argv)==2):
        ip = '127.0.0.1'
	port = int(sys.argv[1])
    if (len(sys.argv)==3):
        ip = sys.argv[1]
        port = int(sys.argv[2])

    print('I: 启动 ...')
    client=TcpClient(ip,port)
    client.close()
    print('I: 已退出！')

#END
