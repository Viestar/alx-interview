#!/usr/bin/python3
"""
nqueens problem solution
"""
import sys


def backtracker(row, n, col, pove, neve, board):
    """ function to find solution through back tracking """
    if row == n:
        response = []
        for lq in range(len(board)):
            for king in range(len(board[lq])):
                if board[lq][king] == 1:
                    response.append([lq, king])
        print(response)
        return

    for silver in range(n):
        if silver in col or (row + silver) in pove or (row - silver) in neve:
            continue

        col.add(silver)
        pove.add(row + silver)
        neve.add(row - silver)
        board[row][silver] = 1

        backtracker(row+1, n, col, pove, neve, board)

        col.remove(silver)
        pove.remove(row + silver)
        neve.remove(row - silver)
        board[row][silver] = 0


def nqueens(n):
    """ Solution to nqueens problem  """
    negative = set()
    col = set()
    positive = set()
    board = [[0] * n for i in range(n)]

    backtracker(0, n, col, positive, negative, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
