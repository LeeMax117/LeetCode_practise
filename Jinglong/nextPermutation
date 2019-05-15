class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the last ascending pair numbers
        # replace the the first number a of ascending pair with the smaller but larger than a number from following descending list numbers
        # then reverse the following descending sub list.
        findi, imin, index = -1, -1, -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                findi = i - 1
                imin = nums[i]
                index = i
            elif imin >= nums[i] and nums[i] > nums[findi]:
                index = i
                imin = nums[i]
        if findi != -1 and index != -1:
            nums[findi], nums[index] = nums[index], nums[findi]
        start, end = findi + 1, len(nums) - 1
        while end > start: 
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
