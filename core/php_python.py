#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import socket
import os

import process

# -------------------------------------------------
# 基本配置
# -------------------------------------------------
LISTEN_PORT = 10240     #服务侦听端口
CHARSET = "utf-8"       #设置字符集（和PHP交互的字符集）


# -------------------------------------------------
# Oracle数据库连接配置
# -------------------------------------------------
#import cx_Oracle
#数据库字符集
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8' 
#数据库连接池
#pool = cx_Oracle.SessionPool(
#    user='diaoyf',
#    password='700327',
#    dsn='127.0.0.1/xe',
#    min=5,
#    max=10,
#    increment=1,
#    connectiontype=cx_Oracle.Connection,
#    threaded=True,
#    getmode=cx_Oracle.SPOOL_ATTRVAL_NOWAIT,
#    homogeneous=True)

#def getConn():
#    """获得数据库连接的公共函数"""
#    return pool.acquire()
#
#def closeConn(conn):
#    """释放数据库连接的公共函数"""
#    pool.release(conn)

import pymysql

def getConn() :
	return pymysql.connect(
		host='localhost',
		user='demo',
		passwd='test',
		db='ppython',
		port=3306)

def closeConn(conn):
	conn.close();

# -------------------------------------------------
# 主程序
#    请不要随意修改下面的代码
# -------------------------------------------------
if __name__ == '__main__':

    print ("-------------------------------------------")
    print ("- PPython Service")
    print ("- Time: %s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) )
    print ("-------------------------------------------")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #TCP/IP
    sock.bind(('', LISTEN_PORT))  
    sock.listen(5)  

    print ("Listen port: %d" % LISTEN_PORT)
    print ("charset: %s" % CHARSET)
    print ("Server startup...")

    while 1:  
        connection,address = sock.accept()  #收到一个请求

        #print ("client's IP:%s, PORT:%d" % address)

        # 处理线程
        try:
            process.ProcessThread(connection).start()
        except:
            pass
