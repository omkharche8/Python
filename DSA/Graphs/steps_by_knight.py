# Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.
#
# Note:
# The initial and the target position coordinates of Knight have been given according to 1-base indexing


# Input:
# N=6
# knightPos[ ] = {4, 5}
# targetPos[ ] = {1, 1}
# Output:
# 3

from collections import deque


class Solution:

    # Function to check if a position is valid
    def isValid(self, x, y, N):
        return 0 <= x < N and 0 <= y < N

        # Function to find out minimum steps Knight needs to reach target position.
        def minStepToReachTarget(self, KnightPos, TargetPos, N):
            directions = [
                (-2, -1), (-1, -2), (1, -2), (2, -1),
                (2, 1), (1, 2), (-1, 2), (-2, 1)
            ]

            board = [[0] * N for _ in range(N)]

            # Converting the indexes
            KnightPos = (KnightPos[0] - 1, KnightPos[1] - 1)
            TargetPos = (TargetPos[0] - 1, TargetPos[1] - 1)

            queue = deque([(KnightPos[0], KnightPos[1], 0)])

            visited = set()
            visited.add(KnightPos[0], KnightPos[1])

            while queue:
                x, y, steps = queue.popleft()

                if (x, y) == TargetPos:
                    return steps

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if self.isValid(nx, ny, N) and (nx, ny) not in visited:
                        visited.add(nx, ny)
                        queue.append(nx, ny, steps + 1)
            return -1
