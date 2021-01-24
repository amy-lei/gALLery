from pymongo import MongoClient
from secrets_ import MONGO_URI, DEVELOPER_KEY, CLIENT_ID, CLIENT_SECRET
from googleapiclient.discovery import build
import pprint
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET))
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def insert_show(username, title, link, tags, client=MongoClient(MONGO_URI)):
    tags = [item.strip().replace(' ', '-') for item in tags.split(',')]
    show = client.gallery.show
    show_info = {
        'username' : username,
        'title' : title,
        'link' : link,
        'tags' : tags
    }
    show.insert_one(show_info)
    return 'successfully inserted ' + str(show_info) + ' into db'

def insert_music(username, vid_link, tags=None, client=MongoClient(MONGO_URI)):
    if tags is None:
        thumbnail, title, tags = get_vid_info(get_vid_id(vid_link))
    else:
        tags = tags.split(',')
        thumbnail, title = get_track_info(vid_link)
    tags = [item.strip().replace(' ', '-') for item in tags]
    music = client.gallery.music
    music_info = {
        'username' : username,
        'title' : title,
        'link' : thumbnail,
        'tags' : tags
    }
    music.insert_one(music_info)
    return 'successfully inserted ' + str(music_info) + ' into db'

def get_vid_info(vid_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    request = youtube.videos().list(part='snippet', id=vid_id)
    resp = request.execute()
    snippet = resp['items'][0]['snippet']
    # pprint.pprint(snippet)
    return snippet['thumbnails']['maxres']['url'], snippet['title'], snippet['tags']

def get_vid_id(vid_link):
    parts = vid_link.split('?')
    if len(parts) == 1:
        return parts[0].split('/')[-1]
    for request in parts[-1].split('&'):
        if request[:2] == 'v=':
            return request[2:]

def get_track_info(spotify_id):
    t = sp.track(spotify_id)
    return t['album']['images'][0]['url'], t['album']['name']

