#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def is_safe(board, row, col, n):
    # Check if a queen can be placed in this row and column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    # Print the solution in the specified format
    print(','.join(map(str, board)))


def solve_nqueens(board, row, n):
    if row == n:
        # All queens are placed successfully, print the solution
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen and move to the next row
            board[row] = col
            solve_nqueens(board, row + 1, n)
            # Backtrack if no solution is found with the current placement
            board[row] = -1


def nqueens(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
