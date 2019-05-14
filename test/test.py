#!/usr/bin/env python3
#coding=utf-8

import pymysql

def go() :
	conn=pymysql.connect(host='127.0.0.1', user='demo', passwd='test', db='essay_quinary') ;
	cur=conn.cursor();
	sql="show databases;"
	cur.execute(sql);
	r=cur.fetchall();
	print("aaaa");
	print(r);
	return r
