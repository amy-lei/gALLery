from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from db import *

app = Flask(__name__)
client = MongoClient(MONGO_URI)

def jsonify_list(data, type_):
    """
    Returns data as a jsonifiable object by removing objectId, adds tag conglomerate
    """
    ans = [{ k:v for k,v in datum.items() if k != "_id" } for datum in data]
    if 'tags' in ans[0]:
        for post in ans:
            post['tag_conglomerate'] = ' '.join(post['tags']) + ' ' + type_
    return ans

@app.route('/')
def index():
    shows = client.gallery.show.find({}).sort('likes', -1)
    music = client.gallery.music.find({}).sort('likes', -1)
    hobby = client.gallery.hobby.find({}).sort('likes', -1)
    posts = {
        "shows": list(jsonify_list(shows, 'shows')),
        "music": list(jsonify_list(music, 'music')),
        "hobbies": list(jsonify_list(hobby, 'hobbies'))
    }
    return render_template('gallery.html', posts=posts)

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

@app.route('/api/hobby', methods=['POST', 'GET'])
def add_hobby():
    if request.method == 'POST':
        body = request.json
        username = body.get('username', '')
        title = body.get('title', '')
        quote = body.get('quote', '')
        tags = body.get('tags', None)
        print(insert_hobby(username, title, quote, tags))
        return jsonify(body), 201
    elif request.method == 'GET':
        return jsonify({'all_hobbies': []}), 200

@app.route('/api/add-like', methods=['POST', 'GET'])
def add_like():
    if request.method == 'POST':
        body = request.json
        # for now we assume all posts have a unique title
        title = body.get('title', '')
        print(insert_like(title))
        return jsonify(body), 201
    elif request.method == 'GET':
        return jsonify({'likes': []}), 200

@app.route('/api/remove-like', methods=['POST', 'GET'])
def subtract_like():
    if request.method == 'POST':
        body = request.json
        # for now we assume all posts have a unique title
        title = body.get('title', '')
        print(remove_like(title))
        return jsonify(body), 201
    elif request.method == 'GET':
        return jsonify({'likes': []}), 200

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
