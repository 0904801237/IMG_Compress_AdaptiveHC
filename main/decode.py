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

def decode(binSource, imgDest, InputSourceSize):
    print("Start decoding...")
    with open('shape.npy', 'rb') as fh:
        shape = numpy.load(fh)
    #read encode bit from file
    bitString = bitarray.bitarray()
    with open(binSource, 'rb') as fh:
        bitString.fromfile(fh)
    del bitString[len(bitString)-shape[-1]:len(bitString)]
    #decoding
    decodedArray = Dep.DecodeProcedure(InputSourceSize, bitString, shape[:-1])
    img = Image.fromarray(decodedArray)
    img.save(imgDest)
    img.show()
    print("\nDecode done!")
if __name__ == "__main__":
    InputSourceSize = 256
    decode('encodeData', 'output.tiff', InputSourceSize)
    