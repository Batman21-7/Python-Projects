import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

df = pd.read_csv("50_states.csv")

correct = 0
states = []
all_states = df.state.to_list()
while len(states) < 50:
    answer_state = screen.textinput(f"{correct}/50 States Correct", "What's another state's name?")
    if answer_state is not None:
        answer_state = answer_state.title()
    if answer_state == "Quit":
        break
    row = df.loc[df["state"] == answer_state]
    if not row.empty:
        if answer_state not in states:
            x = df.loc[df["state"] == answer_state, "x"]
            y = df.loc[df["state"] == answer_state, "y"]
            t.goto(int(x.iloc[0]), int(y.iloc[0]))
            t.write(answer_state)

            correct += 1
            states.append(answer_state)

for state in states:
    all_states.remove(state)
states_to_learn = pd.DataFrame(data=all_states, columns=["States"])
states_to_learn.to_csv("states_to_learn.csv")
