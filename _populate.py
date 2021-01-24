from pymongo import MongoClient
from db import insert_music, insert_hobby
from secrets_ import MONGO_URI

SHOW_DATA = [
    {
        "username": "bean-man",
        "title": "JJK",
        "link": "https://cdn.myanimelist.net/images/anime/1171/109222l.jpg",
        "likes": 0,
        "tags" : ["action", "supernatural", "shounen"],
    },
    {
        "username": "staries",
        "title": "Hannibal",
        "link": "https://i.pinimg.com/originals/ff/2b/25/ff2b255df0e94d2cdeae6829879e0c75.jpg",
        "likes": 1,
        "tags" : ["psychological-thriller", "thriller", "horror"]
    },
    {
        "username": "hedgehog",
        "title": "NARUTO",
        "link": "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UY1200_CR93,0,630,1200_AL_.jpg",
        "likes": 3,
        "tags" : ["action", "adventure", "shounen"]
    },
    {
        "username": "art-fan100",
        "title": "Mob Psycho 100",
        "link": "https://fesapusewebsite.blob.core.windows.net/fathom/mob-psycho-30c4ada3d5240fa55be8dd49aec0ed2e.png",
        "likes": 1,
        "tags" : ["action", "comedy", "supernatural"]
    },
    {
        "username": "tardis",
        "title": "Doctor Who",
        "link": "https://m.media-amazon.com/images/M/MV5BZWJhYjFmZDEtNTVlYy00NGExLWJhZWItNTAxODY5YTc3MDFmXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg",
        "likes": 0,
        "tags" : ["adventure", "sci-fi", "drama"]
    },
    {
        "username": "cool-dinosaur",
        "title": "Squarepants",
        "link": "https://nick.mtvnimages.com/uri/mgid:arc:content:nick.com:9cd2df6e-63c7-43da-8bde-8d77af9169c7?quality=0.7",
        "likes": 2,
        "tags" : ["comedy", "slapstick", "surreal-humor"]
    },
    {
        "username": "sara",
        "title": "Hunter x Hunter",
        "link": "https://cconnect.s3.amazonaws.com/wp-content/uploads/2020/03/Funko-Pop-Hunter-x-Hunter-Figures-thumb-600.jpg",
        "likes": 0,
        "tags" : ["fantasy", "friendship", "adventure", "shounen"]
    },
    {
        "username": "carl",
        "title": "She-ra And The Princesses of Power",
        "link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG7wmAnLk2bxARcLvyu57X4jS5OvKtroNqYzsOtBLpmkquQuBc",
        "likes": 1,
        "tags" : ["drama", "adventure", "action"]
    },
    {
        "username": "pink-horse",
        "title": "The Umbrella Academy",
        "link": "https://m.media-amazon.com/images/M/MV5BNTFhOTk1NTgtYWM1ZS00NWI1LTgzYzAtYmE5MjZiMDE0NzlhXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg?w=144",
        "likes": 1,
        "tags" : ["drama", "action"]
    },
    {
        "username": "yellow-hamster",
        "title": "Sailor Moon",
        "link": "https://m.media-amazon.com/images/M/MV5BZDI4MmMyMjgtNjgxMi00NDU4LTliOGUtMzgxNDE3ZmIxM2NkXkEyXkFqcGdeQXVyNjk1Njg5NTA@._V1_UY1200_CR73,0,630,1200_AL_.jpg",
        "likes": 2,
        "tags" : ["magical-girl", "superhero"]
    },
    {
        "username": "yellow-hamster",
        "title": "Puella Magi Madoka Magica",
        "link": "https://m.media-amazon.com/images/M/MV5BZGYyZDlhY2YtMmYwNC00YjM3LWEwZDEtMTRhOWI5NDViM2NlXkEyXkFqcGdeQXVyMjk0NTE0NA@@._V1_.jpg",
        "likes": 4,
        "tags" : ["magical-girl", "horror", "psychological-thriller"]
    },
    {
        "username": "yellow-hat-dude",
        "title": "Curious George",
        "link": "https://static1.colliderimages.com/wordpress/wp-content/uploads/2016/08/curious-george-image-600x338.jpg?q=50&fit=crop&w=600&dpr=1.5",
        "likes": 0,
        "tags" : ["monkey", "educational", "friendship"]
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
    insert_music('musical-tricycle', 'https://open.spotify.com/track/2cYALQZNXmuFGp2ecgpKMa', 'art pop, avant pop')
    insert_music('small-dinosaur', 'https://youtu.be/tdVAqxNLXiw')
    insert_music('tiny-bot', 'https://youtu.be/8UVNT4wvIGY')
    insert_music('classic-lover','https://open.spotify.com/track/3ThCzJcgLmOjR1smnurVKd', 'classical, relaxing')
    insert_music('classic-lover','https://open.spotify.com/track/7zHd9LxIZB8WKosSWN9Umj', 'minimalist, classical, relaxing')
    insert_music('','https://open.spotify.com/track/1UvaZaHkh3D9AkmBrrnbFg', 'classical, mozart')
    insert_music('average-parrot','https://youtu.be/23xSJ19YW1I')
    insert_music('','https://open.spotify.com/track/3ZCTVFBt2Brf31RLEnCkWJ', 'soft, alternative')
    insert_music('pink-rabbit','https://youtu.be/Hy0bdQpEGPI')
    insert_music('','https://youtu.be/ziUgyu71GAQ')
    print('inserted musics')

    r = client.gallery.hobby.delete_many({})
    print(f'cleared {r.deleted_count} hobby')

    insert_hobby('pidge', 'Birdwatching', 'I saw a robin the other day', 'birds, relaxing')
    insert_hobby('knitten', 'Knitting', 'I knit my kitten a sweater', 'arts, crafts, relaxing')
