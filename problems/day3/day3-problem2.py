import os
import sys
from math import prod

class Solution:
    """Class for solution"""

    def __init__(self):
        self.star_positions = [] # list of (y, x)
        self.numbers = [] # (y, x, num_str)

    def is_number_next_to_gear(self, num_y, num_x, num_str, gear_y, gear_x):
        border = [(num_y-1, x) for x in range(num_x-1, num_x+len(num_str)+1)] + \
        [(num_y, num_x-1), (num_y, num_x + len(num_str))] + \
        [(num_y+1, x) for x in range(num_x-1, num_x+len(num_str)+1)]
        return (gear_y, gear_x) in border

    def get_product_from_star(self, star_y, star_x):
        border = [(star_y-1, x) for x in range(star_x-1, star_x+2)] + \
        [(star_y, star_x-1), (star_y, star_x + star_x+1)] + \
        [(star_y+1, x) for x in range(star_x-1, star_x+2)]
        numbers_adj_to_star = [
            n for n in self.numbers
            if (n[0], n[1]) in border
        ]
        if len(numbers_adj_to_star) != 2:
            print("is not gear")
            return 0
        else:
            print("is gear")
            return prod([int(n[2]) for n in numbers_adj_to_star])

    def process_line(self, line: str, row_idx: int):
        """How to process each line in the input"""
        is_num = False
        current_num_str = ""
        current_num_y = row_idx
        current_num_x = ""
        for col_idx, c in enumerate(line):
            if c != '\n':
                if c == '*':
                    self.star_positions.append((row_idx, col_idx))
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
        numbers_next_to_gear = {} # (gear_y, gear_x): [] 
        for gear_y, gear_x in self.star_positions:
            numbers_next_to_gear[(gear_y, gear_x)] = []
        for num_y, num_x, num_str in self.numbers:
            for gear_y, gear_x in self.star_positions:
                if self.is_number_next_to_gear(num_y, num_x, num_str, gear_y, gear_x):
                    numbers_next_to_gear[(gear_y, gear_x)].append(int(num_str))

        for (num_y, num_x), num_list in numbers_next_to_gear.items():
            if len(num_list) == 2:
                total += prod(num_list)

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

        

