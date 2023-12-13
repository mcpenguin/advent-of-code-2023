import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.boards = []
        self.board = []

    def process_line(self, line):
        """How to process each line in the input"""

        if line == '\n':
            self.boards.append(self.board)
            self.board = []
        else:
            self.board.append([c for c in line if c != '\n'])

    def board_has_vertical_reflection(self, board, num_cols_left):
        num_cols_right = len(board[0]) - num_cols_left
        for i in range(0, min(num_cols_left, num_cols_right)):
            for j in range(0, len(board)):
                if board[j][num_cols_left-i-1] != board[j][num_cols_left+i]:
                    return False
        return True
    
    def board_has_horizontal_reflection(self, board, num_rows_left):
        num_rows_right = len(board) - num_rows_left
        for i in range(0, min(num_rows_left, num_rows_right)):
            for j in range(0, len(board[0])):
                if board[num_rows_left-i-1][j] != board[num_rows_left+i][j]:
                    return False
        return True

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        total = 0
        for board in self.boards:
            for r in range(len(board)):
                if self.board_has_horizontal_reflection(board, r):
                    total += 100 * r
            for c in range(len(board[0])):
                if self.board_has_vertical_reflection(board, c):
                    total += c
        return total

# don't change this
if __name__ == '__main__':
    solution_class = Solution()
    assert len(sys.argv) > 1, "Please provide the name of the input file in the second terminal argument."
    filename = os.path.abspath(
        os.path.dirname(os.path.abspath(__file__))
        ) + \
        f"/inputs/{sys.argv[1]}.txt"
    print("--- DEBUGGING GOES HERE ---")
    with open(filename) as file:
        for line in file:
            solution_class.process_line(line)
    solution_class.process_line('\n')
    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

