from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

snake_body = []
for pos in starting_positions:
    t1 = Turtle(shape="square")
    t1.color("white")
    t1.penup()
    t1.setpos(pos)
    snake_body.append(t1)
screen.update()

is_moving = True

while is_moving:
    screen.update()
    time.sleep(0.1)

    for snake_seg in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[snake_seg - 1].xcor()
        new_y = snake_body[snake_seg -1].ycor()
        snake_body[snake_seg].goto(new_x, new_y)

    snake_body[0].forward(20)
    snake_body[0].left(-90)
screen.exitonclick()
