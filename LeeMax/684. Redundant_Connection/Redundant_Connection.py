class Solution:
    def findRedundantConnection(self, edges):
        def del_one_edge_node(graph):
            nodes_count = {}
            for edge in graph:
                for i in edge:
                    if i in nodes_count:
                        nodes_count[i] += 1
                    else:
                        nodes_count[i] = 1
            node_to_del = []
            for node in nodes_count:
                if nodes_count[node] == 1:
                    node_to_del.append(node)

            edge_to_remove = []
            for node in node_to_del:
                for edge in graph:
                    if node in edge:
                        edge_to_remove.append(edge)

            for edge in edge_to_remove:
                graph.remove(edge)

            return edge_to_remove

        while del_one_edge_node(edges) != []:
            pass
        return edges[-1]

if __name__ == "__main__":
    a = Solution()
    print(a.findRedundantConnection([[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]))