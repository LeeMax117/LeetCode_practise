class Solution:
    def gameOfLife(self, board):
        # L to record last line updated
        L = [0] * len(board[0])
        # the last position for L record the left up conern
        L.append(0)

        for i,line in enumerate(board):
            for j,cell in enumerate(line):
                # sum the live cell around
                if j == 0 and j < len(line) - 1:
                    sum_1 = L[j] + L[j+1]
                    if i < len(board) - 1:
                        sum_2 = board[i][j+1] + board[i+1][j] + board[i+1][j+1]
                    else:
                        sum_2 = board[i][j+1]
                elif j < len(line) - 1:
                    sum_1 = L[j-1] + L[j] + L[j+1] + L[-1]
                    if i < len(board) - 1:
                        sum_2 = board[i][j+1] + board[i+1][j-1] + board[i+1][j] + board[i+1][j+1]
                    else:
                        sum_2 = board[i][j+1]
                else:
                    sum_1 = L[j-1] + L[j] + L[-1]
                    if i < len(board) - 1:
                        sum_2 = board[i+1][j-1] + board[i+1][j]
                    else:
                        sum_2 = 0

                sum_live = sum_1 + sum_2
                L[-1] = L[j]
                L[j] = cell
                if (sum_live < 2 or sum_live > 3) and cell == 1: board[i][j] = 0
                if sum_live == 3 and cell == 0: board[i][j] = 1
                # print('(%s,%s),sum_1 = %s,sum_2 = %s'%(i,j,sum_1,sum_2))

if __name__ == "__main__":

    input = [[0]]
    a = Solution()
    a.gameOfLife(input)
    print(input)
