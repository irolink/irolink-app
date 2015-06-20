import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/')
import irolink


class IROLiNKTest(unittest.TestCase):
    def setUp(self):
        irolink.app.debug = False
        self.app = irolink.app.test_client()

    def test_show_default_01(self):
        raw_response = self.app.get(
            '/'
        )
        assert raw_response.status_code == 200

    def test_show_test_01(self):
        raw_response = self.app.get(
            '/test/'
        )
        assert raw_response.status_code == 200


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(IROLiNKTest))
    return suite
