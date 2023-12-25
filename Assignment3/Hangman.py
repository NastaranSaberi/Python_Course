import random 


words_bank = ["tree","book","green","rock","sheep","run","hello"]
user_mistakes = 0

good_chars = []
bad_chars = []

word_random = random.choice(words_bank)

while user_mistakes < 6 :

    unguessed_words = len(word_random)

    for i in range (len(word_random)) :

        if word_random[i] in good_chars :
            print(word_random[i] , end=" ")
            unguessed_words -= 1

        else :
            print("_ " , end="")

    if unguessed_words == 0:
            print ("You win 😍")
            break

    user = input("  Please write your guess :")
    user_char = user.lower()
    
    if len(user_char) == 1 :
        if user_char in word_random :
            good_chars.append(user_char)
            print("✅")

        else :
            user_mistakes += 1
            bad_chars.append(user_char)
            print("❌")

    else :
        print("msl adam vared kon")

if user_mistakes == 6 :
    print("Game Over ☠️")