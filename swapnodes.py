import math
from collections import deque

"""Perform a series of swaps on a binary tree
    provided via level-order-like traversal"""

class Node:
    def __init__(self, val, depth):
        self.val = val
        self.depth = depth
        self.left = None
        self.right = None
        
    def addChildren(self, val1, val2):
        #find correct node to add to
        children = deque()
        children.append(self)
        while(children):
            cur = children.popleft()
            #if no children, just add them to this node
            if(not cur.left and not cur.right):
                cur.left = Node(val1, cur.depth + 1)
                cur.right = Node(val2, cur.depth + 1)
                return True
            if(cur.left and cur.left.val > 0):
                children.append(cur.left)
            if(cur.right and cur.right.val > 0):
                children.append(cur.right)
        return False
        
    def swapChildren(self, depth):
        if(self.left):
            self.left.swapChildren(depth)
        if(self.right):
            self.right.swapChildren(depth)
        if(not self.depth % depth):
            self.left, self.right = self.right, self.left
        
    def getHeight(self):
        if(self.val < 0):
            return self.depth - 1
        return max(self.left.getHeight(), self.right.getHeight())
        
    def __str__(self):
        ans = ""
        if(self.val < 0):
            return ans
        if(self.left):
            ans += str(self.left)
        ans += str(self.val) + " "
        if(self.right):
            ans += str(self.right)
        return ans
        
def swapNodesT(indexes, queries):
    #Build tree
    root = Node(1, 1)
    for x in range(0, len(indexes), 2):
        root.addChildren(indexes[x], indexes[x+1])
        print(root)
    print(root, "\t<-- Starting tree")
    
    #Perform swaps
    #height = root.getHeight()
    for each in queries:
        root.swapChildren(each)
        print(root, "\t<-- Swapping level", each)
    
    #Traverse tree
    print(root, "\t<-- Final tree")
    print(root)

def swapNodesL(nodes, queries):
    #build the tree using list
    tree = [1]
    size = 1
    maxindx = max(nodes)
    for x in range(0, len(nodes), 2):
        while(tree[size//2] < 0):
            tree.append(-1)
            tree.append(-1)
            size += 2
        tree.append(nodes[x])
        tree.append(nodes[x+1])
        size += 2
        if(nodes[x] == maxindx or nodes[x+1] == maxindx):
            while(not math.log(size+1, 2).is_integer()):
                tree.append(-1)
                size += 1
            break
    
    #perform swaps
    height = math.log(size, 2)
    for depth in queries:
        curDepth = depth
        #while(depth < height):
            
    
    #return in-order traversal

def run():
    tests = [[[2,3,4,-1,5,-1,6,-1,7,8,-1,9,-1,-1,10,11,-1,-1,-1,-1,-1,-1],[2, 4]]]
    #actually not the format of input, so building ended up slightly modified
    
    for each in tests:
        print(swapNodesT(*each))
        #output format also had to be modified slightly