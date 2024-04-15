from termcolor import colored
from gtts import gTTS
import os

def read_file():
    global words_bank
    f = open("translate.txt" , "r")  
    temp = f.read().split("\n")

    words_bank = []
    for i in range(0, len(temp), 2):
        my_dict = {"en": temp[i], "fa": temp[i+1]}
        words_bank.append(my_dict)

    f.close()


def translate_english_to_persian():
    user_text = input("enter your english text:")
    user_words = user_text.split(" ")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output = output + word["fa"] + " "
                break
        else:
            output = output + user_word + " "

    print(colored(output , color="green"))
    
    #Voice
    tts = gTTS(text = output , lang='ur')
    tts.save("output.mp3")
    os.system("afplay output.mp3")


def translate_persian_to_english():
    user_text = input("enter your persian text:")
    user_words = user_text.split(" ")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                output = output + word["en"] + " "
                break
        else:
            output = output + user_word + " " 

    print(colored(output , color="green"))

    #Voice
    tts = gTTS(text = output , lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")


def add_new_word():
    en_word = input("Please enter english word:")
    fa_word = input("Please enter persian word:")
    file = open("translate.txt", "a")

    for word in words_bank:
        if en_word == word["en"] or fa_word == word["fa"] :
            print(colored("This word exists." , color="red"))
            break

    else:
            
        file.write("\n" + en_word + "\n" + fa_word)
        print(colored("\nAdd successfully." , color="green"))
            
    file.close()


def show_menu():
    print("Welcome to my translate")
    print("1_Translate english to persian ")
    print("2_Translate persian to english ")
    print("3_Add new word to database ")
    print("4_Exit")


read_file()

while True:
    show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        translate_persian_to_english()
    elif choice == 3:
        add_new_word()
    elif choice == 4: 
        exit(0)
