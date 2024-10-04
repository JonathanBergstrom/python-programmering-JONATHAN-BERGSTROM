
import matplotlib.pyplot as plt
import numpy as np

def read_file(file_path):
    width = [] 
    height = []
    label = []
    with open(file_path, "r") as file:
        next(file)
        for line in file:
            lines = line.strip().split(",")
            width.append(float(lines[0]))
            height.append(float(lines[1]))
            label.append(int(lines[2]))
    return width, height, label

width, height, label = read_file("datapoints.txt")

test_width = []
test_height = []
with open("testpoints.txt", "r") as file:
    next(file)
    for line in file:
        lines = line.split(". ")[1].strip().strip("()").replace(" ", "")
        x, y = lines.split(",")
        test_width.append(float(x))
        test_height.append(float(y))

# Tried to plot be 10 nearest points. Had to google and try a lot.
test_label = []
for tw, th in zip(test_width, test_height):
    distance = np.sqrt((np.array(width) - tw) **2 + (np.array(height) - th) **2)
    nearest_10_points = np.argsort(distance)[:10]
    classification_10_nearest_points = np.array(label)[nearest_10_points]
    counting_labels, counts = np.unique(classification_10_nearest_points, return_counts=True)
    classification_index = np.argmax(counts)
    classification = counting_labels[classification_index]
    pokemon_classification = "Pikachu" if classification == 1 else "Pichu"
    test_label.append(pokemon_classification)
    print(f"Sample with (width, height): ({tw}, {th}) classified as {pokemon_classification}")


        

for _ in range(len(label)):
    if label[_] == 1:
        plt.scatter(width[_], height[_], color = "yellow")
    else:
        plt.scatter(width[_], height[_], color = "black")


for tw, th, tlabel in zip(test_width, test_height, test_label):
    color = 'yellow' if tlabel == 1 else 'black'
    plt.scatter(tw, th, color = "green" if tlabel == 1 else "red")



plt.title("Pikachu eller Pichu?")
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")


plt.show()
