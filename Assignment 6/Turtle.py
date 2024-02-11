from turtle import *
import turtle

shape("turtle")
color("green")
width(2)

def makeShape ():
   
    l = 30
    h = 15

    for numSides in range(3,10):

        degree = ((numSides - 2) * 180) / numSides
        left(180 - (degree/2))
        
        for i in range(numSides):
            forward(l)
            left(180 - degree)

        right(180-(degree/2))
        penup()
        forward(h)
        pendown()

        l += 15
        h += 2


makeShape()

turtle.done()  

