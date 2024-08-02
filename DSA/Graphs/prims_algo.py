# Prims  Algorithm
# Step 1: Determine an arbitrary vertex as the starting vertex of the MST.
# Step 2: Follow steps 3 to 5 till there are vertices that are not included in the MST (known as fringe vertex).
# Step 3: Find edges connecting any tree vertex with the fringe vertices.
# Step 4: Find the minimum among these edges.
# Step 5: Add the chosen edge to the MST if it does not form any cycle.
# Step 6: Return the MST and exit

import heapq


def prims_algorithm(graph):
    # Number of nodes in the graph
    n = len(graph)

    # Array to track visited nodes
    visited = [False] * n

    # Min-heap to select the edge with the smallest weight
    min_heap = [(0, 0)]  # (weight, node)

    # Variable to store the total weight of the minimum spanning tree (MST)
    total_weight = 0

    # Array to store the edges in the MST
    mst_edges = []

    while min_heap:
        weight, current_node = heapq.heappop(min_heap)

        # If the node is already visited, continue to the next iteration
        if visited[current_node]:
            continue

        # Mark the current node as visited
        visited[current_node] = True

        # Add the weight to the total weight of the MST
        total_weight += weight

        # Add the edge to the MST (except the starting node)
        if weight != 0:
            mst_edges.append((current_node, weight))

        # Iterate through the adjacent nodes
        for neighbor, weight in graph[current_node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight, neighbor))

    return total_weight, mst_edges


# Example usage
# Graph represented as an adjacency list
graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

total_weight, mst_edges = prims_algorithm(graph)
print("Total weight of the MST:", total_weight)
print("Edges in the MST:", mst_edges)
