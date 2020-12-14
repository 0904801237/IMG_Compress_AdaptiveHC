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
    with open(binSource+'/shape.npy', 'rb') as fh:
        shape = numpy.load(fh)
    #read encode bit from file
    bitString = bitarray.bitarray()
    with open(binSource+"/encodeData.bin", 'rb') as fh:
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
    InputPath = "./output" # path to folder contains 2 file: encodeData + shape
    OutPath = "output.tiff" # the output image
    decode(InputPath, 'output.tiff', InputSourceSize)
    