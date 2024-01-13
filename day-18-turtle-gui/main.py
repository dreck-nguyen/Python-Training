import random
import turtle as turtle_module
from turtle import Turtle, Screen

colors = [(233, 233, 236), (233, 232, 228), (236, 230, 233), (224, 234, 229), (176, 48, 79), (42, 98, 146),
          (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173),
          (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89), (124, 218, 207), (120, 43, 71), (94, 158, 65),
          (227, 170, 187), (131, 184, 161), (48, 187, 202), (172, 187, 222), (232, 173, 164), (154, 209, 219),
          (100, 51, 43), (34, 64, 115), (44, 80, 79), (215, 207, 37), (52, 58, 66)]

turtle_module.colormode(255)
tim = turtle_module.Turtle()
screen = turtle_module.Screen()

tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    tim.hideturtle()

screen.exitonclick()
