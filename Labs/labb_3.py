
import numpy as np
import matplotlib.pyplot as plt


min_data = np.loadtxt("unlabelled_data.csv", delimiter=",")

# I drew my own line through these points to split the data
POINT_1 = np.array([2, -1])
POINT_2 = np.array([-4, 3])

k = (POINT_2[1] - POINT_1[1]) / (POINT_2[0] - POINT_1[0])
m = POINT_1[1] - k * POINT_1[0]
x_range = np.linspace(min(min_data[:, 0]), max(min_data[:, 0]), 100)

y = k * x_range + m


def right_or_left(points):
    classifications = []
    for point in points:
        point_1 = point[0]
        point_2 = point[1]
        line = k * point_1 + m
        if point_2 > line:
            classifications.append(0)
        else:
            classifications.append(1)
    return classifications

classifications = right_or_left(min_data)

labelled_data = np.column_stack((min_data, classifications))

np.savetxt("labelled_data.csv", labelled_data, delimiter=",", fmt="%.15f, %.15f, %d")

for point, classification in zip(min_data, classifications):
    if classification == 0:
        plt.scatter(point[0], point[1], color='green', edgecolors="black", label="Right(0)" if "Right(0)" not in plt.gca().get_legend_handles_labels()[1] else "")
    else:
        plt.scatter(point[0], point[1], color='blue', edgecolors="black", label="Left(1)" if "Left(1)" not in plt.gca().get_legend_handles_labels()[1] else "")


plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Testdata with Classification")
plt.plot(x_range, y, color='red')
plt.legend()
plt.show()