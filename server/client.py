#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py
import socket               # 导入 socket 模块
# import simplejson as json
import json
host = "10.34.89.186" # 获取本地主机名
port = 8889                # 设置端口号
BUFSIZE=1024

tcpCliSock = socket.socket()         # 创建 socket 对象
tcpCliSock.connect((host, port))

while True:
	data = "what is this"
	if not data:
		break
	# data = json.dumps(data)
	tcpCliSock.send(data.encode())
	response = tcpCliSock.recv(BUFSIZE).decode()
	# response = json.loads(response_json)
	# response = response_json
	if not response:
		break
	print(response)
	# break
	
tcpCliSock.close()
print("Finish!")
