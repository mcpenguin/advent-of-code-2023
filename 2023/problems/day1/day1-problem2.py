import os
import sys
import re

class Solution:
    """Class for solution"""

    def __init__(self):
        self.total = 0

    def process_line(self, line: str):
        """How to process each line in the input"""
        first_digit = 0
        last_digit = 0
        if line != '':
            digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            positions_start = []
            for digit in digits:
                for m in re.finditer(digit, line):
                    positions_start.append((digit, m.start()))
            for i in range(1, 10):
                for m in re.finditer(str(i), line):
                    positions_start.append((i, m.start()))

            positions_start_sort = list([x for x in positions_start if x[1] != -1])
            positions_start_sort.sort(key=lambda x: x[1])

            first = positions_start_sort[0][0]
            if isinstance(first, str):
                first_digit = digits.index(first) + 1
            else:
                first_digit = first

            last = positions_start_sort[-1][0]
            if isinstance(last, str):
                last_digit = digits.index(last) + 1
            else:
                last_digit = last
        val = first_digit * 10 + last_digit
        self.total += val

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        return self.total

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
    solution_class.process_line("")
    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

