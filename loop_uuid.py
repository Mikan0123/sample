#!/usr/bin/env python3
import redis
import uuid
import sys
import datetime
import os
import shutil
import csv

# set
os.makedirs('./old' , exist_ok=True)

# initialize
list = []
uuid_str = ""
uuid_file = ""
now_time=""
file_name='UUID.csv'

# UUID.csvファイルをmoveしておく。
shutil.move(file_name,'./old/' + file_name)

# Redisに接続する
redis = redis.Redis(host='localhost',port=6379,db=0,password=None)

# uuid, datetimestamp を追加　
for var in range(10):
	uuid_str = str(uuid.uuid4())
	now_time = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))
	with open('./' + file_name ,'a') as f:
		print('%s,%s' %(uuid_str,now_time),file=f)
	redis.set(uuid_str,now_time)
	#print('%s,%s,%d' %(uuid_str,now_time,var))

# 'hoge'というキーで'huga'という値を追加
# redis.set('hoge','huga')

# UUID.csv ファイルを開いて読み込む
f = open('./' + file_name ,'r')
reader = csv.reader(f)

for row in reader:
	print(list.append(row[0]))
	hoge = redis.get(list.append(row[0]))
	print(hoge.decode())

f.close

# 追加した値を取得して表示する
# hoge = redis.get('hoge')
# print(hoge.decode())

# 追加した値を削除する
#result = redis.delete('hoge')

