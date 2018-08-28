from math import sqrt, ceil, floor
import numpy as np
from PIL import Image
import torchvision.transforms as transforms

def _calc_columns_rows(n):
    """
    Calculates the number of columns and rows in which the image will be sliced.
    Arg: The number of sub-images.

    """
    num_columns = int(ceil(sqrt(n)))
    num_rows = int(ceil(n / float(num_columns)))
    return (num_columns, num_rows)

def getSubImages(img, cant, save=False, path="", output="Pytorch"):
    """
    Slices the image in a specific number of sub-images.
    Args:
       img (PIL.Image):  The image encoded in PIL Image.
       cant (int):  The number of sub-images to obtain.
    Kwargs:
       save (bool): Save sub-images to a specific path.
       path (string): Set specific path.
       output (string): Set output format: 'Numpy', 'PIL' or 'Pytorch' 
    Returns:
        List with the sub-images, by default in Pytorch Tensor.
    """

    if output not in ("Pytorch", "PIL", "Numpy"):
            raise ValueError('sub_image_sampler must be \'Pytorch\', \'Numpy\' or \'PIL\'') 

    im_w, im_h = img.size

    columns, rows = _calc_columns_rows(cant)
    sub_img_w, sub_img_h = int(floor(im_w / columns)), int(floor(im_h / rows))

    sum_images = []
    i = 0
    for pos_y in range(0, im_h - rows, sub_img_h):
        for pos_x in range(0, im_w - columns, sub_img_w):
            area = (pos_y, pos_x, pos_y + sub_img_h, pos_x + sub_img_w)
            image = img.crop(area)

            if save:
                image.save(path + "sub_img_" + str(i) + ".png")

            if output == "PIL":
                sum_images.append(image)
            elif output == "Pytorch":
                sum_images.append(transforms.ToTensor()(image))
            else:
                sum_images.append(np.asarray(image))

            i += 1
    
    return sum_images
