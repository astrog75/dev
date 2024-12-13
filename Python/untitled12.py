# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:09:23 2022

@author: moty_
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node_6 = TreeNode(7, None, None)
node_7 = TreeNode(2, None, None)
node_4 = TreeNode(13, None, None)
node_8 = TreeNode(1, None, None)

node_3 = TreeNode(11, node_6, node_7)
node_5 = TreeNode(4, None, node_8)

node_1 = TreeNode(4, node_3, None)
node_2 = TreeNode(8, node_4, node_5)

node_0 = TreeNode(5, node_1, node_2)   # root



def hasPathSum(root: TreeNode, targetSum: int) -> bool:
 

    nodesToCheck = [root]   # Stack of nodes to be checked
    pathSum = 0
    
    while nodesToCheck != []:
        
        currentNode = nodesToCheck[0]  # Retrieve the last element in the stack
        nodesChecked = []
        
        print(currentNode.val)
        
        del nodesToCheck[0]
        
        pathSum += currentNode.val
        
        if currentNode.left == None and currentNode.right == None:
            
            if pathSum == targetSum:
                
                return True
            
            else:
                
                nodesChecked.append(currentNode)
                
                nodesToCheck.insert(0, root)
                
                pathSum = 0
                
                
        
        else:
            
            if currentNode.right != None and currentNode.right not in nodesChecked:
                
                nodesToCheck.insert(0, currentNode.right)
            
            if currentNode.left != None and currentNode.right not in nodesChecked:
                
                nodesToCheck.insert(0, currentNode.left)
                
    return None


print(hasPathSum(node_0, 18))
            