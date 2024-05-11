import telebot
from telebot import types
import random
from khayyam import JalaliDatetime
from gtts import gTTS
import qrcode

bot =  telebot.TeleBot ("7055392490:AAHjJ_vDUb0wS8TtgFxN5a9XFy5YYux2xpI",parse_mode=None)


my_keyboard= types.ReplyKeyboardMarkup (row_width = 3 , resize_keyboard=True)
key1= types.KeyboardButton("Start 😊")
key2= types.KeyboardButton("Game 🎲")
key3= types.KeyboardButton("Age 🗓️")
key4= types.KeyboardButton("Voice 🔈")
key5= types.KeyboardButton("Max")
key6= types.KeyboardButton("Argmax")
key7= types.KeyboardButton("Qrcode")
key8= types.KeyboardButton("Help 💁🏻‍♀️")

my_keyboard.add(key1,key2,key3,key4,key5,key6,key7,key8)



########## Start command ##########
@bot.message_handler(commands=['start'])
def start(message) :
    user_name = message.from_user.first_name
    bot.reply_to(message , "Hello dear " + user_name + " 🤗" , reply_markup=my_keyboard)


########## Menu ##########
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "Start 😊" or message.text == "/start":
        start(message)
    elif message.text == "Game 🎲" or message.text == "/game" or message.text == "New Game": 
        start_game(message)
    elif message.text == "Age 🗓️" or message.text == "/age":
        age(message)
    elif message.text == "Voice 🔈" or message.text == "/voice":
        voice_sentence(message)
    elif message.text == "Max" or message.text == "/max":
        max_message(message)
    elif message.text == "Argmax" or message.text == "/argmax":
        argmax_message(message)
    elif message.text == "Qrcode" or message.text == "/qrcode":
        qrcode_message(message)
    elif message.text == "Help 💁🏻‍♀️" or message.text == "/help":
        help(message)


########## Game command ##########
@bot.message_handler(commands=['game'])
def start_game(message):
    global target_number

    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    new_game_button = types.KeyboardButton('New Game')
    markup.add(new_game_button)

    target_number = random.randint(1, 10)
    bot.send_message(message.chat.id, "Guess a number between 1 and 10." , reply_markup=markup)
    bot.register_next_step_handler(message, guess_number)

def guess_number(message):
    guess = int(message.text)
    if guess < target_number:
        bot.reply_to(message, "Go higher ⬆️.")
        bot.register_next_step_handler(message, guess_number)
    elif guess > target_number:
        bot.reply_to(message, "Go lower ⬇️.")
        bot.register_next_step_handler(message, guess_number)
    elif guess == target_number:
        bot.reply_to(message, "You win 🏆.")

@bot.message_handler(func=lambda message: message.text == 'New Game')
def new_game(message):
    start_game(message)


########## Age command ##########  
@bot.message_handler(commands=['age'])
def age(message):
    bot.send_message(message.chat.id , "Please enter your date of birth in Solar Hijri (year/month/day).")
    bot.register_next_step_handler(message, age_calculation)

def age_calculation(message) :
    birthday = list(map(int, message.text.split('/')))
    age = JalaliDatetime.now().year - birthday[0]
    bot.reply_to(message, f"You are {age} years old.")


########## Voice command ##########
@bot.message_handler(commands=['voice'])
def voice_sentence(message) :
    bot.send_message(message.chat.id , "Please enter the sentence that you want to convert to voice .")
    bot.register_next_step_handler(message, voice)

def voice(message) :
    tts = gTTS(text=message.text, lang='en')
    tts.save("voice_message.mp3")
    voice = open("voice_message.mp3", "rb")
    bot.send_voice(message.chat.id, voice)


########## Max command ##########
@bot.message_handler(commands=['max'])
def max_message(message):
    bot.send_message(message.chat.id, "Please enter a list of numbers separated by commas (1,11,22,33,2).")
    bot.register_next_step_handler(message, calculate_max)

def calculate_max(message):
    num_list = message.text.split(",")
    max_number = max(num_list)
    bot.reply_to(message, f"The maximum value is {max_number} ." )


########## Argmax command ##########
@bot.message_handler(commands=['argmax'])
def argmax_message(message):
    bot.send_message(message.chat.id, "Please enter a list of numbers separated by commas (1,11,22,33,2).")
    bot.register_next_step_handler(message, calculate_argmax)

def calculate_argmax(message):
    num_list = message.text.split(",")
    max_index = num_list.index(max(num_list))
    bot.reply_to(message, f"The index of the maximum value is: {max_index}")


########## Qrcode command ##########
@bot.message_handler(commands=['qrcode'])
def qrcode_message(message):
    bot.send_message(message.chat.id, "Please enter the text for generating QR code.")
    bot.register_next_step_handler(message, create_qrcode)

def create_qrcode(message):
    qr = qrcode.make(message.text)
    qr.save("qrcode.png")
    qr_file = open("qrcode.png", "rb")
    bot.send_photo(message.chat.id, qr_file)


########## help command ##########
@bot.message_handler(commands=['help'])
def help(message):
    help_text = """
    /start: Start
    /game: Number Guessing Game
    /age: Calculate Age
    /voice: Send Sentence as Voice
    /max: Maximum Value
    /argmax: Index of Maximum Value
    /qrcode: Generate QR code
    /help: Help
    """
    bot.reply_to(message, help_text)


bot.infinity_polling()