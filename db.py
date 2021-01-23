from pymongo import MongoClient
from secrets_ import MONGO_URI

def insert_show(username, title, link, client=MongoClient(MONGO_URI)):
    show = client.gallery.show
    show_info = {
        'username' : username,
        'title' : title,
        'link' : link
    }
    show.insert_one(show_info)
    return 'successfully inserted ' + str(show_info) + ' into db'
