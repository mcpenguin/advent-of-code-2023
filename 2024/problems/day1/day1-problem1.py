import os
import sys
import re

class Solution:
    """Class for solution"""

    def __init__(self):
        self.list1 = []
        self.list2 = []

    def process_line(self, line: str):
        """How to process each line in the input"""
        ilist = re.split(' |\n', line)
        n1 = int(ilist[0])
        n2 = int(ilist[-2])
        self.list1.append(n1)
        self.list2.append(n2)

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        self.list1.sort()
        self.list2.sort()
        result = 0
        for n1, n2 in zip(self.list1, self.list2):
            result += abs(n1 - n2)
        return result

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

        

