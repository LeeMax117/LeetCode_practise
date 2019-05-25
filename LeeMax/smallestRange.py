from heapq import heappush,heappop
class Node(object):
    def __init__(self,value,i,j):
        self.value = value
        self.i = i
        self.j = j

    def __lt__(self,other):
        return self.value < other.value

class Solution:
    def smallestRange(self, nums):
        record = []
        tmp_max = nums[0][0]
        for index,num in enumerate(nums):
            if num[0] > tmp_max:
                tmp_max = num[0]
            heappush(record,Node(num[0],index,0))

        tmp_node = heappop(record)
        tmp_min = tmp_node.value
        min_range = [tmp_min, tmp_max]
        min_range_value = min_range[1] - min_range[0]

        while True:
            next_index_0 = tmp_node.i
            next_index_1 = tmp_node.j + 1
            try:
                next_value = nums[next_index_0][next_index_1]
            except IndexError:
                break
            if next_value > tmp_max:
                tmp_max = next_value

            heappush(record,Node(next_value,next_index_0,next_index_1))
            tmp_node = heappop(record)
            tmp_min = tmp_node.value

            tmp = [tmp_min,tmp_max]
            tmp_value = tmp[1] - tmp[0]
            if tmp_value < min_range_value:
                min_range = tmp
                min_range_value = tmp_value

        return min_range

if __name__ == '__main__':
    a = Solution()
    print(a.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))