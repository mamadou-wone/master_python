import turtle
import pandas


def display_country(x, y, country_name):
    my_country = turtle.Turtle()
    my_country.penup()
    my_country.hideturtle()
    my_country.goto(x, y)
    my_country.write(country_name, font=("Arial", 8, "normal"))


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_country = []

for country in data['state']:
    all_country.append(country)
print(all_country)
game_is_on = True

total_country = len(data['state'])
country_guest = 0

while game_is_on:
    answer = screen.textinput(f" {country_guest}/50 States Coorect", "Guest a Country")
    country = answer.title()
    if country != "" and country in all_country:
        country_info = data[data["state"] == country]
        x_cor = country_info["x"]
        y_cor = country_info["y"]
        display_country(int(x_cor), int(y_cor), country)
        country_guest += 1
        all_country.remove(country)

    if country_guest == 50:
        game_is_on = False







turtle.mainloop()

# screen.exitonclick()
