import EncodeProcedure as Enp
import DecodeProcedure as Dep
import bitarray

from PIL import Image

import numpy as np
import sys
import csv
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)
        
import numpy
from PIL import Image

if __name__ == "__main__":

    InputSourceSize = 256
    src = './images/a.tiff'
    img = Image.open(src)
    symbols = np.asarray(img)
    
    
    #symbols = numpy.asarray([0, 0, 17, 3, 21, 0, 17, 10])
    #[0, 0, 17, 3, 21, 0, 17, 10] ~ aardvark
    #00000101000100000110001011010110001010
    shape = symbols.shape
    print("Start decoding...")
    encodedString = Enp.EncodeProcedure(InputSourceSize, symbols)
    print("Encode done:", len(encodedString), " bit")
    
    with open('sample', 'wb') as fh:
        encodedString.tofile(fh)
    print("Start decoding...")
    decodedArray = Dep.DecodeProcedure(InputSourceSize, encodedString, shape)
    
    img = Image.fromarray(symbols).save('a.tiff')
    print("decoding done!")