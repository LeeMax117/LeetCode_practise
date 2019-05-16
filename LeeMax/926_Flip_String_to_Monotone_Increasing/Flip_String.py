class Solution:
    def minFlipsMonoIncr(self, S):
        flip = S.count('0')
        total = flip
        count = 0
        min_flip = flip
        for i in S:
            if count == total:
                break
            if i == '1':
                flip += 1
            elif i == '0':
                flip -= 1
                count += 1

            if flip < min_flip:
                min_flip = flip

        return min_flip

if __name__ == "__main__":
    a = Solution()
    print(a.minFlipsMonoIncr('010110'))
