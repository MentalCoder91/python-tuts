import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race?")

colors = [
    {'color': 'red', 'pos': 100},
    {'color': 'green', 'pos': 60},
    {'color': 'black', 'pos': 20},
    {'color': 'purple', 'pos': -20},
    {'color': 'blue', 'pos': -60},
    {'color': 'grey', 'pos': -100}]

turtles = []
for item in colors:
    data = {}
    tim = Turtle()
    tim.penup()
    tim.color(item['color'])
    tim.shape('turtle')
    tim.setpos(-240, item['pos'])
    data['color'] = item['color']
    data['object'] = tim
    turtles.append(data)
print(turtles)

race_on = False
if user_bet:
    race_on = True

winner = None
while race_on:
    for turtle in turtles:
        rand_dist = random.choice(range(0, 10))
        turtle['object'].forward(rand_dist)

        (x, y) = turtle['object'].pos()
        if x > 218:
            winner = turtle['color']
            race_on = False
            break

print(user_bet)

if winner == str(user_bet).lower():
    print("You win")
else:
    print(f"You Lose.. winner is {winner}")

screen.exitonclick()
