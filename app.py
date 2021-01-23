from flask import Flask, render_template, request, redirect, url_for
from db import *
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/add-show', methods=['POST', 'GET'])
def add_show():
    if request.method == 'POST':
        u = request.form['username']
        t = request.form['title']
        l = request.form['link']
        print(insert_show(u,t,l))
        return redirect(url_for('index'))
    return render_template('add_show.html')

@app.route('/clear-shows')
def clear_shows():
    print('clearing shows...')
    return 'cleared shows.'
