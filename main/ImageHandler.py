from PIL import Image

import numpy as np
import sys
import csv
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)

def getImageRBG (src): 
    img = Image.open(src).convert('L')
    #ary = np.array(img)
    #img.save('b1.jpg')
    image_array = np.asarray(img)
    #im = Image.fromarray(a, 'RGB')
    #img.save('test.jpg')
    return image_array
