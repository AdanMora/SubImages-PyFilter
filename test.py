import sub_image_filter
import numpy as np
from PIL import Image

img = np.asarray(Image.open("dog.png"))

sub_images = sub_image_filter.getSubImages(img,9, True, "output\\")

print(type(sub_images))
print(type(sub_images[0]))
print(sub_images.shape)
