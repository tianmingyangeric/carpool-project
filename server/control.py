#!/usr/bin/python3
import pymysql
from datetime import date, datetime
# -*- coding: UTF-8 -*-
import socket
import json
from DB_api import DB
from time import ctime
import time
from INFO_api import GoogleMaps

class control:
    def sign_in(self,json_data):
        db = DB()
        result = db.sign_in(json_data["user name"],json_data["password"])
        result_list = ['NO','YES']
        result = result_list[result].encode()
        return result

    def sign_up(self,json_data):
        db = DB()
        unique_id = db.check_unique_id() + 1
        result = db.sign_up(json_data["user name"], json_data["password"], \
            json_data["phone"], 0, json_data["email"], unique_id)
        result_list = ['NO','YES']
        result = result_list[result].encode()
        return result

    def press_driver_button(self,json_data):
        db = DB()
        result = db.check_driver_info(json_data["user name"])
        result_list = ['NO','YES']
        result = result_list[result].encode()
        return result

    def driver_register(self,json_data):
        db = DB()
        unique_id = db.read_unique_id(json_data["user name"])
        result = db.add_driver_info(json_data["Fname"], json_data["Lname"], json_data["plate"], json_data["driver_licence"],unique_id, json_data["car_make"], json_data["car_model"], json_data["gender"])
        result_list = ['NO','YES']
        restlt = result_list[result].encode()
        return result

    def driver_trip(self,json_data):
        db = DB()
        unique_id = db.read_unique_id(json_data["user name"])
        dep_address = json_data["Departure street address"] + ',' + json_data["Departure city"] + ',' + json_data["Departure province"]
        des_address = json_data["Destination street address"] +',' + json_data["Destination city"] + ',' + json_data["Destination province"]
        time = json_data["Date"] +',' + json_data["Time"]
        result = db.add_driver_trip(json_data["name"], unique_id, dep_address, des_address, time, json_data["price"], json_data["capability"])
        result_list = ['NO','YES']
        restlt = result_list[result].encode()
        return result

    def passenger_trip(self,json_data):
        db = DB()
        unique_id = db.read_unique_id(json_data["user name"])
        dep_address = json_data["Departure street address"] + ',' + json_data["Departure city"] + ',' + json_data["Departure province"]
        des_address = json_data["Destination street address"] +',' + json_data["Destination city"] + ',' + json_data["Destination province"]
        time = json_data["Date"] +',' + json_data["Time"]
        result = db.add_passenger_trip(json_data["name"], unique_id, dep_address, des_address, time, json_data["num_passenger"])
        result_list = ['NO','YES']
        restlt = result_list[result].encode()
        return result

    def drop_passenger_trip(json_data):
        db = DB()
        result = db.drop_passenger_trip(json_data["user name"])
        result_list = ['NO','YES']
        restlt = result_list[result].encode()
        return result

    def confirm_passenger_trip(json_data):
        db = DB()
        unique_id = db.read_unique_id(json_data["user name"])
        passenger_num = db.check_passenger_number(unique_id)
        result = db.drop_passenger_trip(json_data["user name"])
            if result == 0:
                return 'NO'.encode()
        driver_id = db.check_driver_uniqueid(json_data["First"],json_data["Last"])
        result = db.updata_driver_cap(driver_id, capability)
        result_list = ['NO','YES']
        restlt = result_list[result].encode()
        return result


    def search_match(self,json_data):
        gm = GoogleMaps()
        db = DB()
        no_dict = {'result':'NO'}
        result_json = json.dumps(no_dict)

        unique_id = db.read_unique_id(json_data["user name"])
        passenger_trip = db.check_passenger_trip(unique_id)
        driver_trip = db.check_driver_trip()
        pass_latA,pass_lngA = gm.text_search(passenger_trip[2])
        pass_latB,pass_lngB = gm.text_search(passenger_trip[3])
        driver_list = []
        for drivers in driver_trip:
            if drivers[4].date() == passenger_trip[1].date():
                dri_latA,dri_lngA = gm.text_search(drivers[2])
                dri_latB,dri_lngB = gm.text_search(drivers[3])
                driver_dict = gm.match_info(dri_latA,dri_lngA,dri_latB,dri_lngB,pass_latA,pass_lngA,pass_latB,pass_lngB)
                driver_dict['unique_id'] = drivers[1]
                driver_list.append(driver_dict)
        choosen_driver = 0
        if not driver_list:
            return (result_json.encode())
        for info in driver_list:
            distance = info['extra_distance']
            if (distance < 1000) and (choosen_driver == 0):
                choosen_driver = info
            elif choosen_driver != 0:
                dis = choosen_driver['extra_distance']
                if (distance < dis):
                    choosen_driver = info
        if choosen_driver == 0:
            return (result_json.encode())
        result_dict = db.get_car_info(choosen_driver['unique_id'])
        db.close()
        driver_info =[]
        for driver in driver_trip:
            if driver[1] == choosen_driver['unique_id']:
                driver_info = driver
                break
        result_dict['capability'] = driver_info[6]
        result_dict['price'] = driver_info[5]
        result_json = json.dumps(result_dict)
        return (result_json.encode())

db = control()


