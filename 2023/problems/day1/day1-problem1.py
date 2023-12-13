import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.total = 0

    def process_line(self, line):
        """How to process each line in the input"""
        first_digit = 0
        last_digit = 0
        if line != '':
            for i in range(len(line)):
                if line[i].isdigit():
                    first_digit = int(line[i])
                    break
            for i in range(0, len(line)):
                if line[len(line)-1-i].isdigit():
                    last_digit = int(line[len(line)-1-i])
                    break
        self.total += first_digit * 10 + last_digit

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

        

