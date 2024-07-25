# Using Kahn's Algorithm to detect cycle in a DAG
# Basically the algorithm removes all the vertices from the graph and if it is successful to do so then there is no cycles in the graph
# But if there are vertices with degrees more than 0 then it means it has least one cycle


from collections import deque


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def isCyclic(self):
        inDegree = [0] * self.V
        q = deque()
        visited = 0

        # Calculating the indegree of each vertex
        for u in range(self.V):
            for v in self.adj[u]:
                inDegree[v] += 1

        # Enqueue vertices with 0 indegree
        for u in range(self.V):
            if inDegree[u] == 0:
                q.append(u)

        # Do BFS
        while q:
            u = q.popleft()
            visited += 1

            # Reduce in-degree of adjacent vertices
            for v in self.adj[u]:
                inDegree[v] -= 1
                # If the inDegree becomes 0 then push (enqueue) the vertex
                if inDegree[v] == 0:
                    q.append(v)

        return visited != self.V


if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(4, 5)
    g.addEdge(5, 3)

    if g.isCyclic():
        print("Cycle exists")
    else:
        print("No cycle")
