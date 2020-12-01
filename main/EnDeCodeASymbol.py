import math
import bitarray
def FindER(m):
    '''
    @param m: the size of input symbol sources
    '''
    e = math.floor(math.log2(m))
    r = m-(2**e)
    return [e, r]

def Encode(e, r, k):
    '''
    @param k: the numerical order of ak in input symbol sources {a1, a2, ..., ak,..., am}
    @return: the binary string encoded of ak
    '''
    if(0 <= k < 2*r) :
        # ak = k-1 using e+1 bit
        return bitarray.bitarray('{0:b}'.format(k).zfill(e+1))
    # ak = k-r-1 using e bit
    return bitarray.bitarray('{0:b}'.format(k - r).zfill(e))
        
def Decode(e, r, encodedBitsArray, i):
    '''
    @param encodedArray: the binary array encoded
    @return p: the symbol being decoded
    '''
    p = int(encodedBitsArray[i:i+e].to01(),2)
    #del encodedBitsArray[:e]
    i = i+e
    if(p >= r): return p + r, i
    return p*2 + encodedBitsArray[i], i+1
    