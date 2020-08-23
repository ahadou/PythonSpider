# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 21:30:27 2020

@author: Giyn
"""

import csv
import pymysql
import requests


# 连接MySQL数据库（注意：charset参数是utf8而不是utf-8）
conn = pymysql.connect(host='localhost', user='root', password='******', db='music', charset='utf8')

# 创建游标对象
cur = conn.cursor()

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
name = '华晨宇'
page = 2

for x in range(page):
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'20',
    'w':name,
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }
    
    res = requests.get(url, params=params)
    json = res.json()
    lis = json['data']['song']['list']
    
    data = []
    for music in lis:
        song_name = music['name'] # 以song_name为键，查找歌曲名，把歌曲名赋值给name
        album = music['album']['name'] # 查找专辑名，把专辑名赋给album
        data.append([song_name,album])

    for each in data:
        i = tuple(each)
        sql = "INSERT INTO hcy VALUES" + str(i)
        cur.execute(sql) #执行SQL语句
    
    conn.commit() # 提交数据
cur.close() # 关闭游标
conn.close() # 关闭数据库
print("成功存入数据库")