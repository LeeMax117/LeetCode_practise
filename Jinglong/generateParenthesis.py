class Solution:
    size = 0
    res_lst = []
    def DFS(self, left, right, s):
        if len(s) == self.size * 2:
            self.res_lst.append(s)
            return
        if left < self.size:
            self.DFS(left + 1, right, s + '(')
        if left > right:
            self.DFS(left, right + 1, s + ')')
        return

    def generateParenthesis(self, n: int) -> List[str]:
        self.res_lst = []
        self.size = n
        self.DFS(0, 0, '')
        return self.res_lst
