# Problem posted at 
# For example, given an image 3 pixels wide and 2 pixels tall, 
# the image data 123456789012 corresponds to the following image layers:
#Layer 1: 123
#         456
#
#Layer 2: 789
#         012
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
pixels = []

with open('day8.txt') as f:
    for num in f.read().strip():
        pixels.append(int(num))
    
print(len(pixels))
width = 25
height = 6
numLayers = len(pixels)/(width*height)
layers = []

# building layers
while len(pixels)>0:
    grid = np.ones((height, width)) * np.nan
    j=0
    while j<height:
        for i in range(0,width):
            grid[j,i] = pixels[i]
        pixels = pixels[width:]
        j += 1
    layers.append(grid)

# PART ONE - finding the layer with least 0s and returning number of 1s x number of 2s in that layer
count2 = np.count_nonzero(layers[0] == 0)
for layer in layers:
    count = np.count_nonzero(layer == 0)
    if count < count2:
        count2 = count
        bestLayer = layer
onesTimesTwos = np.count_nonzero(bestLayer == 1) * np.count_nonzero(bestLayer == 2)
print(onesTimesTwos)

# PART 2

def pixel_check(j,i):
    k = 0
    while k<len(layers)-1:
        pixel = int(layers[k][j,i])
        if pixel == 2:
            #print('transparent')
            continue
        elif pixel == 1:
            print('white')
            return 1
        elif pixel == 0:
            print('black')
            return 0
        k += 1

message = np.full((height,width),2)

for j in range(0,height):
    for i in range(0,width):
        #message[j,i] = pixel_check(j,i)
        pass

for layer in layers:
    for j in range(0,height):
        for i in range(0,width):
            if message[j,i] == 2:
                message[j,i] = layer[j,i]

print(message)

# create discrete colormap
cmap = colors.ListedColormap(['red', 'blue'])
bounds = [0,1,2]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
draw = ax.imshow(message, cmap=cmap, norm=norm)
draw.axes.get_xaxis().set_visible(False)
draw.axes.get_yaxis().set_visible(False)

plt.show()