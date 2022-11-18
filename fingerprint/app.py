from flask import Flask, render_template, url_for, request
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)