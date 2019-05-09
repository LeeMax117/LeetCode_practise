# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # record the value for tree avoid duplate calculate
        self.root_dict = {}
        self.count = 0

    def rob(self, root):
        self.count += 1
        if root == None:
            return 0
        elif self.root_dict.get(id(root)):
            return self.root_dict.get(id(root))

        x_root = root.val + self.rob_no_root(root.left) + self.rob_no_root(root.right)
        x_left = self.rob(root.left)
        if x_root <= x_left :
            root_value = self.rob(root.left) + self.rob(root.right)
            self.root_dict[id(root)] = root_value
            return root_value
        else:
            x_no_root = x_left + self.rob(root.right)
            root_value = max(x_root,x_no_root)
            return root_value

    def rob_no_root(self,root):
        if root== None:
            return 0
        else:
            root_left_value = self.rob(root.left)
            root_right_value = self.rob(root.right)
            self.root_dict[id(root.left)] = root_left_value
            self.root_dict[id(root.right)] = root_right_value
            root_value = root_left_value + root_right_value

            return root_value


if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(4)
    c = TreeNode(5)
    b1 = TreeNode(1)
    b2 = TreeNode(3)
    c2 = TreeNode(1)
    a.left = b
    a.right = c
    b.left = b1
    b.right = b2
    c.right = c2
    x = Solution()
    print(x.rob(a))
    print(x.count)
    print(x.root_dict)