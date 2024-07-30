from media import Media

class Clip(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, clip_type):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.clip_type = clip_type