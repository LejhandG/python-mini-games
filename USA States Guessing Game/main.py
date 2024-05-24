import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
map_image = "blank_states_img.gif"
screen.addshape(map_image)
turtle.shape(map_image)

df = pandas.read_csv("50_states.csv")

def guess_state(name, x, y):
    state = turtle.Turtle()
    state.penup()
    state.hideturtle()
    state.goto(x, y)
    state.write(name, align="center", font=("candara", 10, "bold"))

count = 0
flag = True
while flag:
    if count == 50:
        flag = False
    answer_state = screen.textinput("Input", "Enter the name of the state")
    answer_state = answer_state.title()
    if answer_state in df['state'].values:
        state_data = df[df['state'] == answer_state]
        guess_state(answer_state, state_data['x'].values[0], state_data['y'].values[0])
        count += 1
    else:
        continue