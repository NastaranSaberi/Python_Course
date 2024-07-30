from database import Database
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from actor import Actor
from termcolor import colored
from pyfiglet import figlet_format

class MediaManager:
    def __init__(self, db_path):
        self.database = Database(db_path)
        self.media_list = []

    def load_data(self):
        self.media_list = self.database.read_database()
        print("Media data loaded.")

    def add_media(self):
        media_type = input("Please enter media type (Film/Series/Documentary/Clip): ")
        name = input("Please enter name: ")
        director = input("Please enter director: ")
        imdb_score = input("Please enter IMDB score: ")
        url = input("Please enter URL: ")
        duration = int(input("Please enter duration in minutes: "))
        casts_input = input("Please enter cast names (comma separated): ")
        casts = []
        for cast in casts_input.split(","):
            casts.append(Actor(cast.strip()))

        if media_type == "Film" or media_type == "film":
            genre = input("Please enter genre: ")
            media = Film(name, director, imdb_score, url, duration, casts, genre)
        elif media_type == "Series" or media_type == "series":
            episodes = int(input("Please enter number of episodes: "))
            media = Series(name, director, imdb_score, url, duration, casts, episodes)
        elif media_type == "Documentary" or media_type == "documentary":
            subject = input("Please enter subject: ")
            media = Documentary(name, director, imdb_score, url, duration, casts, subject)
        elif media_type == "Clip" or media_type == "clip":
            clip_type = input("Please enter clip type: ")
            media = Clip(name, director, imdb_score, url, duration, casts, clip_type)

        self.media_list.append(media)
        print(colored("New media was successfully added ✅ .", "green"))

    def remove_media(self):
        name = input("Please enter the name of the media to remove: ")
        for media in self.media_list:
            if media.name == name:
                self.media_list.remove(media)
                print(colored("Media " + name + " removed. ✅", "green"))
                break
            else:
                print(colored("This media does not exist. ❌", "red"))
                break

    def edit_media(self):
        name = input("Enter the name of the media to edit: ")
        for media in self.media_list:
            if media.name == name:
                media_type = input("Please enter media type (Film/Series/Documentary/Clip): ")
               
                media.name = input("Please enter new name " + "(" + media.name + "):")
                media.director = input("Please enter new director " + "(" + media.director + "):")
                media.imdb_score = input("Please enter new IMDB score " + "(" + media.imdb_score + "):")
                media.url = input("Please enter new url " + "(" + media.url + "):")
                media.duration = int(input("Please enter new duration " + "(" + media.duration + "):"))
                casts_input = input("Please enter new cast names (comma separated): ")
                media.casts = [Actor(cast.strip()) for cast in casts_input.split(",")]
    
                if media_type == "Film" or media_type == "film":
                    media.genre = input("Please enter new genre " + "(" + media.genre + "):")
                elif media_type == "Series" or media_type == "series":
                    media.episodes = int(input("Please enter new number of episodes " + "(" + media.episodes + "):"))
                elif media_type == "Documentary" or media_type == "documentary":
                    media.subject = input("Please enter new subject " + "(" + media.subject + "):")
                elif media_type == "Clip" or media_type == "clip":
                    media.clip_type = input("Please enter new clip type " + "(" + media.clip_type + "):")
                
                print(colored("Media " + name + " edited. ✅", "green"))
                break
            else:
                print(colored("This media does not exist. ❌", "red"))
                break

    def show_all_media(self):
        if not self.media_list:
            print(colored("No media in the database.", "red"))

        for media in self.media_list:
            media.show_info()
            if isinstance(media, Film):
                print("Genre:", media.genre)
            elif isinstance(media, Series):
                print("Episodes:", media.episodes)
            elif isinstance(media, Documentary):
                print("Subject:", media.subject)
            elif isinstance(media, Clip):
                print("Clip Type:", media.clip_type)

            print("\n")
            
    def save_data(self):
        self.database.write_database(self.media_list)
        print("Media data saved.")

    def download_media(self):
        name = input("Enter the name of the media to download: ").strip().lower()
        for media in self.media_list:
            if media.name == name:
                media.download()
                print(colored("downloaded successfully. ✅", "green"))
            else:
                print(colored("This media does not exist. ❌", "red"))

            print("\n")
            
    def search_media_by_duration(self):
        a = int(input("Please enter minimum duration in minutes: "))
        b = int(input("Please enter maximum duration in minutes: "))

        found_media = False
        for media in self.media_list:
            if a < media.duration and media.duration< b:
                found_media = True
                print("Name: " + media.name)

        if not found_media:
            print(colored("No media found within the specified duration range.", "red"))



def show_menu():
    print("\n")
    print("1- Add New Media")
    print("2- Remove Media")
    print("3- Edit Media")
    print("4- Show All Media")
    print("5- Download Media")
    print("6- Search Media by Duration")
    print("7- Exit")

def management(media_manager):
    print(colored(figlet_format("Video Media Management", font="slant"), color="magenta"))

    while True:
        show_menu()
        choice = input('\nPlease choose a number: ')

        if choice == "1":
            media_manager.add_media()
        elif choice == "2":
            media_manager.remove_media()
        elif choice == "3":
            media_manager.edit_media()
        elif choice == "4":
            media_manager.show_all_media()
        elif choice == "5":
            media_manager.download_media()
        elif choice == "6":
            media_manager.search_media_by_duration()
        elif choice == "7":
            media_manager.database.write_database(media_manager.media_list)
            print("Data saved. Exiting...")
            break
        else:
            print(colored("Invalid choice. Please try again.", "red"))


media_manager = MediaManager("database.txt")
media_manager.load_data()
management(media_manager)