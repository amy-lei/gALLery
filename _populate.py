from pymongo import MongoClient
from secrets_ import MONGO_URI

DATA = [
    {
        "username": "bean-man",
        "title": "JJK",
        "link": "https://cdn.myanimelist.net/images/anime/1171/109222l.jpg",
    },
    {
        "username": "hedgehog",
        "title": "NARUTO",
        "link": "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY1200_CR93,0,630,1200_AL_.jpg",
    },
    {
        "username": "cool-dinosaur",
        "title": "Squarepants",
        "link": "https://nick.mtvnimages.com/uri/mgid:arc:content:nick.com:9cd2df6e-63c7-43da-8bde-8d77af9169c7?quality=0.7",
    },
]

if __name__ == '__main__':
    client = MongoClient(MONGO_URI)
    show = client.gallery.show
    
    # First delete existing shows
    r = client.gallery.show.delete_many({})
    print(f'cleared {r.deleted_count} shows')

    # Then repopulate
    r = client.gallery.show.insert_many(DATA)
    print(f'successfully inserted {len(r.inserted_ids)} shows')
