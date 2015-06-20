import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/')
import irolink


class IROLiNKAPIImageTest(unittest.TestCase):
    def setUp(self):
        irolink.app.debug = False
        self.app = irolink.app.test_client()

    def test_found_image_01(self):
        raw_response = self.app.get(
            '/api/one-color-image/ffffff'
        )
        assert raw_response.status_code == 200
        assert raw_response.content_type == 'image/png'

    def test_found_image_02(self):
        raw_response = self.app.get(
            '/api/one-color-image/000000'
        )
        assert raw_response.status_code == 200
        assert raw_response.content_type == 'image/png'

    def test_notfound_image_02(self):
        raw_response = self.app.get(
            '/api/one-color-image/0000000'
        )
        assert raw_response.status_code == 404
        assert raw_response.content_type != 'image/png'


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(IROLiNKAPIImageTest))
    return suite
