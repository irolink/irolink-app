import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src')
from utils.color_convert import ColorConvertUtil


class IROLiNKUtilsColorConvertTest(unittest.TestCase):
    def test_rgbhex_01(self):
        rgb_hex = ColorConvertUtil.rgbstr_to_rgbhex('112233')
        assert rgb_hex['r'] == '11'
        assert rgb_hex['g'] == '22'
        assert rgb_hex['b'] == '33'

    def test_rgbdec_01(self):
        rgb_dec = ColorConvertUtil.rgbhex_to_rgbdec('00', '99', 'ff')
        assert rgb_dec['r'] == 0
        assert rgb_dec['g'] == 153
        assert rgb_dec['b'] == 255

    def test_rgbpercent_01(self):
        rgb_percent = ColorConvertUtil.rgbdec_to_rgbpercent(0, 153, 255)
        assert round(rgb_percent['r'], 1) == 0.0
        assert round(rgb_percent['g'], 1) == 59.8
        assert round(rgb_percent['b'], 1) == 99.6

    def test_cmyk_01(self):
        cmyk = ColorConvertUtil.rgbdec_to_cmyk(0, 153, 255)
        assert cmyk['c'] == 100
        assert cmyk['m'] == 40
        assert cmyk['y'] == 0
        assert cmyk['k'] == 0


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(IROLiNKUtilsColorConvertTest))
    return suite
