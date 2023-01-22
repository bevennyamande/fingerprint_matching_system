import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from fingerprint_matching import algorithm

app = Flask(__name__)
app.secret_key = os.urandom(34)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'temp')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    file = request.files['filename']
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
## you call your algorithm here 
        # algorithm(file)


        # file has been uploaded now you can call your algorithm here and
        #  after processing return the user to a desirable page

        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)