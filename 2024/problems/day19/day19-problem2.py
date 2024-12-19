import os
import sys
import re

class Solution:
    """Class for solution"""

    def __init__(self):
        self.parse_designs = False
        self.designs = []
        self.patterns = set()
        self.num_ways = {}

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line == '\n':
            self.parse_designs = True
        else:
            if self.parse_designs:
                self.designs.append(line.strip())
            else:
                self.patterns = sorted(line.strip().split(', '), key=len, reverse=True)

    def max_munch(self, s, idx=0):
        if idx >= len(s):
            return True
        if idx in self.num_ways:
            return self.num_ways[idx]
        
        num = 0
        for pat in self.patterns:
            if idx + len(pat) <= len(s) and s[idx:len(pat) + idx] == pat:
                res = self.max_munch(s, idx + len(pat))
                if res:
                    num += res

        self.num_ways[idx] = num  
        return num

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        res = 0
        for i, design in enumerate(self.designs):
            self.num_ways = {}
            res += self.max_munch(design, 0)
        return res
        

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

        

