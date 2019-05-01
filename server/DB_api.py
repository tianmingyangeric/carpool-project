#!/usr/bin/python3
import pymysql
from datetime import date, datetime


class DB:
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1',
                                  port=3306,
                                  user='root',
                                  password='12345678',
                                  db='CarPool')
        self.cursor = self.db.cursor()
    def sign_up(self, usr, pwd, phone, car, email, unique_id):
        """
		    usr sign up, insert usr information to dabases carpool table usr_info Args:
		usr,pwd,phone,birthday,car,email, unique_id (user's personal information)
		Returns:
		rersult from execute sql, 1 successful, 0 failed
		"""
        # sql insertion setence
        sql = "SELECT usr_name from usr_info WHERE usr_name = '%s'" % usr
        result = self.cursor.execute(sql)
        if result == 0:
            sql = "INSERT INTO usr_info (usr_name,password,phone_num,car_info,email,unique_id) \
    		VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % \
                   (usr, pwd, phone, car, email, unique_id)
            # execute sql and retun results 0/1
            result = self.cursor.execute(sql)
            # commit to database
            self.db.commit()
            return result
        else: 
            return 0

    def check_unique_id(self):
        """
        check column car_info  in table usr_info
        return : result
        """
        sql = "SELECT MAX(unique_id) from usr_info"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()[0]
        return result

    def read_unique_id(self,usr):

        sql = "SELECT unique_id from usr_info WHERE usr_name = '%s'" % usr
        self.cursor.execute(sql)
        result = self.cursor.fetchone()[0]
        #self.db.close()
        return result

    def sign_in(self, usr, pwd):
        # if usr name and pwd match, return 0/1
        sql = "SELECT * FROM usr_info WHERE usr_name = '%s' and password = '%s'" % (usr, pwd)
        result = self.cursor.execute(sql)
        # results = cursor.fetchall()
        return result

    def add_driver_info(self, Fname, Lname, plate, driver_licence, unique_id, car_make, car_model,gender):
        """
        add driver information to table car_info,undate column car_info to 1 in table usr_info
        return 1 if done, 0 if something wrong
        """
        sql = "INSERT INTO car_info(Fname,Lname, \
           Plate, Driver_license, Unique_id, make, model,gender) \
           VALUES ('%s', '%s', '%s', '%s', '%s', '%s' ,'%s','%s')" % \
              (Fname, Lname, plate, driver_licence, unique_id, car_make, car_model,gender)
        sql2 = "UPDATE usr_info SET car_info = '1' WHERE unique_id = '%s'" % unique_id
        try:
            result = self.cursor.execute(sql)
            self.cursor.execute(sql2)
            self.db.commit()
        except:
            return 0
        return result

    def check_driver_info(self, usr):
        """
            check column car_info  in table usr_info
            return : result
            """
        sql = "SELECT car_info from usr_info WHERE usr_name = '%s'" % usr
        self.cursor.execute(sql)
        result = self.cursor.fetchall()[0][0]
        return int(result)

    def add_driver_trip(self, name, unique, departure, destination, time, price, capability):
        """
    	add driver's name,unique,departure, destination, time ,price, cability to table driver_info
    	return 1 if done,else 0
    	"""
        sql = "INSERT INTO driver_info (name, unique_id, departure, destination, time, price, capability) " \
              "VALUES('%s','%s','%s','%s','%s','%s','%s')" % (name,unique,departure,destination,time,price,capability)
        try:
            result = self.cursor.execute(sql)
            self.db.commit()
        except:
            return 0
        return result

    def add_passenger_trip(self, name, unique, departure, destination, time, num_passenger):
        """
    	add passenger's name,unique,departure, destination, time to table passenger
    	return 1 if done,else 0
    	"""
        sql = ("INSERT INTO passenger(passenger_name, time, departure, destination, unique_id, num_passenger) VALUES('%s','%s','%s','%s','%s' ,'%s')" %\
              (name, time, departure, destination, unique, num_passenger))
        try:
            result = self.cursor.execute(sql)
            self.db.commit()
        except:
            return 0
        return result

    def get_driver_info(self,usr):
        """
        return name,unique,departure, destination, time from table driver_info
        and plate, car make from car info
        and phone number from usr
        """
        sql = "SELECT d.`name`, d.unique_id, d.departure,d.destination,d.time,c.Plate,c.make,u.phone_num " \
              "FROM driver_info as d INNER JOIN car_info as c ON d.unique_ID=c.unique_ID INNER JOIN usr_info as u " \
              "On d.unique_ID=u.unique_ID AND d.`name` = '%s'" % usr
        # try:
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        # for row in results:
        #     print (row)
        # except:
        #     return 0
        return results

    def drop_driver_trip(self,usr):
        """
         delete driver's trip from table driver info //can only post one or all will be deleted?
         """
        sql = "DELETE FROM driver_info WHERE `name` = '%s'" % usr
        # try:
        result = self.cursor.execute(sql)
        self.db.commit()
        return result

    def drop_passenger_trip(self,usr):
        """
         delete passenger's trip from table driver info
        """
        sql = "DELETE FROM passenger WHERE passenger_name = '%s'" % usr
        self.cursor.execute(sql)
        self.db.commit()
        return 0

    def check_driver_trip(self):
        sql = "SELECT * from driver_info"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def check_passenger_trip(self,unique):
        sql = "SELECT * from passenger WHERE unique_id = '%s'" % unique
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results[0]

    def get_car_info(self, unique):
        sql = "SELECT * from car_info WHERE unique_id = '%s'" % unique
        self.cursor.execute(sql)
        results = self.cursor.fetchall()[0]
        result_dict = {'first' : results[0],'last' : results[1],'plate' : results[2],'license' : results[3],'make' : results[5],'model' : results[6],'gender' : results[7] }
        return result_dict


    def updata_driver_cap(self, unique_id, capability):
        sql = "UPDATE driver_info SET capability = '"+ str(capability)+"' WHERE unique_id = '%s'" % unique_id
        result = self.cursor.execute(sql)
        self.db.commit()
        return result

    def check_passenger_number(self,unique_id):
        sql = "SELECT num_passenger from passenger WHERE unique_id = '%s'" % unique_id
        self.cursor.execute(sql)
        results = self.cursor.fetchone()[0]
        return results
    def check_driver_uniqueid(self,first,last):
        sql = "SELECT Unique_id FROM car_info WHERE Lname = '%s' and Fname = '%s'" % (last, first)
        self.cursor.execute(sql)
        results = self.cursor.fetchone()[0]
        return results

    def close(self):
        self.db.close()

db = DB()
#a = db.check_driver_uniqueid('yang','tianming')
#print (a)
# print(db.sign_in('eric_ty', '123456'))
#today = datetime.now().date()
# print(today)
# print(today)	# db = DB()
#r = db.sign_up('zmt3', '123123', '2269999999', '0', 'zmt@gmail.com', '9')
#r = db.check_unique_id()
#r = db.sign_in('zmt', '123123')
#r = db.add_driver_info('zmt','rrr', 'f2f2f2', 's00000003', '6', 'audi', 'q7')
#r = db.check_driver_info('zmt')
#r = db.read_unique_id('zmt')
#r = db.check_driver_trip()
#r = db.add_driver_trip('ytm', 5, 'Waterloo', 'Toronto', now, 15, '5')
#r = db.add_passenger_trip('zmt', 31, 'Waterloo', 'Shanghai', today,3)

#r = db.updata_driver_cap(4,1)
#r = db.check_passenger_trip(5)
#r = db.get_car_info(6)
#db.close()
#print((r))
#print(type(r))


