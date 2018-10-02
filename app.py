from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/visualizer")
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


if __name__ == '__main__':
    TEMPLATES_AUTO_RELOAD = True
    app.run(debug = True)
