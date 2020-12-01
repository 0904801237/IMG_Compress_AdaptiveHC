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

def encode(imgSrc, InputSourceSize):
    # Read image
    img = Image.open(imgSrc)
    symbols = np.asarray(img)

    #InputSourceSize = 26
    #symbols = numpy.asarray([0, 0, 17, 3, 21, 0, 17, 10])
    #[0, 0, 17, 3, 21, 0, 17, 10] ~ aardvark
    #00000101000100000110001011010110001010

    shape = numpy.array(symbols.shape)
    #encode image
    print("Start encoding...")
    encodedString = Enp.EncodeProcedure(InputSourceSize, symbols)
    print("Encode done:", len(encodedString), " bit")

    shape = numpy.append(shape, 8 - len(encodedString)%8)
    
    # #save to file
    with open('shape.npy', 'wb') as fh:
        numpy.save(fh, shape)
    with open('encodeData', 'wb') as fh:
        encodedString.tofile(fh)

def decode(binSource, imgDest, InputSourceSize):
    with open('shape.npy', 'rb') as fh:
        shape = numpy.load(fh)
    #read encode bit from file
    bitString = bitarray.bitarray()
    with open(binSource, 'rb') as fh:
        bitString.fromfile(fh)
    del bitString[len(bitString)-shape[-1]:len(bitString)]
    #decoding
    print("Start decoding...")
    decodedArray = Dep.DecodeProcedure(InputSourceSize, bitString, shape[:-1])
    img = Image.fromarray(decodedArray).save(imgDest)
    print("decoding done!")

if __name__ == "__main__":
    InputSourceSize = 256
    #encode('./images/lena512color.tiff', InputSourceSize)
    decode('encodeData', 'output.tiff', InputSourceSize)
    