# Assignment 16 (Super Snake 🐍) : 

**📖Overview**

Super Snake is a classic snake game with enhanced features and AI-driven gameplay. The objective is to control a snake as it navigates the field, consuming various fruits to increase its score and length. The game features a smart AI mode where the snake automatically moves towards the nearest fruit without user input.

___

**🗂️Project Structure**

Super Snake <br>
├── fruits.py <br>
├── snake.py <br>
├── main.py <br>
├── main_ai.py <br>
└── README.md <br>

____

**🧩Features**

1. Score Display: The current score is shown on the screen.
2. Striped Snake Body: The snake's body is colored in a striped pattern.
3. Apple Class:
Eating an apple increases the snake's length by one unit.
4. Pear Class:
Eating a pear adds 2 points to the score. 
5. Rotten Fruit Class:
Eating a rotten fruit decreases the score by 1.
6. Game Over Conditions: <br>
The game ends if the snake's score reaches zero. <br>
The game ends if the snake hits the walls. <br>
The game ends if the snake collides with itself.
7. AI Mode: The snake moves automatically towards the nearest fruit using AI.

____

**🚀 How to Run**

Prerequisites

Python 3.x <br>
arcade library

```python
pip install arcade
```


Running the Game

To play manually:

```python
python main.py
```

To watch the AI play:

```python
python main_ai.py
``` 

____

[Super Snake Game Video](Video/Snake.mp4)



