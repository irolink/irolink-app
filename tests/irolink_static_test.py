import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/')
import irolink


class IROLiNKStaticTest(unittest.TestCase):
    def setUp(self):
        irolink.app.debug = False
        self.app = irolink.app.test_client()

    def test_css_file_01(self):
        raw_response = self.app.get(
            '/assets/css/style.css'
        )
        assert raw_response.status_code == 200
        assert raw_response.content_type == 'text/css; charset=utf-8'

    def test_js_file_01(self):
        raw_response = self.app.get(
            '/assets/js/script.js'
        )
        assert raw_response.status_code == 200
        assert raw_response.content_type == 'application/javascript'

    def test_static_file_01(self):
        raw_response = self.app.get(
            '/robots.txt'
        )
        assert raw_response.status_code == 200

    def test_static_file_02(self):
        raw_response = self.app.get(
            '/favicon.ico'
        )
        assert raw_response.status_code == 404


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(IROLiNKStaticTest))
    return suite
