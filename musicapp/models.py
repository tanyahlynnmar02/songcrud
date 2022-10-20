class Artiste:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Song:
    def __init__(self, title, date_released, likes, artiste_id):
        self.title = title
        self.date_released = date_released
        self.likes = likes
        self.artiste_id = artiste_id


class Lyric:
    def __init__(self, content, song_id):
        self.content = content
        self.song_id = song_id

# Create your models here.
