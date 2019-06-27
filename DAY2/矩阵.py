import numpy as np

from PIL import Image

im = Image.open("d:/TD/4.jpg")
print(im, type(im))

im = np.array(im)

