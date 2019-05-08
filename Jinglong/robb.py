# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # below two dicts used to store the current node's max value
    # to avoid duplicated computing.
    node_dict1 = {}
    node_dict2 = {}
    def robb(self, current: TreeNode, parent_chk: bool) -> int:
        val = 0
        if parent_chk:
            if current is not None:
                if current in self.node_dict1:
                    return self.node_dict1[current]
                val = self.robb(current.left, False) + self.robb(current.right, False)
                self.node_dict1[current] = val
            else:
                val = 0
        else:
            if current is not None:
                if current in self.node_dict2:
                    return self.node_dict2[current]
                val = max(current.val + self.robb(current.left, True) + self.robb(current.right, True), self.robb(current.left, False) + self.robb(current.right, False))
                self.node_dict2[current] = val
            else:
                val = 0
        return val
    def rob(self, root: TreeNode) -> int:
        if root is not None:
            return max(root.val + self.robb(root.left, True) + self.robb(root.right, True), self.robb(root.left, False) + self.robb(root.right, False))
        else:
            return 0
