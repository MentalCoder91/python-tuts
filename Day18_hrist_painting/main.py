###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random

import colorgram
from turtle import Turtle, Screen

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

print(rgb_colors)

tanu = Turtle()

flag = True
while flag:

    tanu.dot(50, random.choice(rgb_colors))
    tanu.penup()
    tanu.forward(50)
    tanu.pendown()
    tanu.dot(50, random.choice(rgb_colors))
    break

screen = Screen()
screen.exitonclick()















