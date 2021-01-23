from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from db import *

app = Flask(__name__)
client = MongoClient(MONGO_URI)

@app.route('/')
def index():
    shows = client.gallery.show.find({})
    music = client.gallery.music.find({})
    DATA = {
        "shows": list(shows),
        "music": list(music)
    }
    return render_template('gallery.html', posts=DATA)

@app.route('/api/shows', methods=['POST', 'GET'])
def add_show():
    if request.method == 'POST':
        body = request.json
        username = body.get('username', '')
        title = body.get('title', '')
        link = body.get('link', '')
        tags = body.get('tags', '')
        print(insert_show(username, title, link, tags))
        return jsonify(body), 201
    elif request.method == 'GET':
        return jsonify({'all_shows': []}), 200

@app.route('/api/music', methods=['POST', 'GET'])
def add_music():
    if request.method == 'POST':
        body = request.json
        username = body.get('username', '')
        link = body.get('link', '')
        tags = body.get('tags', None)
        print(insert_music(username, link, tags))
        return jsonify(body), 201
    elif request.method == 'GET':
        return jsonify({'all_music': []}), 200

@app.route('/clear-shows')
def clear_shows():
    print('clearing shows...')
    r = client.gallery.show.delete_many({})
    return 'cleared ' + str(r.deleted_count) + ' shows.'

@app.route('/clear-moviess')
def clear_movies():
    print('clearing music ...')
    r = client.gallery.music.delete_many({})
    return 'cleared ' + str(r.deleted_count) + ' music.'
