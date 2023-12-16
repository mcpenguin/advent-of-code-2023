import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.seq = []

    def process_line(self, line):
        """How to process each line in the input"""

        if line != '\n':
            self.seq = line[:-1].split(',')

    def get_hash(self, text):
        total = 0
        for c in text:
            total = ((total + ord(c)) * 17) % 256
        return total

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        total = 0
        for t in self.seq:
            total += self.get_hash(t)
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

    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

