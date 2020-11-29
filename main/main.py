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
    src = '/media/hunn/E/Documents/code/other python/compress image/IMG_Compress_AdaptiveHC/images/lena_color.tiff'
    img = Image.open(src).convert('L')
    symbols = np.asarray(img)
    w, h = img.size

    #write new bin file
    encodedString = Enp.EncodeProcedure(InputSourceSize, symbols[0])
    bits = bitarray.bitarray(encodedString)

    with open('sample.bin', 'wb') as fh:
        bits.tofile(fh)
    for i in range(1, len(symbols)):
        print(i)
        encodedString = Enp.EncodeProcedure(InputSourceSize, symbols[i])
        bits = bitarray.bitarray(encodedString)
        with open('sample.bin', 'ab') as fh:
            bits.tofile(fh)

    b = bitarray.bitarray()
    with open('sample.bin', 'rb') as fh:
        b.fromfile(fh)
        print("start decode")
        decodedArray = Dep.DecodeProcedure(InputSourceSize, b.to01())
        print(decodedArray)
        #numpyDecode = np.array(decodedArray)
        #numpyDecode = numpyDecode.reshape(w, h)
        #gr_im = Image.fromarray(numpyDecode).save('out.tiff')

    
    
    
  