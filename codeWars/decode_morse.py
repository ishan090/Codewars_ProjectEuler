# Related to bits in morsecode

# Standard libaray
import math
import random
# import matplotlib.pyplot as plt
import numpy as np

def parse_data(bits):
    """
    Takes in bits in a string and returns a split version of them    
    """
    current = "0"
    index = 0
    split = []
    for i in range(len(bits)):
        if bits[i] != current:
            split.append(bits[index:i])
            current = bits[i]
            index = i
    split.append(bits[index:])
    return split

print(parse_data("000011110011011010101000"))


def cluster_means(clusters):
    """
    Given the clusters, finds their mean
    """
    return [sum(c)/len(c) for c in clusters]

# print(cluster_means([[np.array([i, j]) for i in range(3) for j in range(3, 6)]]))


def MinkowskiDist(x, y, p):
    """
    Returns the Minkowski distance between two points for a certain p
    """
    assert len(x) == len(y), "Can only find the distance between two vectors of the same degree"
    return math.pow(sum([math.pow(abs(x[i] - y[i]), p) for i in range(len(x))]), 1/p)


print("L2:", MinkowskiDist([1, 2], [2, 4], 2))

def norm(x):
    return MinkowskiDist(x, np.zeros(len(x)), 2)


def initial_means(data: list, k):
    """
    This time data is a frequency distribution of the form:
    bits : frequency
    """
    means = []
    freq = {}
    # Idea over here is to form a frequency dict sorting all of data.
    # The first mean is chosen randomly from data
    # The others are chosen from the remaining data points such that
    # each mean is different with greater probability given to a data point further away
    # from any of the other means
    first = random.choice(data)   # choose first, del from main list and add to the means
    del data[data.index(first)]
    means.append(first)
    for i in data:   # For the rest of them, add them into freq by their distance
        dist = MinkowskiDist(first, i, 2)
        freq[dist] = freq.get(dist, []) + [i]
    
    for i in range(k-1):  # time to add the other means
        # choose the distance and then randomly get a value
        # associated with that distance from the freq dict
        while True:
            d = random.choices(list(freq.keys()), weights=[i*len(freq[i]) for i in freq])[0]
            mean = random.choice(freq[d])
            if mean not in means:
                break
        del freq[d][freq[d].index(mean)]   # del the mean from freq
        means.append(mean)    # and also add it to the means
        # Now, update the freq dict. But a dict can't be changed while iterating so store it in a new dict
        new_dict = freq.copy()
        for key, values in freq.items():
            for val in values:
                dist = MinkowskiDist(mean, val, 2)
                if dist < key:   # If the distance between a point and the new mean is lesser than ever,
                    # update the value
                    new_dict[dist] = new_dict.get(dist, []) + [val]
                    # and remove the value from its previous spot
                    del new_dict[key][new_dict[key].index(val)]
        # Great, now repeat until all of the means are found, then return
    return means
                    




print("initial means", initial_means([(i,) for i in [1, 2, 3, 5, 8, 5, 3, 2, 9]], 3))



def k_means_cluster(data, k):
    """
    Given `data` distributes it along `k` clusters
    For the pusposes of this program, I'll only be needing to do things in one dimension,
    but I'll still try and make this adaptable for d dimensions
    """
    centroids = initial_means(data, k)
    print("initial means", centroids)
    converged = False
    while not converged:
        clusters = [[]]*k
        for point in data:
            print("point", point)
            least = None
            index = 0
            print(centroids, point)
            for c in range(len(centroids)):
                dist = MinkowskiDist(point, centroids[c], 2)
                print("\tdistance between", point, "and", centroids[c], "=", dist)
                if least is None or dist < least:
                    index = c
                    print("vals", point, centroids[c])
                    least = dist
            print("assinging", point, "to", clusters[index])
            clusters[index].append(point)
        print("this is clusters", clusters)
        c = cluster_means(clusters)
        if c == centroids:
            converged = True
        centroids = c
    return clusters


print(k_means_cluster([[3], [4], [5], [3], [2], [5], [11], [9], [10], [11]], 2))



# # Create data for the x and y axes
# x_data = np.array([1, 2, 3, 4, 5])
# y_data = np.array([10, 8, 6, 4, 2])

# # Create the plot
# plt.plot(x_data, y_data)

# # Add labels and title (optional but recommended)
# plt.xlabel("X-axis Label")
# plt.ylabel("Y-axis Label")
# plt.title("Simple 1D Line Plot")

# # Display the plot
# plt.show()
