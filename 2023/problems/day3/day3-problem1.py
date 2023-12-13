import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.symbol_positions = [] # list of (y, x)
        self.numbers = [] # (y, x, num_str)

    def is_number_next_to_symbol(self, num_y, num_x, num_str):
        border = [(num_y-1, x) for x in range(num_x-1, num_x+len(num_str)+1)] + \
        [(num_y, num_x-1), (num_y, num_x + len(num_str))] + \
        [(num_y+1, x) for x in range(num_x-1, num_x+len(num_str)+1)]
        return len(set(border).intersection(set(self.symbol_positions))) > 0

    def process_line(self, line: str, row_idx: int):
        """How to process each line in the input"""
        is_num = False
        current_num_str = ""
        current_num_y = row_idx
        current_num_x = ""
        for col_idx, c in enumerate(line):
            if c != '\n':
                if not c.isdigit() and c != '.':
                    self.symbol_positions.append((row_idx, col_idx))
                if c.isdigit():
                    if not is_num:
                        is_num = True
                        current_num_x = col_idx
                    current_num_str += c
                if not c.isdigit() and is_num:
                    self.numbers.append((current_num_y, current_num_x, current_num_str))
                    current_num_str = ''
                    is_num = False
        if is_num == True:
            self.numbers.append((current_num_y, current_num_x, current_num_str))

    def get_solution(self):
        total = 0
        for num_y, num_x, num_str in self.numbers:
            if self.is_number_next_to_symbol(num_y, num_x, num_str):
                total += int(num_str)
        """How to retrieve the solution once all lines have been processed"""
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
        for row_idx, line in enumerate(file):
            solution_class.process_line(line, row_idx)

    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

