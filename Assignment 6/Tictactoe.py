import random
import time
from termcolor import colored
import pyfiglet 

titel = pyfiglet.figlet_format("Tic tac toe ",font = "ogre")
time_has_passed = time.time()

print(titel)
print("Which do you want?")
print("1_ Player1 & Player2\n2_ Player & computer")

selection = input(" 1 or 2 : ")

def show_game_board():
    for i in range(3):
        for j in range(3):
            if game[i][j] == 'X':
                print(colored(game[i][j],"red"),end=' ')
            elif game[i][j] == 'O':
                print(colored(game[i][j],"blue"),end=' ')
            else:
                print(game[i][j],end=' ')
        print('\n',end='')

def check():
    if game [0][0]== 'x'and game [0][1]== 'x'and game [0][2]== 'x':
        print('player 1 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [0][0]== 'x'and game [1][0]== 'x'and game [2][0]== 'x':
        print('player 1 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [0][0]== 'x'and game [1][1]== 'x'and game [2][2]== 'x':
        print('player 1 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [1][0]== 'x'and game [1][1]== 'x'and game [1][2]== 'x':
        print('player 1 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [2][0]== 'x'and game [2][1]== 'x'and game [2][2]== 'x':
        print('player 1 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [2][0]== 'x'and game [1][1]== 'x'and game [0][2]== 'x':
        print('player 1 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [1][1]== 'x'and game [0][1]== 'x'and game [2][1]== 'x':
        print('player 1 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [0][2]== 'x'and game [1][2]== 'x'and game [2][2]== 'x':
        print('player 1 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [0][0]== 'o'and game [0][1]== 'o'and game [0][2]== 'o':
        print('player 2 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [0][0]== 'o'and game [1][0]== 'o'and game [2][0]== 'o':
        print('player 2 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [0][0]== 'o'and game [1][1]== 'o'and game [2][2]== 'o':
        print('player 2 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [1][0]== 'o'and game [1][1]== 'o'and game [1][2]== 'o':
        print('player 2 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [2][0]== 'o'and game [2][1]== 'o'and game [2][2]== 'o':
        print('player 2 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [2][0]== 'o'and game [1][1]== ''and game [0][2]== '':
        print('player 2 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [1][1]== 'o'and game [0][1]== 'o'and game [2][1]== 'o':
        print('player 2 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif game [0][2]== 'o'and game [1][2]== 'o'and game [2][2]== 'o':
        print('player 2 wins')
        print('Time spent playing :' , time_has_passed)
        exit()
    elif ((game[0][0]=="x" or game[0][0]=="o") and (game[0][1]=="x" or game[0][1]=="o")and
    (game[0][2]=="x" or game[0][2]=="o" ) and (game[1][0]=="x" or game[1][0]=="o") and 
    (game[1][1]=="x" or game[1][1]=="o") and (game[1][2]=="x" or game[1][2]=="o") and 
    (game[2][0]=="x" or game[2][0]=="o") and (game[2][1]=="x" or game[2][1]=="o") and 
    (game[2][2]=="x" or game[2][2]=="o")):
        print('Drow')
    
    
game = [['_','_','_'],
       ['_','_','_'],
       ['_','_','_']]

show_game_board()

if selection=="1":
    while True:
        # Player 1
        print('player number 1')
        while True:
            row = int(input('Please enter the row number :'))
            col = int(input('Please enter the column number :'))
            if 0<= row <= 2 and 0<= col <=2:
                if game[row][col] == '_':
                    game [row][col] = 'x'
                    break
                else:
                    print('cell is not empty!!!')
            else :
                print('index out of range. \n try again !!!')
        show_game_board()
        check()

        # Player 2
        print('player number 2')    
        while True:        
            row = int(input('Please enter the row number :'))
            col = int(input('Please enter the column number :'))
            if 0<= row <= 2 and 0<= col <=2:
                if game[row][col] == '_':
                    game [row][col] = 'o'
                    break
                else:
                    print('cell is not empty!!!')
            else :
                print('index out of range. \n try again !!!')
        show_game_board()
        check()


# Player & computer
if selection=="2":
     while True: 
        # Player 1
        print('player number 1')
        while True:
            row = int(input('Please enter the row number :'))
            col = int(input('Please enter the column number :'))
            if 0<= row <= 2 and 0<= col <=2:
                if game[row][col] == '_':
                    game [row][col] = 'x'
                    break
                else:
                    print('cell is not empty!!!')
            else :
                print('index out of range. \n try again !!!')
        show_game_board()
        check()

        # Computer
        print('computer')    
        while True:        
            row=random.randint(0,2)
            column=random.randint(0,2)
            if 0<= row <= 2 and 0<= col <=2:
                if game[row][col] == '_':
                    game [row][col] = 'o'
                break
            else:
                print('index out of range. \n try again !!!')
        show_game_board()
        check()