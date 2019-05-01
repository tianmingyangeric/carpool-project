#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket      
import unittest
import json

class SignInTestCase(unittest.TestCase):
	def setUp(self):
		host = '10.34.89.186'
		port = 8889
		BUFSIZE=1024
		self.tcpCliSock = socket.socket()
		self.tcpCliSock.connect((host, port))

	def test_correct_usr(self):
		data =  { 'function' : 'sign_in', 'user name' : 'ytm', 'password' : 8888} 
		data = json.dumps(data)
		self.tcpCliSock.send(data.encode())
		data = json.dumps(data)
		response = self.tcpCliSock.recv(1024).decode()
		self.assertEqual(response, 'YES')

	def test_wrong_usr(self):
		data =  { 'function' : 'sign_in', 'user name' : 'ytm', 'password' : 123123} 
		data = json.dumps(data)
		self.tcpCliSock.send(data.encode())
		data = json.dumps(data)
		response = self.tcpCliSock.recv(1024).decode()
		self.assertEqual(response, 'NO')

	def test_empty_usr(self):
		data =  { 'function' : 'sign_in', 'user name' : 'ytm', 'password' : 123456} 
		data = json.dumps(data)
		self.tcpCliSock.send(data.encode())
		data = json.dumps(data)
		response = self.tcpCliSock.recv(1024).decode()
		self.assertEqual(response, 'NO')

	def tearDown(self):
		self.tcpCliSock.close()

if __name__ == '__main__':
    unittest.main()