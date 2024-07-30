from media import Media

class Documentary(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, subject):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.subject = subject
