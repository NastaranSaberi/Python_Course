from media import Media

class Series(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, episodes):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.episodes = episodes

