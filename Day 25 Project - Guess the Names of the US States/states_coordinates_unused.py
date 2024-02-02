# To get the coordinates of each state:

# Code from stackoverflow:
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


# This is an event listener. It listens for when the mouse clicks and calls the function:
turtle.onscreenclick(get_mouse_click_coor)

# This is an alternative to exitonclick() to make the screen stay open after all code is executed:
turtle.mainloop()
# All the states coordinates is in the 50_states.csv
