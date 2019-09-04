class BSTIterator:
    def _build_lst(self, node: TreeNode):
        lst = list()
        if node is None:
            return None
        left_lst = self._build_lst(node.left)
        if left_lst is not None:
            lst.extend(left_lst)
        lst.append(node.val)
        right_lst = self._build_lst(node.right)
        if right_lst is not None:
            lst.extend(right_lst)
        return lst

    def __init__(self, root: TreeNode):
        self.p_lst = self._build_lst(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.p_lst.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.p_lst is not None and len(self.p_lst) > 0
