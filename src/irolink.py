from flask import abort
from flask import Flask
from flask import redirect
from flask import render_template
from flask import Response
from PIL import Image
import colorsys
import re
import StringIO

app = Flask(__name__, static_url_path='')


@app.route('/')
def show_root():
    return render_template('default.html')


@app.route('/test/')
def show_test():
    return render_template('test.html')


@app.route('/rgb-hex/<code>')
def color_detail_rgb_hex(code):
    if not re.match(r'^([0-9a-zA-Z]){6}$', code):
        abort(404)
    if re.match(r'.*[A-Z].*', code):
        return redirect('/rgb-hex/' + code.lower())
    rgb_hex = ColorConvertUtil.rgbstr_to_rgbhex(code)
    rgb_dec = ColorConvertUtil.rgbhex_to_rgbdec(
        rgb_hex['r'], rgb_hex['g'], rgb_hex['b'])
    rgb_percent = ColorConvertUtil.rgbdec_to_rgbpercent(
        rgb_dec['r'], rgb_dec['g'], rgb_dec['b'])
    cmyk = ColorConvertUtil.rgbdec_to_cmyk(
        rgb_dec['r'], rgb_dec['g'], rgb_dec['b'])
    raw_hls = colorsys.rgb_to_hls(rgb_dec['r'], rgb_dec['g'], rgb_dec['b'])
    hsl = {'h': raw_hls[0], 's': raw_hls[2], 'l': raw_hls[1]}
    raw_hsv = colorsys.rgb_to_hsv(rgb_dec['r'], rgb_dec['g'], rgb_dec['b'])
    hsv = {'h': raw_hsv[0], 's': raw_hsv[1], 'v': raw_hsv[2]}

    nearly_colors = []
    nearly_colors.append({
        'r': rgb_hex['r'],
        'g': rgb_hex['g'],
        'b': rgb_hex['b']
    })
    num = 0
    tmp_r = rgb_dec['r']
    tmp_g = rgb_dec['g']
    tmp_b = rgb_dec['b']
    while num < 5:
        num += 1
        tmp_r -= 10
        tmp_g -= 10
        tmp_b -= 10
        r = tmp_r if 0 < tmp_r else 0
        g = tmp_g if 0 < tmp_g else 0
        b = tmp_b if 0 < tmp_b else 0
        nearly_colors.append({
            'r': '0' + hex(r)[2:3] if r < 16 else hex(r)[2:4],
            'g': '0' + hex(g)[2:3] if g < 16 else hex(g)[2:4],
            'b': '0' + hex(b)[2:3] if b < 16 else hex(b)[2:4]
        })
        if (r == 0 and g == 0 and b == 0):
            break

    num = 0
    tmp_r = rgb_dec['r']
    tmp_g = rgb_dec['g']
    tmp_b = rgb_dec['b']
    while num < 5:
        num += 1
        tmp_r += 10
        tmp_g += 10
        tmp_b += 10
        r = tmp_r if tmp_r < 255 else 255
        g = tmp_g if tmp_g < 255 else 255
        b = tmp_b if tmp_b < 255 else 255
        nearly_colors.insert(0, {
            'r': '0' + hex(r)[2:3] if r < 16 else hex(r)[2:4],
            'g': '0' + hex(g)[2:3] if g < 16 else hex(g)[2:4],
            'b': '0' + hex(b)[2:3] if b < 16 else hex(b)[2:4]
        })
        if (r == 255 and g == 255 and b == 255):
            break

    colorcode_text = '#' + code
    colorcode_link = code
    return render_template(
        'color-detail-rgb-hex.html',
        colorcode_text=colorcode_text,
        colorcode_link=colorcode_link,
        rgb_hex=rgb_hex,
        rgb_dec=rgb_dec,
        rgb_percent=rgb_percent,
        cmyk=cmyk,
        hsl=hsl,
        hsv=hsv,
        nearly_colors=nearly_colors
    )


# @app.route('/rgba-hex/<colorcode>')
# def color_detail_rgba_hex(colorcode):
#     debug_str = ""
#     if re.match(r'^([0-9a-zA-Z]){8}$', colorcode):
#         debug_str = "Color Detail RGBa Hex %s" % (colorcode)
#     else:
#         debug_str = "Color Detail Error"
#     return debug_str
#
#
# @app.route('/rgb-dec/<colorcode>')
# def color_detail_rgb_dec(colorcode):
#     debug_str = ""
#     if re.match(r"^([\d]){1,3},([\d]){1,3},([\d]){1,3}$", colorcode):
#         debug_str = "Color Detail RGB Dec %s" % (colorcode)
#     else:
#         debug_str = "Color Detail Error"
#     return debug_str
#
#
# @app.route('/color/<name>')
# def color_detail(name):
#     debug_str = "Color Name = %s" % (name)
#     return debug_str


@app.route('/api/one-color-image/<code>')
def api_one_color_image(code):
    if not re.match(r'^([0-9a-zA-Z]){6}$', code):
        abort(404)
    code = code.lower()
    rgb_hex = ColorConvertUtil.rgbstr_to_rgbhex(code)
    rgb_dec = ColorConvertUtil.rgbhex_to_rgbdec(
        rgb_hex['r'], rgb_hex['g'], rgb_hex['b'])
    try:
        canvas = Image.new('RGB', (1, 1), (rgb_dec['r'],
            rgb_dec['g'], rgb_dec['b']))
        output = StringIO.StringIO()
        canvas.save(output, 'PNG')
        contents = output.getvalue()
        output.close()
        return Response(contents, mimetype='image/png')
    except Exception as e:
        print 'type:' + str(type(e))
        print 'args:' + str(e.args)
        print 'message:' + e.message
        print 'e: ' + str(e)
        error = e.message
    return error


@app.route('/assets/<path:path>')
def send_assets(path):
    return app.send_static_file('assets/' + path)


@app.route('/favicon.ico')
def send_favicon():
    return app.send_static_file('favicon.ico')


@app.route('/robots.txt')
def send_robots():
    return app.send_static_file('robots.txt')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


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


if __name__ == "__main__":
    app.run()
