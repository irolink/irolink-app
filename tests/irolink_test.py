import sys, os, unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/')
import irolink


class IROLiNKTest(unittest.TestCase):
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


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(IROLiNKTest))
    return suite
