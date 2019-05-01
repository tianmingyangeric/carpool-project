import unittest
import sys
sys.path.append('..')
from server import DB_api
from datetime import datetime

today = datetime.now()

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.db = DB_api.DB()

    def test_signUp(self):
        self.assertTrue(self.db.sign_up('aaa','111111','1231231234',0,'ttt@ttt.tt',999))

    def test_checkUniqueId(self):
        self.assertEqual(self.db.check_unique_id(),999)

    def test_readUniqueId(self):
        self.assertEqual(self.db.read_unique_id('aaa'),999)

    def test_signIn(self):
        self.assertTrue(self.db.sign_in('ttt','111111'))

    def test_addDriverInfo(self):
        self.assertEqual(self.db.check_driver_info('aaa'),0)
        self.assertTrue(self.db.add_driver_info('firstName','lastName','Waterloo','s000123','999','BWM','La','female'))
        self.assertEqual(self.db.check_driver_info('aaa'),1)

    def test_addDriverTrip(self):
        self.assertTrue(self.db.add_driver_trip('aaa','999','Toronto','Waterloo',today,30,'4'))

    def test_addPassengerTrip(self):
        self.assertTrue(self.db.add_passenger_trip('aaa','999','Toronto','Waterloo',today,2))

    def test_dropDriverTrip(self):
        self.assertFalse(self.db.drop_driver_trip('aaa'))

    def test_dropPassengerTrip(self):
        self.assertFalse(self.db.drop_passenger_trip('aaa'))
        
    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    unittest.main()
#    HTMLTestRunner.main()
