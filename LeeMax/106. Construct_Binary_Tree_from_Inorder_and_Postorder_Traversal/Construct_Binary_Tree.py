
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        tree_len = len(inorder)
        if tree_len == 0:
            return None

        index_inorder = {}
        for index,i in enumerate(inorder):
            index_inorder[i] = index

        def build_tree(start_i,end_p,lenth):
            print(inorder[start_i:start_i+lenth])
            print(postorder[end_p - lenth + 1:end_p+1])
            if lenth == 1:
                root = TreeNode(postorder[end_p])
                return root
            root = TreeNode(postorder[end_p])
            # find root.left
            left_index = index_inorder[root.val]
            if left_index > start_i:
                print('left')
                left = build_tree(start_i,end_p - lenth + left_index - start_i,left_index - start_i)
                root.left = left
            if left_index < start_i + lenth - 1:
                print('right')
                right = build_tree(left_index+1, end_p-1, start_i + lenth - left_index -1)
                root.right = right

            return root

        root_0 = build_tree(0,tree_len - 1, tree_len)

        return root_0


if __name__ == '__main__':
    a = Solution()
    a.buildTree([9,3,15,20,7],[9,15,7,20,3])
