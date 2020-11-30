import UpdateProcedure as UpdateProcedure
import EnDeCodeASymbol as EnDeCodeASymbol
import math
import bitarray
import numpy
    
def DecodeProcedure(inputSourceSize, encodedBitsArray, imgWeight) :
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
    #convert encodedString to an array
    #encodedBitsArray = list(encodedString)

    while (len(encodedBitsArray) != 0):
        current = AHM_Tree
        #if current is not an external node (leaf node) -> read next bit
        #print(len(encodedBitsArray))
        while(current.left):
            current = current.right if encodedBitsArray.pop(0) else current.left
        #if current node is a leaf node
        if (current.symbol): symbol = current.symbol
        #if current node is a leaf node
        else: symbol = EnDeCodeASymbol.Decode(e,r,encodedBitsArray)
        #append the decoded symbol to array and update tree
        decodedArray.append(symbol)
        AHM_Tree.UpdateProcedure(symbol, current)
    img = []
    while(decodedArray != []):
        row = []
        for i in range(imgWeight):
            pixel = []
            for j in range(4):
                pixel.append(decodedArray.pop(0))
            row.append(pixel)
        img.append(row)
    return img