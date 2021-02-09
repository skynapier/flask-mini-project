import unittest
from startup import create_app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app("test")
        self.app = app.test_client()


    def test_something(self):
        self.assertTrue(self.app.application.config['TESTING'] is True)


if __name__ == '__main__':
    unittest.main()
