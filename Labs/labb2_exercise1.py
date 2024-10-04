
import numpy as np
from labb_2 import read_file

width, height, label = read_file("datapoints.txt")

while True:
    try:
        user_width = float(input("What is the width of your pokemon(cm)? "))
        if 0 <= user_width:
            break
        else:
            print("The width can´t be a negative number")
    except ValueError:
        print("The width needs to be a number")

while True:
    try:
        user_height = float(input("What is the height of your pokemon(cm)? "))
        if 0 <= user_height:
            break
        else:
            print("The height can´t be a negative number")
    except ValueError:
        print("The height needs to be a number")

distance = np.sqrt((np.array(width) - user_width) ** 2 + (np.array(height) - user_height) ** 2)
nearest_point = np.argmin(distance)
classification = label[nearest_point]
pokemon_classification = "Pikachu" if classification == 1 else "Pichu"
print(f"Your pokemon is a {pokemon_classification}")