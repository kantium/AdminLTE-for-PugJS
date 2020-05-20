from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__, static_url_path='')

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.debug = True


@app.route('/')
@app.route('/<name>')
def hello(name="index"):
    content= {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'Friends': ['Bob', 'Alice'], 'Male':False, 'html':'<b>test</b>'}
    return render_template(name + '.pug', content=content)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


# To replace by nxing static folder !
@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    app.run(debug=True)

