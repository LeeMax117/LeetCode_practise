class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        start = False
        ind1, ind2, total, inmax = -1, -1, 0, 0
        for i in range(len(S)):
            if not start:
                if S[i] == '1':
                    start, total, inmax, ind1 = True, -1, -1, i
            else:
                if S[i] == '1':
                    total += -1
                else:
                    total += 1
                if total > inmax:
                    inmax, ind2 = total, i
        if inmax > 0:
            dist = ind2 - ind1 + 1
            m = (dist - inmax) // 2
            n = (len(S) - ind2 - 1 - inmax + total) // 2
            return m + n
        elif ind1 >= 0:
            dist = len(S) - ind1
            m = (dist + total) // 2
            return m
        return 0
