# Doing classic Breadth first search, this case we go to the levels of the node before going deep

from collections import deque


def bfs(adjList, startNode, visited):
    # A queue for the BFS
    q = deque()

    # Mark the current node as visited as you pass it and push(enqueue) it
    visited[startNode] = True
    q.append(startNode)

    # Iterate over the queue
    while q:
        # pop (dequeue) this vertex and print it
        currentNode = q.popleft()
        print(currentNode, end=" ")

        for neighbour in adjList[currentNode]:  # Now see for the connected node to the current node
            if not visited[neighbour]:  # if it's not visited
                visited[neighbour] = True  # just mark it true
                q.append(neighbour)  # Append that also travelled


# Add an edge to the graph
def addEdge(adjList, u, v):
    adjList[u].append(v)

def main():
    # define number of vertices
    vertices = 5

    adjList = [[] for _ in range(vertices)]

    #Add edges
    addEdge(adjList, 0,1)
    addEdge(adjList, 0,2)
    addEdge(adjList, 1,3)
    addEdge(adjList, 0,4)
    addEdge(adjList, 2,4)

    visited = [False] * vertices

    bfs(adjList, 0, visited)

if __name__ == "__main__":
    main()