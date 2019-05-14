class Solution:
    def calculate(self, l, board, lst):
        temp = []
        last = 0
        for i in range(len(board[0])):
            s = 0
            temp.append(board[l][i])
            start_i = i - 1
            if start_i < 0: start_i = 0
            end_i = i + 2
            if end_i > len(board[0]): end_i = len(board[0])
            s += last + sum(board[l][i:end_i])
            if l+1 < len(board): s += sum(board[l+1][start_i:end_i])
            if lst is not None:
                s += sum(lst[start_i:end_i])
            s -= board[l][i]
            last = board[l][i]
            if s < 2 or s > 3:
                board[l][i] = 0
            elif s == 3:
                board[l][i] = 1
        return temp
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lst = None
        for i in range(len(board)):
            lst = self.calculate(i, board, lst)
        
