import turtle as t
import random


# def random_colors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rand =  (r, g, b)
#     return rand


tim = t.Turtle()
tim.speed('fastest')
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colours))
    #tim.color(random_colors())
    tim.pensize(10)
    tim.forward(30)
    tim.setheading(random.choice(directions))