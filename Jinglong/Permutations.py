class Solution:
    def permutes(self, num, out):
        tmp = []
        print(out)
        for lst in out:
            for i in range(len(lst)+1):
                tmp.append(lst[:i]+[num]+lst[i:])
        return tmp
    def permute(self, nums: List[int]) -> List[List[int]]:
        out_lst = []
        for num in nums:
            if len(out_lst) == 0:
                out_lst.append([num])
            else:
                out_lst = self.permutes(num, out_lst)
        return out_lst
