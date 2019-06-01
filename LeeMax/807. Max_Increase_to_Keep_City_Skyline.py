class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        i_max = []
        j_max = []
        i_num = len(grid)
        j_num = len(grid[0])

        for line in grid:
            i_max.append(max(line))

        for i in range(j_num):
            j_max.append(max([grid[x][i] for x in range(i_num)]))

        num_add = 0
        for i in range(i_num):
            for j in range(j_num):
                num_add += min(i_max[i],j_max[j]) - grid[i][j]

        return num_add

if __name__ =='__main__':
    a = Solution()
    print(a.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))