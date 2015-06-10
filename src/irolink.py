from flask import Flask, request, redirect, render_template, abort
import re

app = Flask(__name__, static_url_path='')

@app.route('/')
def show_root():
    return render_template(
        'test.html',
        name = 'hoge'
    )

@app.route('/test/')
def show_test():
    return render_template('test.html')

@app.route('/rgb-hex/<code>')
def color_detail_rgb_hex(code):
    if not re.match(r'^([0-9a-zA-Z]){6}$', code):
        abort(404)
    if re.match(r'.*[A-Z].*', code):
        return redirect('/rgb-hex/' + code.lower())
    r_hex = code[0:2]
    g_hex = code[2:4]
    b_hex = code[4:6]
    r_dec = int(r_hex, 16)
    g_dec = int(g_hex, 16)
    b_dec = int(b_hex, 16)
    r_percent = float(r_dec) / 256 * 100
    g_percent = float(g_dec) / 256 * 100
    b_percent = float(b_dec) / 256 * 100

    # cmyk
    black = min(1 - r_dec / 255, min(1 - g_dec / 255, 1 - b_dec / 255))
    cmyk_c = (1 - (r_dec / 255) - black) / (1 - black)
    cmyk_m = (1 - (g_dec / 255) - black) / (1 - black)
    cmyk_y = (1 - (b_dec / 255) - black) / (1 - black)
    cmyk_k = black

    rgb_hex = {'r': r_hex, 'g': g_hex, 'b': b_hex}
    rgb_dec = {'r': r_dec, 'g': g_dec, 'b': b_dec}
    rgb_percent = {'r': r_percent, 'g': g_percent, 'b': b_percent}
    cmyk = {'c': cmyk_c, 'm': cmyk_m, 'y': cmyk_y, 'k': cmyk_k}

    colorcode_text = '#' + code
    colorcode_link = code
    #cvs_rgb_percent =
    return render_template(
        'color-detail-rgb-hex.html',
        colorcode_text = colorcode_text,
        colorcode_link = colorcode_link,
        rgb_hex_r = r_hex,
        rgb_hex_g = g_hex,
        rgb_hex_b = b_hex,
        rgb_dec_r = r_dec,
        rgb_dec_g = g_dec,
        rgb_dec_b = b_dec,
        rgb_percent_r = r_percent,
        rgb_percent_g = g_percent,
        rgb_percent_b = b_percent,
        rgb_hex = rgb_hex,
        rgb_dec = rgb_dec,
        rgb_percent = rgb_percent,
        cmyk = cmyk
    )

@app.route('/rgba-hex/<colorcode>')
def color_detail_rgba_hex(colorcode):
    debug_str = ""
    if re.match(r'^([0-9a-zA-Z]){8}$', colorcode) :
        debug_str = "Color Detail RGBa Hex %s" % (colorcode)
    else :
        debug_str = "Color Detail Error"
    return debug_str

@app.route('/rgb-dec/<colorcode>')
def color_detail_rgb_dec(colorcode):
    debug_str = ""
    if re.match(r"^([0-9]){1,3},([0-9]){1,3},([0-9]){1,3}$", colorcode) :
        debug_str = "Color Detail RGB Dec %s" % (colorcode)
    else :
        debug_str = "Color Detail Error"
    return debug_str

@app.route('/color/<colorcode>')
def color_detail(colorcode):
    debug_str = ""
    if re.match(r"^([0-9a-zA-Z]){6}$", colorcode) :
        debug_str = "Color Detail RGB Hex %s" % (colorcode)
    elif re.match(r"^([0-9a-zA-Z]){8}$", colorcode) :
        debug_str = "Color Detail RGBa Hex %s" % (colorcode)
    elif re.match(r"^([0-9]){1,3},([0-9]){1,3},([0-9]){1,3}$", colorcode) :
        debug_str = "Color Detail RGB Dec %s" % (colorcode)
    elif re.match(r"^([0-9]){1,3},([0-9]){1,3},([0-9]){1,3},([0-9]){1,3}$", colorcode) :
        debug_str = "Color Detail RGBa Dec %s" % (colorcode)
    elif re.match(r"^([0-9]){1,3},([0-9]){1,3},([0-9]){1,3},([0-9]){1,3}$", colorcode) :
        debug_str = "Color Detail RGBa Dec %s" % (colorcode)
    else :
        debug_str = "Color Detail Error"
    return debug_str

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

if __name__ == "__main__":
    app.run()
