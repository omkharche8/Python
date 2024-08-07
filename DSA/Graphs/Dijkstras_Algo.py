# Classic implementation

import heapq

class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u, v, w):  # U is the one node, V is another, W is the weight
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def shortestpath(self, src):
        pq = []
        heapq.heappush(pq, (0, src))
        dist = [float('inf')] * self.V
        dist[src] = 0

        while pq:
            d, u = heapq.heappop(pq)  # d is the smallest dist
            for v, weight in self.adj[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")


if __name__ == "__main__":
    V = 9
    g = Graph(V)

    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)

    g.shortestpath(0)
