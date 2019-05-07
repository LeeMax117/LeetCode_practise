class Solution:
    def descartes(self, l1: list, l2: list) -> List[str]:
        return [a+b for a in l1 for b in l2]
    def letterCombinations(self, digits: str) -> List[str]:
        ind_list = [None, None, ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
               ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'],
               ['w', 'x', 'y', 'z']]
        out_list = []
        for ind in digits:
            lst = ind_list[int(ind)]
            if len(out_list) == 0:
                out_list = lst
            else:
                out_list = self.descartes(out_list, lst)
        return out_list