# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        else:
            rv = postorder[-1]
            ind = inorder.index(rv)
            tn = TreeNode(rv)
            tn.left = self.buildTree(inorder[:ind], postorder[:ind])
            tn.right = self.buildTree(inorder[ind+1:], postorder[ind:len(postorder)-1])
            return tn
