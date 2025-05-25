from turtle import Turtle

import pandas as pd
import turtle


# def get_mouse_click_co(x, y):
#     print(x, y)


def set_state_co(state_name, df_state):
    df_state.state = df_state.state.str.lower()
    check = df_state[df_state.state == state_name]
    print(check)
    if not check.empty:
        x_cor = int(check.iloc[0]['x'])
        y_cor = int(check.iloc[0]['y'])
        state = Turtle()
        state.penup()
        state.setx(x_cor)
        state.sety(y_cor)
        state.hideturtle()
        state.write(state_name.title(), align="center")
        return True
    else:
        print('State not present')
        return False


screen = turtle.Screen()
screen.title('Anish Game')
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pd.read_csv('50_states.csv', sep=',')
states = df['state'].tolist()
guessed_states = []
correct = 0
game_on = True
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"guess the state ({correct} / 50)",
                                    prompt="What's another states name?").title()
    ans = set_state_co(answer_state.lower(), df)
    if ans:
        guessed_states.append(answer_state.lower())
        try:
            states.remove(answer_state)
        except:
            print('Nothing')
    else:
        guessed_states.append(answer_state.lower())

        correct += 1
# turtle.onscreenclick(get_mouse_click_co)
# screen.exitonclick()
turtle.mainloop()

pd.Series(states).to_csv('Missed.csv')


