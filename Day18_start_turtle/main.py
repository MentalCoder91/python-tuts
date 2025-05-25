from turtle import Turtle, Screen

# def penup_down(timy):
#     count = 0
#     up = True
#     while count != 50:
#         timy.forward(count)
#         if up:
#             timy.pendown()
#             up = False
#         else:
#             timy.penup()
#             up = True
#         count += 5


tim = Turtle()
tim.shape('turtle')
tim.color('red')

cnt = 4
cnt_glob = 4
total = 360
angle = 90
flag = False
while cnt != 0 and cnt_glob != 11:
    tim.forward(100)
    tim.right(angle)

    if cnt == 1:
        flag = True
    cnt -= 1

    if flag:
        cnt = cnt_glob + 1
        angle = total / cnt
        cnt_glob += 1
        flag = False

screen = Screen()
screen.exitonclick()
