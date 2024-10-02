import matplotlib.pyplot as plt
import numpy as np

width = [] 
height = []
label = []
with open("datapoints.txt", "r") as file:
    next(file)
    for line in file:
        lines = line.strip().split(",")
        width.append(float(lines[0]))
        height.append(float(lines[1]))
        label.append(int(lines[2]))



test_width = []
test_height = []
with open("testpoints.txt", "r") as file:
    next(file)
    for line in file:
        lines = line.split(". ")[1].strip().strip("()").replace(" ", "")
        x, y = lines.split(",")
        test_width.append(float(x))
        test_height.append(float(y))


test_label = []
for tw, th in zip(test_width, test_height):
    distance = np.sqrt((np.array(width) - tw) **2 + (np.array(height) - th) **2)
    nearest_point = np.argmin(distance)
    classification = label[nearest_point]
    test_label.append(label[nearest_point])
    print(f"Sample with (width, height): ({tw}, {th}) is {classification}")

        

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












