import matplotlib.pyplot as plt # for plotting
import pandas as pd # for dataframe / csv reading
import numpy as np # for array calculations

# create a figure with a 3d axes
fig = plt.figure()
ax = plt.axes(projection='3d')

# read the .csv file into a dataframe "data"
data = pd.read_csv("dataset.csv")
print(data.head())

# create a list "clrs" containing all the rgb values listed in
# the csv file
clrs = zip(data.loc[:,"red"], data.loc[:,"green"], data.loc[:,"blue"])
clrs = list(clrs)

# for index and value in list "clrs"
for i, clr in enumerate(clrs):
    # normalise the values from 1-255 --> 0-1
    nplist = np.array(clrs[i])
    nplist_max = max(nplist)
    normalised = nplist / nplist_max
    # outputs   
    print("RGB:        " + str(clrs[i]))
    print("Normalised: (%.3f, %.3f, %.3f)" % (normalised[0], normalised[1], normalised[2]))
    print("Labelled as: %s\n" % str(list(data.loc[:,"label"])[i]))
    # update the "clrs" list to contain the normalised value
    clrs[i] = normalised

# plot a 3d scatter plot where x=red, y=green and z=blue
# set the colour of each point to its corresponding value in "clrs"
ax.scatter3D(data.loc[:,"red"],data.loc[:,"green"],data.loc[:,"blue"],color=clrs)
ax.set_xlabel("Red")
ax.set_ylabel("Green")
ax.set_zlabel("Blue")

# ax.axis("off")

# output the unique "labels" and their frequencies
print(data.label.value_counts())
plt.show()