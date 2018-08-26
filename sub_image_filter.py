from math import sqrt, ceil, floor
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def calc_columns_rows(n):
    """
    Calculates the number of columns and rows in which the image will be sliced.
    Arg: The number of sub-images.

    """
    num_columns = int(ceil(sqrt(n)))
    num_rows = int(ceil(n / float(num_columns)))
    return (num_columns, num_rows)

def getSubImages(img, cant, save=False, path=""):
    """
    Slices the image in a specific number of sub-images.
    Args:
       img (numpy.array):  The image encoded in numpy array.
       cant (int):  The number of sub-images to obtain.
    Kwargs:
       save (bool): Saves the sub-images to a specific path.
       path (string): Set the specific path.
    Returns:
        Numpy array with the sub-images.
    """
    
    im_w, im_h, _ = img.shape

    print(im_w, im_h)
    
    img = Image.fromarray(np.uint8(img))
    columns, rows = calc_columns_rows(cant)
    extras = (columns * rows) - cant
    sub_img_w, sub_img_h = int(floor(im_w / columns)), int(floor(im_h / rows))

    print(sub_img_w, sub_img_h)

    sum_images = []
    i = 0
    for pos_y in range(0, im_h - rows, sub_img_h):
        for pos_x in range(0, im_w - columns, sub_img_w):
            area = (pos_y, pos_x, pos_y + sub_img_h, pos_x + sub_img_w)
            image = img.crop(area)

            if save:
                image.save(path + "sub_img_" + str(i) + ".png")
            
            sum_images.append(np.asarray(image))
            i += 1
    
    return np.array(sum_images)
