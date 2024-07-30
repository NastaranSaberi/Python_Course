from actor import Actor
from series import Series
from documentary import Documentary
from clip import Clip
from film import Film

class Database:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_database(self):
        media_list = []
        with open(self.file_path, 'r') as file:
            for line in file:
                media_data = line.strip().split(',')
                media_type = media_data[0]
                name = media_data[1]
                director = media_data[2]
                imdb_score = media_data[3]
                url = media_data[4]
                duration = int(media_data[5])
                casts = [Actor(cast.strip()) for cast in media_data[6].split('|')]

                if media_type == 'Film':
                    genre = media_data[7]
                    media = Film(name, director, imdb_score, url, duration, casts, genre)
                elif media_type == 'Series':
                    episodes = int(media_data[7])
                    media = Series(name, director, imdb_score, url, duration, casts, episodes)
                elif media_type == 'Documentary':
                    subject = media_data[7]
                    media = Documentary(name, director, imdb_score, url, duration, casts, subject)
                elif media_type == 'Clip':
                    clip_type = media_data[7]
                    media = Clip(name, director, imdb_score, url, duration, casts, clip_type)
                
                media_list.append(media)
        return media_list

    def write_database(self, media_list):
        with open(self.file_path, 'w') as file:
            for media in media_list:
                if isinstance(media, Film):
                    media_type = 'Film'
                    extra_info = media.genre
                elif isinstance(media, Series):
                    media_type = 'Series'
                    extra_info = media.episodes
                elif isinstance(media, Documentary):
                    media_type = 'Documentary'
                    extra_info = media.subject
                elif isinstance(media, Clip):
                    media_type = 'Clip'
                    extra_info = media.clip_type

                file.write(f"{media_type},{media.name},{media.director},{media.imdb_score},{media.url},{media.duration},{'|'.join([actor.name for actor in media.casts])},{extra_info}\n")