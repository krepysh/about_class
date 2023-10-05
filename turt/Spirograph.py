import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.shape("turtle")

for _ in range(72):
    tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    tim.circle(100)
    tim.left(5)

screen = t.Screen()
screen.exitonclick()

