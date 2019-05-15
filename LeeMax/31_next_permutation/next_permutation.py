class Solution:
    def nextPermutation(self, nums):
        bp = -1
        try:
            while nums[bp-1] >= nums[bp]:
                    bp -= 1
            else:
                t = bp - 1
                bp = -1
                while nums[t] >= nums[bp]:
                    bp -= 1
                else:
                    nums[t],nums[bp] = nums[bp] ,nums[t]
                    nums[t+1:] = nums[len(nums)-1:t:-1]
        except IndexError:
            nums.sort()

if __name__ == "__main__":
    a = Solution()
    input = [3,2,1]
    a.nextPermutation(input)
    print(input)