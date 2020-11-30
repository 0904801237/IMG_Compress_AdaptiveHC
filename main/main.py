import EncodeProcedure as Enp
import DecodeProcedure as Dep
import bitarray

from PIL import Image

import numpy as np
import sys
import csv
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)
        
import numpy as np
from PIL import Image

if __name__ == "__main__":
    '''
    InputSourceSize = 26 # example the alphabet in english has 26 chacracters
    
    #encode
    symbols = [1,1,2,2,2,2,3,4] # ~ [a,a,r,d,v,a,r,k]
    encodedString = Enp.EncodeProcedure(InputSourceSize, symbols)
    print("the encoded string is:", encodedString) 
    # 00000101000100000110001011010110001010
    # 00000101000100000110001011010110001010
    decodedArray = Dep.DecodeProcedure(InputSourceSize, encodedString)
    print("the decoded symbols array is:", decodedArray) # = [1,1,18,4,22,1,18,11]
    '''
    InputSourceSize = 256
    src = './images/a.tiff'
    img = Image.open(src)
    symbols = np.asarray(img)
    a, b = img.size
    
    #write new bin file
    # symbols = [[[0,1,1],[2,2,2],[3,3,3],[4,4,4]], 
    #             [[5,5,5],[6,6,255],[7,7,7],[8,8,8]], 
    #             [[9,9,9],[10,10,10],[11,11,11],[12,12,12]]] 
    
    encodedString = Enp.EncodeProcedure(InputSourceSize, symbols)
    bits = bitarray.bitarray(encodedString)
    #print(len(bits))
    with open('sample.bin', 'wb') as fh:
        bits.tofile(fh)

    w = len(symbols[0])
    # print(len(bits))
    # b = bitarray.bitarray()
    # with open('sample.bin', 'rb') as fh:
    #      b.fromfile(fh)
    # a = 0
    # for i in b:
    #     print(a)
    #     a += 1
    # print(len(b))
    decodedArray = Dep.DecodeProcedure(InputSourceSize, bits, w)
    decodedArray = np.array(decodedArray)
    decodedArray = decodedArray.astype(np.uint8)
    im = Image.fromarray(symbols).save('a.tiff')
    print("done")
    # size = len(bits)
    # with open('sample.bin', 'wb') as fh:
    #      bits.tofile(fh)
    # for i in range(1, len(symbols)):
    #     print(i)
    #     encodedString = Enp.EncodeProcedure(InputSourceSize, symbols[i])
    #     bits = bitarray.bitarray(encodedString)
    #     size += len(bits)
    #     with open('sample.bin', 'ab') as fh:
    #         bits.tofile(fh)
    #print(size)
    # b = bitarray.bitarray()
    # with open('sample.bin', 'rb') as fh:
    #     b.fromfile(fh)
    #     print("start decode")
    #     decodedArray = Dep.DecodeProcedure(InputSourceSize, b.to01())
    #     print(decodedArray)
    #     #numpyDecode = np.array(decodedArray)
    #     #numpyDecode = numpyDecode.reshape(w, h)
    #     #gr_im = Image.fromarray(numpyDecode).save('out.tiff')

    
    
    
  