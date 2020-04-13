from turtle import Turtle
from random import randint


#create instance for the object Turtle
erik = Turtle()

#add methods to customize the object
erik.shape('turtle')
erik.color('blue')
erik.penup()
erik.goto(-160, 100)
erik.pendown()

# create 3 more turtles
dara = Turtle()
dara.shape('turtle')
dara.color('red')
dara.penup()
dara.goto(-160, 70)
dara.pendown()

doctor = Turtle()
doctor.shape('turtle')
doctor.color('green')
doctor.penup()
doctor.goto(-160, 40)
doctor.pendown()

barry = Turtle()
barry.shape('turtle')
barry.color('black')
barry.penup()
barry.goto(-160, 10)
barry.pendown()



for movement in range(100):
    erik.forward(randint(1,5))
    dara.forward(randint(1,5))
    doctor.forward(randint(1,5))
    barry.forward(randint(1,5))