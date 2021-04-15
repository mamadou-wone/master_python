
import pandas

data = pandas.read_csv("country.csv")
colors = data["Primary Fur Color"]
gray = 0
cinnamon = 0
black = 0
for color in colors:
    if color == "Black":
        black += 1
    elif color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        cinnamon += 1

data_dict = {
    'Fur Color': ["grey", "red", "black"],
    'Count': [gray, cinnamon, black]
}
new_csv_dict = pandas.DataFrame(data_dict)
new_csv_file = new_csv_dict.to_csv("squirrel_count.csv")



