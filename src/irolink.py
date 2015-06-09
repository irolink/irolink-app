from flask import Flask, request, redirect, render_template, url_for
#from jinja2 import FileSystemLoader
import re

app = Flask(__name__, static_url_path='')
#app.jinja_loader = FileSystemLoader('views')

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

@app.route("/rgb-hex/<colorcode>")
def color_detail_rgb_hex(colorcode):
    debug_str = ""
    if re.match(r"^([0-9a-zA-Z]){6}$", colorcode) :
        debug_str = "Color Detail RGB Hex %s" % (colorcode)
    else :
        return "Color Detail Error"
    return render_template(
        "color-detail-rgb-hex.html",
        colorcode = colorcode,
        display_colorcode = colorcode,
        raw_colorcode = colorcode
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
