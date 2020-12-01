import UpdateProcedure as UpdateProcedure
import EnDeCodeASymbol as EnDeCodeASymbol
import math
import bitarray
import numpy

#find and return the external node and road from root to it
def FindExternalNode(externalNode):
    road = bitarray.bitarray()
    current = externalNode
    while(current.parent != None):
        road.append(current.parent.right == current)
        current = current.parent
    return road[::-1]

def EncodeProcedure(inputSourceSize, symbols) :
    '''
    @param: inputSourceSize : # the total leafs ~ total size of source
    @param: symbols : the symbol string that need to encode
    @return: encodedBitArray : the binary string encoded from the input
    '''
    [e, r] = EnDeCodeASymbol.FindER(inputSourceSize)
    # the total nodes
    totalNodes = 2*inputSourceSize - 1 
    # create a tree with only one node (NYT)
    AHM_Tree = UpdateProcedure.AdaptiveHuffmanTree(totalNodes)
    AHM_Tree.refresh()
    # the binary string encoded from the input
    encodedBitArray = bitarray.bitarray()
    i = 0
    symbolsArray = symbols.reshape(1,symbols.size)[0]
    for s in symbolsArray:
        print(len(symbolsArray) - i)
        i += 1
        # if s have not been transmited yet
        externalNode = AHM_Tree.SymbolsTransmited.get(s) 
        if(externalNode == None):
            #find road to NYT node
            encodedBitArray +=  FindExternalNode(UpdateProcedure.AdaptiveHuffmanTree.NYT)
            encodedBitArray +=  EnDeCodeASymbol.Encode(e, r, s)
            AHM_Tree.UpdateProcedure(s)
        else: # if s have been transmited yet
            #find external node and road to it
            encodedBitArray += FindExternalNode(externalNode)
            AHM_Tree.UpdateProcedure(s, externalNode)
    #AHM_Tree.PreOrderTraversal()
    return encodedBitArray

