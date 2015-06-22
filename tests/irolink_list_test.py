import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/')
import irolink


class IROLiNKListTest(unittest.TestCase):
    def setUp(self):
        irolink.app.debug = False
        self.app = irolink.app.test_client()

    def test_show_html16color_01(self):
        raw_response = self.app.get(
            '/html-16-base-colors'
        )
        assert raw_response.status_code == 200

    def test_show_x11color_01(self):
        raw_response = self.app.get(
            '/x11-colors'
        )
        assert raw_response.status_code == 200


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(IROLiNKListTest))
    return suite
