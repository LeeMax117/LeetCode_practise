class Solution:
    def generateParenthesis(self, n):
        def iteration(n):
            if n == 0:
                return []
            if n == 1:
                return ['()']

            ans = ['('+ k +')' for k in self.generateParenthesis(n-1)]

            return ans

        if n == 0:
            return []
        if n == 1:
            return ['()']

        total = ['('+ k +')' for k in self.generateParenthesis(n-1)]
        for i in range(1,n):
            total.extend([l + k for k in self.generateParenthesis(i) for l in iteration(n-i)])

        return total

if __name__ == "__main__":
    a = Solution()
    print(a.generateParenthesis(4))
    print(len(a.generateParenthesis(4)))
    print(len(set(a.generateParenthesis(4))))