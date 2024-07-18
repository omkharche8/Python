# Classical knights tour question on a 8X8 Chessboard

n = 8  #initial size of the chessboard


def isSafe(x, y, board):
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
        return True
    return False


def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solveKT(n):
    board = [[-1 for i in range(n)] for i in range(n)]  # The board initilalized with -1
    # move_x and move_y is the way the knight will move

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[0][0] = 0  # This is the place where the knight is initially at

    #counter
    pos = 1

    if (not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
        print("No solution")
    else:
        printSolution(n, board)


def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    if (pos == n ** 2):
        return True

    #now moving
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            if solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos + 1):
                return True
            board[new_x][new_y] = -1
    return False


if __name__ == "__main__":
    solveKT(n)
