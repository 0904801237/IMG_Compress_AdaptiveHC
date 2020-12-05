import UpdateProcedure as UpdateProcedure
import EnDeCodeASymbol as EnDeCodeASymbol
import math
import bitarray
import numpy
from progress.bar import ShadyBar
    
def DecodeProcedure(inputSourceSize, encodedBitsArray, shape) :
    '''
    @param: inputSourceSize : # the total leafs ~ total size of source
    @param: encodedString : the binary string encoded from the source
    @return: decodedArray : the symbols array decoded from the encodedString
    '''

    [e, r] = EnDeCodeASymbol.FindER(inputSourceSize)
    # the total nodes
    totalNodes = 2*inputSourceSize - 1
    # create a tree with only one node (NYT)
    AHM_Tree = UpdateProcedure.AdaptiveHuffmanTree(totalNodes)
    AHM_Tree.refresh()
    
    decodedArray = []
    i = 0
    progressbar = ShadyBar(
        'decoding',
        max=len(encodedBitsArray),
        suffix='%(percent).1f%% - %(elapsed_td)ss'
    )
    while (len(encodedBitsArray) != i):
        #print(len(encodedBitsArray)-i)
        current = AHM_Tree
        #if current is not an external node (leaf node) -> read next bit
        while(current.left != None):
            if (encodedBitsArray[i]): current = current.right
            else: current = current.left
            i+=1
            progressbar.next()
        #if current node is a leaf node
        if (current.symbol != None): symbol = current.symbol
        #if current node is a leaf node
        else:  symbol, i = EnDeCodeASymbol.Decode(e,r,encodedBitsArray,i)

        #append the decoded symbol to array and update tree
        decodedArray.append(symbol)
        AHM_Tree.UpdateProcedure(symbol, current)
    return numpy.asarray(decodedArray).reshape(shape).astype(numpy.uint8)