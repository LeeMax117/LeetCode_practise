class Solution:      
    min_lst = []
    def insert(self, that):
        low, high = 0, len(self.min_lst)
        mid = (low + high) //2
        while(mid < high):
            this = self.min_lst[mid]
            if this[0] == that[0]:
                self.min_lst.insert(mid, that)
                return
            elif this[0] > that[0]: high = mid
            elif this[0] < that[0]: low = mid + 1
            mid = (low + high) // 2
        self.min_lst.insert(mid, that)
        return
    def getmin(self):
        return self.min_lst.pop(0)
            
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        left, right = 0, 0
        imin, imax, inmin, inmax = nums[0][0], -1, 0, 0
        lst = [-1] * len(nums)
        cur = [0] * len(nums)
        for i, line in enumerate(nums):
            lst[i] = line[0]
            if imin > lst[i]: imin, inmin = lst[i], i
            if imax < lst[i]: imax, inmax = lst[i], i
            self.insert((lst[i], i))
        self.min_lst.pop(0)
        left, right = imin, imax
        while(True):
            if imax - imin < right - left:
                left, right = imin, imax
            print("inmin:" + str(inmin))
            cur[inmin] += 1
            print(inmin, cur[inmin])
            if cur[inmin] >= len(nums[inmin]): break
            lst[inmin] = nums[inmin][cur[inmin]]
            if imax < lst[inmin]: imax, inmax = lst[inmin], inmin
            self.insert((lst[inmin], inmin))
            imin, inmin = self.getmin()
        return [left, right]
