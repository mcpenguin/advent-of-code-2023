import os
import sys
import copy

class Solution:
    """Class for solution"""

    def __init__(self):
        self.num_safe = 0

    def is_safe(self, l: list[int]):
        diff = []
        abs_diff = []
        for i in range(0, len(l) - 1):
            diff.append(l[i+1] - l[i])
            abs_diff.append(abs(l[i+1] - l[i]))
        if (min(diff) > 0 or max(diff) < 0) and (min(abs_diff) >= 1 and max(abs_diff)) <= 3:
            return True
        return False
    
    def is_actually_safe(self, l: list[int]):
        # print(l)
        if self.is_safe(l):
            return True
        for i in range(len(l)):
            l_copy = copy.deepcopy(l)
            del l_copy[i]
            # print(l_copy)
            if self.is_safe(l_copy):
                return True
        return False

    def process_line(self, line: str):
        """How to process each line in the input"""

        l = [int(x) for x in line.split()]
        if self.is_actually_safe(l):
            self.num_safe += 1

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        return self.num_safe

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

        

