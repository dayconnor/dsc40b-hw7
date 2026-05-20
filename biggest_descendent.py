# import dsc40graph

def biggest_descendent(graph, root, value):
    biggest = {}
    
    def dfs(node):
        if len(list(graph.neighbors(node))) == 0:   # Base
            biggest[node] = value[node]
            return
        
        node_values = [value[node]]
        
        for child in graph.neighbors(node):         # Recursive
            dfs(child)
            node_values.append(biggest[child])
        
        biggest[node] = max(node_values)
    
    dfs(root)
    return biggest
        
# edges = [(1,2), (1,3), (2,4), (2,5), (4,8), (4,9), (3,6), (3,7)]
# g = dsc40graph.DirectedGraph()
# for edge in edges: g.add_edge(*edge)
# value = {1:2, 2:1, 3:4, 4:8, 5:5, 6:2, 7:10, 8:3, 9:9}

# print(biggest_descendent(g, 1, value))