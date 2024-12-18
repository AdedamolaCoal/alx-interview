#!/usr/bin/python3
"""N-queens problem solver."""

import sys


def is_valid(board, row, col):
    """Check if placing a queen at (row, col) is safe.
    
    Args:
        board (list): The current state of the board.
        row (int): The row where the queen is being placed.
        col (int): The column where the queen is being placed.
    
    Returns:
        bool: True if placing a queen at (row, col) is safe, else False.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, row, board, solutions):
    """Recursive backtracking to find all solutions.

    Args:
        N (int): The size of the board.
        row (int): The current row being processed.
        board (list): The current state of the board.
        solutions (list): The list of solutions found.
    """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)

def main():
    """verifies the input and calls the solve_nqueens function.

    Returns:
        None"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(N, 0, [-1] * N, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
