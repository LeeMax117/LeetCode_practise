class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max = 0
        ignore_dict = {}
        for ind in range(len(s)):
            if s[ind] in ignore_dict:
                ignore_dict[s[ind]].append(ind)
            else:
                ignore_dict[s[ind]] = [ind]
        ind_lst = [-1, len(s)]
        for lst in ignore_dict.values():
            if len(lst) < k:
                ind_lst.extend(lst)
        if len(ind_lst) == 2:
            return len(s)
        ind_lst.sort()
        for ind in range(1, len(ind_lst)):
            temp1 = ind_lst[ind-1]
            temp2 = ind_lst[ind]
            if temp2 - temp1 - 1 < k:
                continue
            else:
                res = self.longestSubstring(s[temp1+1:temp2], k)
                if res > max:
                    max = res
        return max
