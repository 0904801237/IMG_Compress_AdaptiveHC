import UpdateProcedure as UpdateProcedure
import EnDeCodeASymbol as EnDeCodeASymbol
import math

#find and return the external node and road from root to it
def FindExternalNode(externalNode):
    road = ""
    current = externalNode
    while(current.parent != None):
        if(current.parent.left == current): 
            road += "0"
        else:
            road += "1"
        current = current.parent
        print(current.number)
    return road[::-1]
#find and return the road from root to the NYT node

def EncodeProcedure(inputSourceSize, symbols) :
    '''
    @param: inputSourceSize : # the total leafs ~ total size of source
    @param: symbols : the symbol string that need to encode
    @return: encodedString : the binary string encoded from the input
    '''
    [e, r] = EnDeCodeASymbol.FindER(inputSourceSize)
    # the total nodes
    totalNodes = 2*inputSourceSize - 1 
    # create a tree with only one node (NYT)
    AHM_Tree = UpdateProcedure.AdaptiveHuffmanTree(totalNodes)
    AHM_Tree.refresh()
    # the binary string encoded from the input
    encodedString = ""
    for s in symbols :
        # if s have not been transmited yet
        externalNode = AHM_Tree.SymbolsTransmited.get(s) 
        if(externalNode == None):
            #find road to NYT node
            roadToNYT = FindExternalNode(UpdateProcedure.AdaptiveHuffmanTree.NYT)
            encodedString +=  (roadToNYT + EnDeCodeASymbol.Encode(e, r, s))
            AHM_Tree.UpdateProcedure(s)
        else: # if s have been transmited yet
            #find external node and road to it
            roadToExternalNode = FindExternalNode(externalNode)
            encodedString += roadToExternalNode
            AHM_Tree.UpdateProcedure(s, externalNode)
    AHM_Tree.PreOrderTraversal()
    # for i in AHM_Tree.AllNode:
    #     print(i.number)
    return encodedString

