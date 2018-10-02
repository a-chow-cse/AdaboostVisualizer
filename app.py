import os
from flask import Flask, render_template, request , redirect,url_for
from werkzeug.utils import secure_filename
import shutil

UPLOAD_FOLDER = "static/temp/"
ALLOWED_EXTENSIONS = set(['pdf','arff','csv'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    ans= '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
    print(ans)
    return ans


@app.route("/")
def index():
    if(os.path.exists(UPLOAD_FOLDER)):
        shutil.rmtree(UPLOAD_FOLDER)
    os.mkdir(UPLOAD_FOLDER)
    return render_template('index.html')


@app.route("/visualizer", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("WHat"+ request.url)
            return redirect(request.url_root)
        file=request.files['file']
        if file.filename == '':
            return redirect(request.url_root)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return render_template('DataUploadFirstView.html')
        else:
            return redirect(request.url_root)
    return ''


if __name__ == '__main__':
    TEMPLATES_AUTO_RELOAD = True
    app.run(debug = True)
