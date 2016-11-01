#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Filename :  start.py
# Author   :  node@Shenzhen
# Created  :  2016-11-01 17:35
# Copyright:  (c) node
#
# Python script start template 
#
 
'''
这里可以写一个头部的多行注释

TODO:
- is_verbose
- debug mode and level
- getopt for argopt and arglist 
'''
__version__ = '1.0'
 
import os,sys,traceback
import time

# time stat 
start_time = time.time()

def close():
    # release  resource here, or output statistic info 
    print 
    print 'Totally took %f ms' %(time.time() - start_time)
    
import atexit
atexit.register(close)

# usage 
def usage(rc):
    """Show usage from 'About', then exit."""
    print globals()['__doc__']
    sys.exit(rc)

# execute shell cmd 
import subprocess
def do(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    (std, err) = p.communicate()
    # rc = p.returncode
    return std

def task1(d):
    """
    Task function 
 
        这里是函数的整体说明的多行注释
 
    Args:
 
    Returns:
 
    Raises:
    """
    time.sleep(0.2)
 
    return d
 
    # end of task1 function 
 
def task2(fout,result):
    fout_lines = len(result)
    fout_i = 0
    for line in result:
        fout_i += 1
        print 'process output line %d of %d' %(fout_i,fout_lines)
        fout.write(''.join([line,'\r\n']))
        if (fout_i % 100 == 0):
            fout.flush()
    fout.flush()
 
def main():
    fin_filename = 'input.txt'
    print 'read input file : %s ' %(fin_filename)
    if not os.path.exists(fin_filename):
        print '[ERROR] %s not exist.' %(fin_filename)
        return 
    fin = open(fin_filename,'r')
    data = fin.readlines()
    fin_lines = len(data)
    fin_i = 0
    result = []
    for line in data:
        fin_i += 1
        print 'process input line %d of %d'  %(fin_i,fin_lines)
        result.append(task1(line.replace('\r','').replace('\n','')))
    
    fout_filename = 'output.txt'
    print 'write output : %s' %(fout_filename)
    if os.path.exists(fout_filename):
        print '[WARN] %s has exist. Will rewrite it !' %(fout_filename)
    with open(fout_filename,'w') as fout:
        task2(fout,result)
    print 'output file OK.'
 
    # end of main function
 
if __name__ == '__main__':
    print 'start ...'
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt:
        print("Keyboard interrupt.")
        sys.exit(0)
    except SystemExit:
        sys.exit(0)
    except Exception, e:
        print str(e)
        traceback.print_exc()
        sys.exit(1)
    else:
        print 'Unknown error.'
    finally:
        print '...finish'