import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/')
import irolink


class IROLiNKDetailTest(unittest.TestCase):
    def setUp(self):
        irolink.app.debug = False
        self.app = irolink.app.test_client()

    def test_show_rgb_hex_01(self):
        raw_response = self.app.get(
            '/rgb-hex/ffffff'
        )
        assert raw_response.status_code == 200

    def test_show_rgb_hex_02(self):
        raw_response = self.app.get(
            '/rgb-hex/000000'
        )
        assert raw_response.status_code == 200

    def test_show_rgb_hex_03(self):
        raw_response = self.app.get(
            '/rgb-hex/cd0000'
        )
        assert raw_response.status_code == 200

    def test_show_rgb_hex_04(self):
        raw_response = self.app.get(
            '/rgb-hex/008b00'
        )
        assert raw_response.status_code == 200

    def test_show_rgb_hex_05(self):
        raw_response = self.app.get(
            '/rgb-hex/0012ef'
        )
        assert raw_response.status_code == 200

    def test_show_rgb_hex_06(self):
        raw_response = self.app.get(
            '/rgb-hex/FFFFFF'
        )
        assert raw_response.status_code == 302

    def test_show_rgb_hex_07(self):
        raw_response = self.app.get(
            '/rgb-hex/FF0000'
        )
        assert raw_response.status_code == 302

    def test_show_rgb_hex_08(self):
        raw_response = self.app.get(
            '/rgb-hex/00FF00'
        )
        assert raw_response.status_code == 302

    def test_show_rgb_hex_09(self):
        raw_response = self.app.get(
            '/rgb-hex/0000FF'
        )
        assert raw_response.status_code == 302

    def test_show_rgb_hex_10(self):
        raw_response = self.app.get(
            '/rgb-hex/0000ffaa'
        )
        assert raw_response.status_code == 404

    def test_show_rgb_hex_11(self):
        raw_response = self.app.get(
            '/rgb-hex/0000ff11'
        )
        assert raw_response.status_code == 404


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(IROLiNKDetailTest))
    return suite
