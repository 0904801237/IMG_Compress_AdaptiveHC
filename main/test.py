import bitarray
import numpy as np

symbols = [[[1,1,11],[2,2,2],[3,3,3],[4,4,4]], 
            [[5,5,5],[6,6,255],[7,7,7],[8,8,8]], 
            [[9,9,9],[10,10,10],[11,11,11],[12,12,12]]]
symbols = np.array(symbols)
symbols = symbols.reshape(1,symbols.size)
for s in symbols[0]:
    print(s)