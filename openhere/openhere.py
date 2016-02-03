#!/usr/bin/env python
#
# Start simple web server here , and visit by QR code !
#
# By YangZhentao @vivo @2015.9
#


qr_filename = 'qr.png'
tmp_html_filename = '.clickme.to.get.QRcode.html'
PORT = 19840

import socket
import fcntl  
import struct
import os

#ifname='etho0' or 'lo'
def get_local_ip(ifname='eth0'):  
    try:  
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
        return socket.inet_ntoa(fcntl.ioctl(  
            s.fileno(),    
            0x8915, # SIOCGIFADDR    
            struct.pack('256s', ifname[:15])    
        )[20:24])   
    except:  
        ips = os.popen("LANG=C ifconfig | grep \"inet addr\" | grep -v \"127.0.0.1\" | awk -F \":\" '{print $2}' | awk '{print $1}'").readlines()  
        if len(ips) > 0:  
            return ips[0]  
    return '' 
IP = get_local_ip(ifname='etho')
URL = 'http://%s:%d' %(IP.strip(),PORT)

import re,urllib2
#unused now
class IpGetter:
    def getmyip(self):
        try:
            myip = self.visit("http://www.ip138.com/ip2city.asp")
        except:
            try:
                myip = self.visit("http://www.bliao.com/ip.phtml")
            except:
                try:
                    myip = self.visit("http://www.whereismyip.com/")
                except:
                    myip = "" # "So sorry!!!"
        return myip
    def visit(self,url):
        opener = urllib2.urlopen(url)
        if url == opener.geturl():
            str = opener.read()
        return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)

#g = IpGetter()
#outerip = g.getmyip()

# generate qrcode 
def out_html():
    s = '<html><head><meta name="viewport" content="width=device-width,target-densitydpi=high-dpi,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/></head><body><div style="text-align:center;"><img src="'+qr_filename+'" alt="scan me !"/><br/>Scan me !  By YangZhentao</div>'    

    index_html = open(tmp_html_filename,'w')
    index_html.write(s)
    index_html.close()


def out_qrcode():
    import qrcode 
    qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4, )
    qr.add_data(URL) 
    qr.make(fit=True)  
    img = qr.make_image()
    img.save(qr_filename)

def eog():
    import os
    os.system('eog '+qr_filename)

# start http server 
def svc(t):
    import SimpleHTTPServer
    import SocketServer

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "Running ",URL
    try:
        httpd.serve_forever()
    except KeyboardInterrupt,e:
        print 'Receive ctrl+c'
        # delete tmp file 
        if os.path.isfile(tmp_html_filename):
            os.remove(tmp_html_filename)
        if os.path.isfile(qr_filename):
            os.remove(qr_filename)
    t.join()

if __name__ == '__main__':
    print 'Start ...'

    out_qrcode()
    out_html()

    import threading
    t = threading.Thread(target=eog)
    t.setDaemon(True)
    t.start()

    svc(t)

    print 'Shutdown.'
#end
