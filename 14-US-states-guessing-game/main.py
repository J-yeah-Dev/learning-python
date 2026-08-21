import turtle
import pandas

FONT =("Arial", 9, "normal")

screen = turtle.Screen()
screen.title("US state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guesed_states = []

while len(guesed_states)< 50:

    answer_state = screen.textinput(title=f"{len(guesed_states)}/50  states correct",
                                    prompt="whats another state name?").title()
    if answer_state == "Exit":
        # mising_states = []
        # for state in all_states:
        #     if state not in guesed_states:
        #         mising_states.append(state)
        mising_states = [state for state in all_states if state not in guesed_states]
        new_data= pandas.DataFrame(mising_states)
        new_data.to_csv("missed_states.csv")
        break;
    if answer_state in guesed_states:
        answer_state = screen.textinput(title=f"{len(guesed_states)}/50  states correct", prompt="You already guessed that state. \n Whats another state name?").title()

    if answer_state in all_states:
        guesed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(f"{state_data.state.item()}", font=FONT)



