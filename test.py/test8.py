import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

for i in range(60):
    def square(length, angle):
        for i in range(4):
            t.forward(length)
            t.left(angle)
    square(100, 90)
    t.right(5)
    print(i)
turtle.done()