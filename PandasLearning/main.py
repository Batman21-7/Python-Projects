import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = data["Primary Fur Color"].to_list()

grey_count = 0
red_count = 0
black_count = 0

for color in fur_colors:
    if color == "Gray":
        grey_count += 1
    elif color == "Cinnamon":
        red_count += 1
    elif color == "Black":
        black_count += 1

df = pandas.DataFrame({"Fur Color": ["grey", "red", "black"], "Count": [grey_count, red_count, black_count]})

df.to_csv("squirrel_count.csv")
# Gray
# Cinnamon
# Black
