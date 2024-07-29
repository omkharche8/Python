# Initialize distance array dist[] for each vertex ‘v‘ as dist[v] = INFINITY.
# Assume any vertex (let’s say ‘0’) as source and assign dist = 0.
# Relax all the edges(u,v,weight) N-1 times as per the below condition:
# dist[v] = minimum(dist[v], distance[u] + weight)
# Now, Relax all the edges one more time i.e. the Nth time and based on the below two cases we can detect the negative cycle:
# Case 1 (Negative cycle exists): For any edge(u, v, weight), if dist[u] + weight < dist[v]
# Case 2 (No Negative cycle) : case 1 fails for all the edges.


# Given a directed weighted graph, the task is to find whether the given graph contains any negative-weight cycle or not.
#
# Note: A negative-weight cycle is a cycle in a graph whose edges sum to a negative value.


# Bellman Ford


def isNegCycle(src, dist):
    global graph, V, E  # Vertices and Edges

    for i in range(V):
        dist[i] == 10 ** 18
    dist[src] = 0

    for i in range(1, V):
        for j in range(E):
            u = graph[j][0]
            v = graph[j][1]
            weight = graph[j][2]
            if dist[u] != 10 and dist[u] + weight < dist[v]:
                dist[v] = weight + dist[u]
    # Checking for negative cycles now
    for i in range(E):
        u = graph[i][0]
        v = graph[i][1]
        weight = graph[i][2]
        if dist[u] != 10 ** 18 and dist[u] + weight < dist[v]:
            return True
    return False


def isNegCycleDisconnected():
    global V, E, graph

    visited = [0] * V

    dist = [0] * V  # This array is filled with Bellman Ford Array

    for i in range(V):
        if visited[i] == 0:

            # if cycle
            if isNegCycle(i, dist):
                return True
            for i in range(V):
                if dist[i] != 10 ** 18:
                    visited[i] = True
    return False


if __name__ == '__main__':

    # /* Let us create the graph given in above example */
    V = 5  # Number of vertices in graph
    E = 8  # Number of edges in graph
    graph = [[0, 0, 0] for i in range(8)]

    # add edge 0-1 (or A-B in above figure)
    graph[0][0] = 0
    graph[0][1] = 1
    graph[0][2] = -1

    # add edge 0-2 (or A-C in above figure)
    graph[1][0] = 0
    graph[1][1] = 2
    graph[1][2] = 4

    # add edge 1-2 (or B-C in above figure)
    graph[2][0] = 1
    graph[2][1] = 2
    graph[2][2] = 3

    # add edge 1-3 (or B-D in above figure)
    graph[3][0] = 1
    graph[3][1] = 3
    graph[3][2] = 2

    # add edge 1-4 (or A-E in above figure)
    graph[4][0] = 1
    graph[4][1] = 4
    graph[4][2] = 2

    # add edge 3-2 (or D-C in above figure)
    graph[5][0] = 3
    graph[5][1] = 2
    graph[5][2] = 5

    # add edge 3-1 (or D-B in above figure)
    graph[6][0] = 3
    graph[6][1] = 1
    graph[6][2] = 1

    # add edge 4-3 (or E-D in above figure)
    graph[7][0] = 4
    graph[7][1] = 3
    graph[7][2] = -3

    if isNegCycleDisconnected():
        print("Yes")
    else:
        print("No")
