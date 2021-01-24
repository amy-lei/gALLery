from pymongo import MongoClient
from db import insert_music
from secrets_ import MONGO_URI

SHOW_DATA = [
    {
        "username": "bean-man",
        "title": "JJK",
        "link": "https://cdn.myanimelist.net/images/anime/1171/109222l.jpg",
        "tags" : ["action", "supernatural", "shounen"]
    },
    {
        "username": "staries",
        "title": "Hannibal",
        "link": "https://i.pinimg.com/originals/ff/2b/25/ff2b255df0e94d2cdeae6829879e0c75.jpg",
        "tags" : ["psychological thriller", "thriller", "horror"]
    },
    {
        "username": "hedgehog",
        "title": "NARUTO",
        "link": "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY1200_CR93,0,630,1200_AL_.jpg",
        "tags" : ["action", "adventure", "shounen"]
    },
    {
        "username": "tardis",
        "title": "Doctor Who",
        "link": "https://m.media-amazon.com/images/M/MV5BZWJhYjFmZDEtNTVlYy00NGExLWJhZWItNTAxODY5YTc3MDFmXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg",
        "tags" : ["adventure", "sci-fi", "drama"]
    },
    {
        "username": "cool-dinosaur",
        "title": "Squarepants",
        "link": "https://nick.mtvnimages.com/uri/mgid:arc:content:nick.com:9cd2df6e-63c7-43da-8bde-8d77af9169c7?quality=0.7",
        "tags" : ["comedy", "slapstick", "surreal humor"]
    },
    {
        "username": "sara",
        "title": "Hunter x Hunter",
        "link": "https://cconnect.s3.amazonaws.com/wp-content/uploads/2020/03/Funko-Pop-Hunter-x-Hunter-Figures-thumb-600.jpg",
        "tags" : ["fantasy", "friendship", "adventure"]
    },
    {
        "username": "carl",
        "title": "She-ra And The Princesses of Power",
        "link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG7wmAnLk2bxARcLvyu57X4jS5OvKtroNqYzsOtBLpmkquQuBc",
        "tags" : ["drama", "adventure", "action"]
    },
]

if __name__ == '__main__':
    client = MongoClient(MONGO_URI)
    show = client.gallery.show
    
    # First delete existing shows
    r = client.gallery.show.delete_many({})
    print(f'cleared {r.deleted_count} shows')

    # Then repopulate
    r = client.gallery.show.insert_many(SHOW_DATA)
    print(f'successfully inserted {len(r.inserted_ids)} shows')

    # delete existing music
    r = client.gallery.music.delete_many({})
    print(f'cleared {r.deleted_count} music')

    # repopulate
    insert_music('musical_tricycle', 'https://open.spotify.com/track/2cYALQZNXmuFGp2ecgpKMa', 'art pop, avant pop')
    insert_music('small_dinosaur', 'https://youtu.be/tdVAqxNLXiw')
    insert_music('tiny_bot', 'https://youtu.be/8UVNT4wvIGY')
    insert_music('caracal', 'https://open.spotify.com/track/0NsMgzCzCuedQKqIWSOF34', 'rock, soft')
    insert_music('average_parrot','https://youtu.be/23xSJ19YW1I')
