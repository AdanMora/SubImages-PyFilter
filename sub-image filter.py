import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_images

def getSubImages(img, dim, stride):
    images = []
    x = 0
    y = 0
    for i in range(0, img.shape[0]-dim, stride):
        for j in range(0, img.shape[1]-dim, stride):
            if ((i+dim <= img.shape[0]) and (j+dim <= img.shape[1])):
                images.append(img[i:i+dim, j:j+dim])
    return images

dataset = load_sample_images()
img = dataset.images[1]

#print(img)
#print(img.shape)

plt.imshow(img[25:350,80:350])
plt.show()

img = img[25:350,80:350]

imagenes = getSubImages(img,200,10)

for m in imagenes:
    plt.imshow(m)
    plt.show()
