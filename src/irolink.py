from flask import Flask, request, redirect, render_template, url_for
#from jinja2 import FileSystemLoader
import re

app = Flask(__name__, static_url_path='')
#app.jinja_loader = FileSystemLoader('views')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@app.route('/assets/<path:path>')
def send_assets(path):
    return app.send_static_file('assets/' + path)

@app.route('/favicon.ico')
def send_favicon():
    return app.send_static_file('favicon.ico')

@app.route('/robots.txt')
def send_robots():
    return app.send_static_file('robots.txt')

@app.route('/')
def root():
    return render_template(
        "test.html",
        name = "hoge"
    )

@app.route('/test/')
def show_test():
    return render_template("test.html")

@app.route('/rgb-hex/<code>')
def color_detail_rgb_hex(code):
    if not re.match(r"^([0-9a-zA-Z]){6}$", code):
        return page_not_found()
    #if re.match(r'([A-Z])', code):
    #    return redirect('/rgb-hex/' + code.lower())
    r_hex = code[0:2]
    g_hex = code[2:4]
    b_hex = code[4:6]
    r_dec = int(r_hex, 16)
    g_dec = int(g_hex, 16)
    b_dec = int(b_hex, 16)
    colorcode_text = '#' + code
    colorcode_link = code
    cvs_rgbdec_def = '%s, %s, %s' % (r_hex, g_hex, b_hex)
    cvs_rgbdec_css = 'rgb(%s, %s, %s)' % (r_dec, g_dec, b_dec)
    cvs_rgbhex_def = '#' + code
    cvs_rgbhex_css = '#' + code
    return render_template(
        'color-detail-rgb-hex.html',
        colorcode_text = colorcode_text,
        colorcode_link = colorcode_link,
        cvs_rgbdec_def = cvs_rgbdec_def,
        cvs_rgbdec_css = cvs_rgbdec_css,
        cvs_rgbhex_def = cvs_rgbhex_def,
        cvs_rgbhex_css = cvs_rgbhex_css
    )

@app.route("/rgba-hex/<colorcode>")
def color_detail_rgba_hex(colorcode):
    debug_str = ""
    if re.match(r"^([0-9a-zA-Z]){8}$", colorcode) :
        debug_str = "Color Detail RGBa Hex %s" % (colorcode)
    else :
        debug_str = "Color Detail Error"
    return debug_str

@app.route("/rgb-dec/<colorcode>")
def color_detail_rgb_dec(colorcode):
    debug_str = ""
    if re.match(r"^([0-9]){1,3},([0-9]){1,3},([0-9]){1,3}$", colorcode) :
        debug_str = "Color Detail RGB Dec %s" % (colorcode)
    else :
        debug_str = "Color Detail Error"
    return debug_str

@app.route("/color/<colorcode>")
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

if __name__ == "__main__":
    app.run()
