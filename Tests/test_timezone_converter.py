import unittest


class MyTestCase(unittest.TestCase):

    def test_basecase(self):
        lat, lng = -33.865143, 151.209900
        timestamp = 1480933800
        from utils.timezone_converter_utils import convert_timestamp_with_coordinates
        time = convert_timestamp_with_coordinates(lat, lng, timestamp)

        self.assertEqual(time, '05/12/2016 21:30 AEDT +1100')





if __name__ == '__main__':
    unittest.main()
