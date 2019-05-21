class Solution:
    graph_dict = None
    def connected(self, val1, val2):
        root1 = self.getroot(val1)
        root2 = self.getroot(val2)
        if  root1 == root2:
            return True
        else:
            self.graph_dict[root2] = root1
            return False

    def getroot(self, val):
        if val not in self.graph_dict:
            self.graph_dict[val] = val
            return val
        root = val
        while(root != self.graph_dict[root]):
            root = self.graph_dict[root]
        return root
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.graph_dict = {}
        for edge in edges:
            if self.connected(edge[0], edge[1]):
                return [edge[0], edge[1]]
