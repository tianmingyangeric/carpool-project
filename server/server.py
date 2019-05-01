#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
# import simplejson as json
import json
from DB_api import DB
from time import ctime
import time
from INFO_api import GoogleMaps
from control import control

port = 8889
host = '10.34.89.186'
BUFSIZE = 1024
tcp_socket = socket.socket()
tcp_socket.bind((host, port))
tcp_socket.listen(5)
while True:
    result = None
    tcpcli_socket, addr = tcp_socket.accept()     # 建立客户端连接。
    print ('connection address: ', addr)
    data = tcpcli_socket.recv(BUFSIZE)
    json_data = json.loads(data.decode())
    function_name = json_data['function']
    ctr = control()
    if function_name == "sign_in":
        result = ctr.sign_in(json_data)
        #tcpcli_socket.send(result)
    elif function_name == "sign_up":
        result = ctr.sign_up(json_data)
        #tcpcli_socket.send(result)
    elif function_name == "driver_button":
        result = ctr.press_driver_button(json_data)
        #tcpcli_socket.send(result)

    elif function_name == "driver_register":

        result = ctr.driver_register(json_data)
        #tcpcli_socket.send(result)

    elif function_name == "driver_trip":

        result = ctr.driver_trip(json_data)
        #tcpcli_socket.send(result)

    elif function_name == "passenger_trip":
        result = ctr.passenger_trip(json_data)
        #tcpcli_socket.send(result)

    elif function_name == "search_match":

        result = ctr.passenger_trip(json_data)

        if result != 'NO'.encode():
            result = ctr.search_match(json_data)
        else:
            no_dict = {'result':'NO'}
            result_json = json.dumps(no_dict)
            result = result_json.encode()

    elif function_name == "exit":
        result = ctr.drop_passenger_trip(json_data)

    elif function_name == "confirm":
        result = ctr.confirm_passenger_trip(json_data)


    if result != None:
        tcpcli_socket.send(result)


    tcpcli_socket.close() 








