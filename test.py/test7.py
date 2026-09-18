import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
length=5
for i in range(60):
    def square(length, angle):
        for i in range(4):
            t.forward(update_length(length))
            t.left(angle)
            def update_length(length):
                length = length + 5
                length = update_length(length)
    print(i)

    length = 25
    square(length, 90)
    t.right(5)


angle = 90
turtle.done()