from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/add-show')
def add_show():
    return render_template('add_show.html')
