# -*- coding: utf-8 -*-


class ColorConvertUtil(object):
    @staticmethod
    def rgbstr_to_rgbhex(code):
        ret = {
            'r': code[0:2],
            'g': code[2:4],
            'b': code[4:6]
        }
        return ret

    @staticmethod
    def rgbhex_to_rgbdec(r, g, b):
        ret = {
            'r': int(r, 16),
            'g': int(g, 16),
            'b': int(b, 16)
        }
        return ret

    @staticmethod
    def rgbdec_to_rgbpercent(r, g, b):
        ret = {
            'r': float(r) / 256 * 100,
            'g': float(g) / 256 * 100,
            'b': float(b) / 256 * 100
        }
        return ret

    @staticmethod
    def rgbdec_to_cmyk(r, g, b):
        if (r == 0) and (g == 0) and (b == 0):
            return {'c': 0, 'm': 0, 'y': 0, 'k': 100}
        c = 1 - r / float(255)
        m = 1 - g / float(255)
        y = 1 - b / float(255)
        min_cmy = min(c, m, y)
        c = (c - min_cmy) / (1 - min_cmy)
        m = (m - min_cmy) / (1 - min_cmy)
        y = (y - min_cmy) / (1 - min_cmy)
        k = min_cmy
        return {'c': c*100, 'm': m*100, 'y': y*100, 'k': k*100}
