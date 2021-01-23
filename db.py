from pymongo import MongoClient
from secrets_ import MONGO_URI, DEVELOPER_KEY
from googleapiclient.discovery import build
import json
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def insert_show(username, title, link, client=MongoClient(MONGO_URI)):
    show = client.gallery.show
    show_info = {
        'username' : username,
        'title' : title,
        'link' : link
    }
    show.insert_one(show_info)
    return 'successfully inserted ' + str(show_info) + ' into db'

def get_thumbnail(link):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    # youtube.videos()
