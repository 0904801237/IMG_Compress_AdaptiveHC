import EncodeProcedure as Enp
import DecodeProcedure as Dep
import bitarray
import random

from PIL import Image

import numpy as np
import sys
import csv
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)
        
import numpy
from PIL import Image

def encode(imgSymbols, destSource, InputSourceSize):
    symbols = numpy.asarray(imgSymbols) # ~ aardvark
    print("the original size of image: ",symbols.size * 5, " bits")
    # 00000101000100000110001011010110001010

    #shape of the orginal image
    shape = numpy.array(symbols.shape)

    #encode image
    encodedString = Enp.EncodeProcedure(InputSourceSize, symbols)
    #print("\nEncode bits string: ", encodedString)
    #000
    #save the remainder bit
    if(len(encodedString)%8 == 0): shape = numpy.append(shape, 0)
    else: shape = numpy.append(shape, 8 - len(encodedString)%8)
    
    #save to file
    with open('shape.npy', 'wb') as fh:
        numpy.save(fh, shape)
    with open(destSource, 'wb') as fh:
        encodedString.tofile(fh)

    #print("The image file was encoded to file 'encodeData'.")
    #print("The compressed string: ", encodedString)
    print("\nThe compressed file size: ", len(encodedString), " bit")
    print("The image was compressed: ",100 - len(encodedString)*100/(symbols.size * 5), "%")

    return encodedString
def decode(binSource, imgDest, InputSourceSize):
    with open('shape.npy', 'rb') as fh:
        shape = numpy.load(fh)
    #read encode bit from file
    bitString = bitarray.bitarray()
    
    with open(binSource, 'rb') as fh:
        bitString.fromfile(fh)
    
    del bitString[len(bitString)-shape[-1]:len(bitString)]
    #decoding
    decodedArray = Dep.DecodeProcedure(InputSourceSize, bitString, shape[:-1])
    #img = Image.fromarray(decodedArray).save(imgDest)
    return decodedArray
if __name__ == "__main__":
    InputSourceSize = 26 # [a - z]

    symbols = []
    for i in range(1000000):
        symbols.append(random.randrange(0, 25))
    
    print("\nThe symbols size", len(symbols))

    encodeBitsString = encode(symbols, 'encodeData', InputSourceSize)

    decodeSymbol = decode('encodeData', 'test.bmp', InputSourceSize)

    print("\n", (symbols == decodeSymbol).all(), "\n")

