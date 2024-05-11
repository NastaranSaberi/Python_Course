# Assignment 9 :

This Python script utilizes the Telebot library to create a Telegram bot with various functionalities. Here's a rundown of the key features :

**Initialization:** The script initializes the Telegram bot using your API token.

**Custom Keyboard:** It defines a custom keyboard with options like Start, Game, Age, Voice, Max, Argmax, Qrcode, and Help.

**Start Command:** The **"/start"** command greets the user by their first name and displays the custom keyboard.

**Game Command:** The **"/game"** command initiates a number guessing game. The bot randomly selects a number between 1 and 10, and the user attempts to guess it. Feedback is provided based on whether the guess is higher or lower than the target number.

**Age Command:** The **"/age"** command calculates the user's age based on their input date of birth in Solar Hijri format.

**Voice Command:** The **"/voice"** command converts the user's input sentence into speech using the Google Text-to-Speech (gTTS) library and sends it as a voice message.

**Max Command:** The **"/max"** command calculates the maximum value from a list of numbers provided by the user.

**Argmax Command**: The **"/argmax"** command finds the index of the maximum value from a list of numbers provided by the user.

**Qrcode Command:** The **"/qrcode"** command generates a QR code from the user's input text and sends it as a photo.

**Help Command:** The **"/help"** command displays a help message listing all available commands and their descriptions.




---



The libraries used in this script are:

**telebot:** Used for creating and managing the Telegram bot.

**types from telebot:** Utilized for various types of buttons and messages.

**random:** Employed for generating random numbers in the number guessing game.

**khayyam:** Utilized for calculating age based on Solar Hijri birthdates.

**gtts:** Used for converting text to speech in the Voice section.

**qrcode:** Utilized for generating QR codes.

These libraries provide various features and capabilities for performing different tasks within this Telegram bot.
