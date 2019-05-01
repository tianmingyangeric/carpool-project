#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket      
import unittest
import json

class SignUpTestCase(unittest.TestCase):
	def setUp(self):
		host = '10.34.89.186'
		port = 8889
		BUFSIZE=1024
		self.tcpCliSock = socket.socket()
		self.tcpCliSock.connect((host, port))

	def test_correct_usr(self):

		data =  { 'function' : 'sign_up', 'user name' : 'ytmm', 'password' : 8888, "phone" : 812312,"email":'asdas'} 
		data = json.dumps(data)
		self.tcpCliSock.send(data.encode())
		data = json.dumps(data)
		response = self.tcpCliSock.recv(1024).decode()
		self.assertEqual(response, 'YES')

	def test_repeat_usr(self):
		data =  { 'function' : 'sign_up', 'user name' : 'ytm', 'password' : 8888, "phone" : 812312,"email":'asdas'} 
		data = json.dumps(data)
		self.tcpCliSock.send(data.encode())
		data = json.dumps(data)
		response = self.tcpCliSock.recv(1024).decode()
		self.assertEqual(response, 'NO')

	def tearDown(self):
		self.tcpCliSock.close()

if __name__ == '__main__':
    unittest.main()