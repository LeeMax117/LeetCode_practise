class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))
        print(parent)
        ans = []
        for i, j in edges:
            p, q = i, j
            print(p,q)
            while p != parent[p]:
                print('p = %d, parent[p] = %d'%(p,parent[p]))
                p = parent[p]
            while q != parent[q]:
                print('q = %d, parent[q] = %d' % (q, parent[q]))
                q = parent[q]
            if p == q:
                ans = [i, j]
            else:
                parent[q] = p
        return ans

if __name__ == "__main__":
    a = Solution()
    print(a.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))