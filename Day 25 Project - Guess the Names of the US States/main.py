import turtle
import pandas

# Setting up screen:
screen = turtle.Screen()
screen.title("U.S. States Game")
# (Note that turtle only works with gif image files):
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Setting up text to write the name of the state at the state's location after state is guessed:
text = turtle.Turtle()
text.penup()
text.hideturtle()

# Separates the 3 columns of states, x coordinates and y coordinates into their own list.
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
x_cor_list = data.x.to_list()
y_cor_list = data.y.to_list()


correct_guesses = 0
game_running = True
while game_running is True:
    answer = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                              prompt="What's a state's name? Type 'give up' to stop guessing.").title()

    if answer == "Give Up":
        game_running = False
        # Or use 'break' keyword.

    # If answer is a state that has not been guessed yet, obtain the position of the state in the list
    # and the coordinates where the state should be displayed on the screen:
    if answer in state_list:
        index = state_list.index(answer)
        x_cor = x_cor_list[index]
        y_cor = y_cor_list[index]

        # Writes the name of the state at where the state is located on the map:
        text.goto(x_cor, y_cor)
        text.write(arg=state_list[index])

        # Removes data about the guessed state from all lists to ensure data on any state cannot be called twice:
        x_cor_list.remove(x_cor)
        y_cor_list.remove(y_cor)
        state_list.remove(answer)

        correct_guesses += 1

    else:
        pass

    if correct_guesses == 50:
        game_running = False

# To get x and y cor of state, model answer uses: ans_state = data[data.state == answer] to get the data row of state
# we can then write text.goto(float(ans_state.x), float(ans_state.y))

# To provide feedback on user's performance:
new_data = pandas.DataFrame(state_list)
new_data.to_csv("states_to_learn.csv")
print("Check the states_to_learn.csv file to see the list of states you couldn't remember. Happy learning!")
