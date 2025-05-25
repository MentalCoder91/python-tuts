from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fd():
    tim.forward(10)

def move_bk():
    tim.back(10)

def move_clock_wise():
    tim.circle(50, None, 10)

def move_counter_clock_wise():
    tim.circle(-50,None,10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bk)
screen.onkey(key="a", fun=move_clock_wise)
screen.onkey(key="d", fun=move_counter_clock_wise)

screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
