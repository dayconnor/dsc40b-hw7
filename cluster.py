from collections import deque
import dsc40graph

def cluster(graph, weights, level):
    visited = set()
    clusters = []
    
    def bfs(start):
        cluster = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            cluster.add(node)
            
            for neighbor in graph.neighbors(node):
                if neighbor not in visited and weights(node, neighbor) >= level:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return frozenset(cluster)
        
    for node in graph.nodes:
        if node not in visited:
            clusters.append(bfs(node))
        
    return frozenset(clusters)

# g = dsc40graph.UndirectedGraph()
# g.add_edge('a', 'b')
# g.add_edge('b', 'c')
# g.add_edge('c', 'd')
# g.add_edge('a', 'd')

# def weights(x, y):
#     x, y = (x, y) if x < y else (y, x)
#     return {('a', 'b'):1, ('b', 'c'):0.3, ('c', 'd'):0.9, ('a', 'd'):0.2}[(x, y)]

# print(cluster(g, weights, 0.4))