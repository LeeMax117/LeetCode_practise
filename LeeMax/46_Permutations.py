class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        ans = []
        for num in nums:
            nums_copy = nums[:]
            nums_copy.remove(num)
            k = self.permute(nums_copy)
            for i in k:
                i.insert(0,num)
            ans.extend(k)

        return ans

if __name__ == '__main__':
    a = Solution()
    print(a.permute([1,2,3]))
