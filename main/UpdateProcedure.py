import numpy
''''
to understand the algorithm 
    B1: see diagram page 59 in "Introduction to DATA COMPRESSION - third edition - author: khalid-sayood"
    B2: read __init__ function
    B3: read UpdateProcedure() function
'''
class AdaptiveHuffmanTree:
# not yet transmitted node (weight = 0, number is min)
    NYT = None 
# Save the symbols that were transmitted
    SymbolsTransmited = {}
    AllNode = []
#init the tree (root node ~ parent = None, symbol = None)
    def __init__(self, number, parent = None, symbol = None):
        AdaptiveHuffmanTree.NYT = self
        self.right = self.left = None
        self.parent = parent
        self.symbol = symbol
        self.number = number
        self.weight = 0
        AdaptiveHuffmanTree.AllNode.append(self)
#refresh the SymbolsTransmited dict
    def refresh(self):
        AdaptiveHuffmanTree.SymbolsTransmited = {}
        AdaptiveHuffmanTree.AllNode = []
#swap the current node with the max number node in block (block contains node with the same weight)
    def SwapNode(self, current):
        if(current != self):
            maxNumberNode = current
#find node has max number in blocks (blocks contain nodes which have the same weight)
            for node in AdaptiveHuffmanTree.AllNode:
                if(node.weight == current.weight and node.number > maxNumberNode.number and node != current.parent):
                    maxNumberNode = node
#swap two node
            if(maxNumberNode != current):
                maxNumberNode_parent = maxNumberNode.parent
                current_parent = current.parent
                maxNumberNode.number, current.number = current.number, maxNumberNode.number
                if(maxNumberNode_parent == current_parent):
                    current_parent.left, current_parent.right = maxNumberNode, current
                else:
                    if(current_parent.left == current):
                        current_parent.left = maxNumberNode
                    else:
                        current_parent.right = maxNumberNode
                    maxNumberNode.parent = current_parent

                    if(maxNumberNode_parent.left == maxNumberNode):
                        maxNumberNode_parent.left = current
                    else:
                        maxNumberNode_parent.right = current
                    current.parent = maxNumberNode_parent

#UpdateProcedure function
    def UpdateProcedure(self, symbol, current = None):
        # If first appearance for symbol
        if(AdaptiveHuffmanTree.SymbolsTransmited.get(symbol) == None):
            #current <- NYT
            current = AdaptiveHuffmanTree.NYT
            #NYT node gives birth to new NYT and external node
            current.right = AdaptiveHuffmanTree(current.number - 1, current, symbol)
            current.left = AdaptiveHuffmanTree(current.number - 2, current) # new NYT node
            #Increment weight of external node and old NYT node
            current.right.weight+=1 #external node
            current.weight+=1 #old NYT node
            #Sign the symbols had been transmited by an array
            AdaptiveHuffmanTree.SymbolsTransmited[symbol] = current.right
        # If symbol had been appeared before
        else:
            # swap (if not max in block) -> Increment weight node
            self.SwapNode(current)
            current.weight+=1
        # if not root -> go to parent node -> swap (if not max in block) -> Increment weight node
        while (current != self):
            current = current.parent
            self.SwapNode(current)
            current.weight+=1
# traver the tree in pre-order to test
    def PreOrderTraversal(self):
        #print(self.number, self.weight, self.symbol)
        if(self.left != None): 
            self.left.PreOrderTraversal()
        if(self.right != None): 
            self.right.PreOrderTraversal() 