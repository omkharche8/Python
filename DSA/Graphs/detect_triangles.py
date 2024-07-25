# Input is a matrix

def triangle(graph, isDirected):
    nodes = len(graph)
    count = 0

    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):

                if(graph[i][j] and graph[j][k] and graph[k][i]):
                    count += 1

    if isDirected:
        return count//3
    else:
        return count//6

graph = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [0, 1, 1, 0]]
# Create adjacency matrix of a directed graph
digraph = [[0, 0, 1, 0],
           [1, 0, 0, 1],
           [0, 1, 0, 0],
           [0, 0, 1, 0]]
print("The Number of triangles in undirected graph : %d" %
      triangle(graph, False))

print("The Number of triangles in directed graph : %d" %
      triangle(digraph, True))