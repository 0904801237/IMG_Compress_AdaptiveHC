import EncodeProcedure as Enp
import bitarray

from PIL import Image

import numpy as np
import sys
import csv
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)
        
import numpy
from PIL import Image

def encode(imgSrc, destSource, InputSourceSize):
    # Read image to an array
    img = Image.open(imgSrc)
    img.show()
    symbols = np.asarray(img)
    size = symbols.size * 8
    print("\nthe original size of image: ",size, " bits")
    print("Start encoding...")

    #shape of the orginal image
    shape = numpy.array(symbols.shape)

    #encode image
    encodedString = Enp.EncodeProcedure(InputSourceSize, symbols)
    
    #save the remainder bit
    if(len(encodedString)%8 == 0): shape = numpy.append(shape, 0)
    else: shape = numpy.append(shape, 8 - len(encodedString)%8)
    
    #save to file
    with open('shape.npy', 'wb') as fh:
        numpy.save(fh, shape)
    with open(destSource, 'wb') as fh:
        encodedString.tofile(fh)

    print("\n\nThe image file was encoded to file 'encodeData'.")
    
    print("\nThe compressed file size: ", len(encodedString), " bit")
    print("\nThe image was compressed: ",100 - len(encodedString)*100/(symbols.size * 8), "%")
    print("\n")

if __name__ == "__main__":
    InputSourceSize = 256
    encode('./images/3.tiff', 'encodeData', InputSourceSize)
