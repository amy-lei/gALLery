from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/add-show', methods=['POST', 'GET'])
def add_show():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['title'])
        print(request.form['link'])
    return render_template('add_show.html')
