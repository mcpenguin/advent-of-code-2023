import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.codes = []

    def process_line(self, line: str):
        """How to process each line in the input"""

        self.codes.append(line.strip())

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        self.elf_calories_list.sort(reverse=True)
        return sum(self.elf_calories_list[0:3])

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

        

