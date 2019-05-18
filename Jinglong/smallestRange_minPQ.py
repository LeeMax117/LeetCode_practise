import queue
class Node(object):
    def __init__(self, value, position):
        self.val = value
        self.pos = position
    def __lt__(self, other):
        return self.val < other.val
    def __str__(self):
        return 'value: ' + str(self.val) + ', position: ' + str(self.pos)
    def getInfo(self):
        return (self.val, self.pos)

class Solution:
    
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minpq = queue.PriorityQueue()
        left, right = 0, 0
        imin, imax, inmin, inmax = nums[0][0], -1, 0, 0
        lst = [-1] * len(nums)
        cur = [0] * len(nums)
        for i, line in enumerate(nums):
            lst[i] = line[0]
            if imin > lst[i]: imin, inmin = lst[i], i
            if imax < lst[i]: imax, inmax = lst[i], i
            minpq.put(Node(line[0], i))
        minpq.get()
        left, right = imin, imax
        while(True):
            if imax - imin < right - left:
                left, right = imin, imax
            cur[inmin] += 1
            if cur[inmin] >= len(nums[inmin]): break
            lst[inmin] = nums[inmin][cur[inmin]]
            if imax < lst[inmin]: imax, inmax = lst[inmin], inmin
            minpq.put(Node(lst[inmin], inmin))
            imin, inmin = minpq.get().getInfo()
        return [left, right]
