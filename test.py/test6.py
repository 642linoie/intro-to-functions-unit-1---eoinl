import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

def addSquares(iRange):
    length = 25
    def square(length, angle):
        for i in range(60):
            t.forward(length)
            t.left(angle)
    for i in range(iRange):
        square(length, 95)
        length = length+25
addSquares(5)


turtle.done()