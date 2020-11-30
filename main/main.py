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
    symbols = [1,1,18,4,22,1,18,11] # ~ [a,a,r,d,v,a,r,k]
    encodedString = Enp.EncodeProcedure(InputSourceSize, symbols)
    print("the encoded string is:", encodedString) 
    # 00000101000100000110001011010110001010
    # 00000101000100000110001011010110001010
    # 00000101000100000110001011010110001010
    decodedArray = Dep.DecodeProcedure(InputSourceSize, encodedString)
    print("the decoded symbols array is:", decodedArray) # = [1,1,18,4,22,1,18,11]
    '''
    InputSourceSize = 256
    src = './images/a.tiff'
    img = Image.open(src)
    symbols = np.asarray(img)
    shape = symbols.shape
    
    # symbols = [[[0,0,17],[3,21,2],[3,3,3],[4,4,4]], 
    #             [[5,5,5],[6,6,255],[7,7,7],[8,8,8]], 
    #             [[9,9,9],[10,10,10],[11,11,11],[12,12,12]]] 
    
    
    encodedString = Enp.EncodeProcedure(InputSourceSize, symbols)
    print(len(encodedString))
    with open('sample', 'wb') as fh:
        encodedString.tofile(fh)
    
    decodedArray = Dep.DecodeProcedure(InputSourceSize, encodedString, shape)
    
    im = Image.fromarray(symbols).save('a.tiff')
    print("done")
    print(decodedArray == symbols)