from turtle import *
from random import randint

speed(10)
penup()
goto(-140, 140)

for step in range(15):
    write(step, align="center")
    right(90)
    forward(10)
    pendown()
    for n in range(10):
        forward(7)
        penup()
        forward(8)
        pendown()
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle("turtle")
ada.color("red")
ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle("turtle")
bob.color("blue")
bob.penup()
bob.goto(-160, 70)
bob.pendown()

eva = Turtle("turtle")
eva.color("purple")
eva.penup()
eva.goto(-160, 40)
eva.pendown()

tortilla = Turtle("turtle")
tortilla.color("green")
tortilla.penup()
tortilla.goto(-160, 10)
tortilla.pendown()

for turn in range(10):
    ada.right(36)
    bob.left(36)
    eva.right(36)
    tortilla.left(36)

for turn in range(100):
    ada.penup()
    ada.forward(randint(1, 5))
    ada.pendown()
    bob.penup()
    bob.forward(randint(1, 5))
    bob.pendown()
    eva.penup()
    eva.forward(randint(1, 5))
    eva.pendown()
    tortilla.penup()
    tortilla.forward(randint(1, 5))
    tortilla.pendown()
    delay(10)

input()