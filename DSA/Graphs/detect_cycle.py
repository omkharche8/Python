# Detect cycle in a graph

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True   # Mark the visited node true
        recStack[v] = True  # Mark the same node true in the stack also

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack):  # If a neighbor hasn't been visited, it calls isCyclicUtil recursively on the neighbor.
                    return True
            elif recStack[neighbour]:  # If a neighbor is in the recursion stack (recStack[neighbour] == True), it indicates a cycle.
                return True

            recStack[v] = False
            return False

    def isCycle(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack):
                    return True
        return False

if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    if g.isCycle() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")