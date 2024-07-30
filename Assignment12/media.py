import pytube

class Media:
    def __init__(self, name, director, imdb_score, url, duration, casts):
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts

    def show_info(self):
        print("Name:", self.name)
        print("Director:", self.director)
        print("IMDB Score:", self.imdb_score)
        print("URL:", self.url)
        print("Duration:", self.duration, "minutes")
        print("Casts:", end=" ")
        for actor in self.casts:
            print(actor.name, end=", ")
        print()
        
    def download(self):
        link = self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename='youtube.mp4')

        
    
