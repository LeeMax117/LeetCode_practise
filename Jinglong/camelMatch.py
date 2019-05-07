class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        out_list = []
        l2 = len(pattern)
        for query in queries:
            l1 = len(query)
            cnt = 0
            flag = True
            for i in range(l1):
                if cnt < l2:
                    if query[i] > 'Z' and query[i] != pattern[cnt]:
                        continue
                    elif query[i] < 'a' and query[i] != pattern[cnt]:
                        flag = False
                        break
                    cnt = cnt + 1
                else:
                    if query[i] < 'a':
                        flag = False
                        break
            out_list.append(cnt == l2 and flag)
        return out_list