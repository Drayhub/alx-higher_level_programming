import sys

def solve(n, board, col):
    if col == n:
        # All queens have been placed, so we have found a solution
        print_board(board)
        return True

    # Try placing a queen in each row of the current column
    for i in range(n):
        if is_safe(board, i, col):
            # Place the queen and recurse
            board[i][col] = 1
            solve(n, board, col + 1)
            # Backtrack
            board[i][col] = 0

    # No solution was found
    return False

def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the same diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def print_board(board):
    for row in board:
        print(' '.join([str(cell) for cell in row]))

def main():
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        return 1

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        return 1

    if n < 4:
        print('N must be at least 4')
        return 1

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(n, board, 0)

if __name__ == '__main__':
    main()
