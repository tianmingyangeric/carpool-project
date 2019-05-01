# api to mach datas 
#AIzaSyBSVsY9UMx-K0RxQfQThtFyNf0rwlZacXk
#AIzaSyB5YDw-6B89z0kxdO3m8k5lnF_glbmpXrQ
from googleplaces import GooglePlaces
import googlemaps
#from importlib import reload
import sys
import ssl
from math import *
from datetime import datetime
import re
ssl._create_default_https_context = ssl._create_unverified_context
#reload(sys)

class GoogleMaps(object):

    def __init__(self):

        self._GOOGLE_MAPS_KEY = "AIzaSyB5YDw-6B89z0kxdO3m8k5lnF_glbmpXrQ"
        self._Google_Places = GooglePlaces(self._GOOGLE_MAPS_KEY)
        self._Google_Geocod = googlemaps.Client(key=self._GOOGLE_MAPS_KEY)

    def text_search(self, query, language=None, location=None):
        text_query_result = self._Google_Places.text_search(query=query, language=language, location=location)
        result_class = text_query_result.places
        result_dict = result_class[0].__dict__
        return result_dict['_geo_location']['lat'], result_dict['_geo_location']['lng']

    def calcDistance(self, Lat_A, Lng_A, Lat_B, Lng_B):
    	EARTH_RADIUS = 6378.137
    	radLat1 = radians(Lat_A)
    	radLat2 = radians(Lat_B)
    	a=radLat1-radLat2
    	b=radians(Lng_A)-radians(Lng_B)
    	s = 2 * asin(sqrt(pow(sin(a/2),2)+cos(radLat1)*cos(radLat2)*pow(sin(b/2),2)))  
    	s = s * EARTH_RADIUS
    	return s

    def driving_info(self, Lat_A, Lng_A, Lat_B, Lng_B):
        now = datetime.now()
        directions_result = self._Google_Geocod.directions(str(Lat_A) + ',' + str(Lng_A),
                                     str(Lat_B) + ',' + str(Lng_B),
                                     mode="driving",
                                     avoid="ferries",
                                     departure_time=now
                                    )
        return directions_result[0]['legs'][0]['duration']['text'],directions_result[0]['legs'][0]['distance']['text']
    def distance_unit(self,distance_str):
    	distance_str = distance_str.split()
    	if distance_str[1] == 'mi':
    		return float(distance_str[0]) * 1.6
    	elif distance_str[1] == 'km':
    		return float(distance_str[0])
    	elif distance_str[1] == 'm':
    		if float(distance_str[0]) < 1000:
    			return 0
    		return float(distance_str[0])/1000
    	elif distance_str[1] == 'ft':
    		if float(distance_str[0]) < 3000:
    			return 0
    		return float(distance_str[0])/3000

    def match_info(self,driverdep_latA,driverdep_lngA,driverdep_latB,driverdep_lngB,passengerdep_latA,passengerdep_lngA,passengerdep_latB,passengerdep_lngB):
    	origin_time, origin_distance = self.driving_info(driverdep_latA,driverdep_lngA,driverdep_latB,driverdep_lngB)
    	passenger_time, passenger_distance = self.driving_info(passengerdep_latA,passengerdep_lngA,passengerdep_latB,passengerdep_lngB)
    	extra_time1, extra_distance1 = self.driving_info(driverdep_latA,driverdep_lngA,passengerdep_latA,passengerdep_lngA)
    	extra_time2, extra_distance2 = self.driving_info(passengerdep_latB,passengerdep_lngB,driverdep_latB,driverdep_lngB)
    	passenger_distance = self.distance_unit(passenger_distance)
    	origin_distance = self.distance_unit(origin_distance)
    	extra_distance = self.distance_unit(extra_distance2) + self.distance_unit(extra_distance1)
    	#print (origin_distance, passenger_distance, extra_distance)
    	time_list = [origin_time, passenger_time, extra_time1,extra_time2]
    	for x in range(0,4):
    		new_time = time_list[x].split()
    		if len(new_time) == 4:
    			time_list[x] = float(new_time[0]) * 60 + float(new_time[2])
    		elif len(new_time) == 2:
    			time_list[x] = float(new_time[0])
    	match_dict = {'origin_time': time_list[0],
    	'passenger_time':time_list[1],
    	'extra_time' : time_list[2] + time_list[3],
    	'origin_distance': origin_distance,
    	'passenger_distance' : passenger_distance,
    	'extra_distance' : extra_distance}
    	return match_dict

