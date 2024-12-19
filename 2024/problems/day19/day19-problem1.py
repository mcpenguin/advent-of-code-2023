import os
import sys
import re

class Solution:
    """Class for solution"""

    def __init__(self):
        self.parse_designs = False
        self.designs = []
        self.patterns = set()

        self.no_work = set()

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line == '\n':
            self.parse_designs = True
        else:
            if self.parse_designs:
                self.designs.append(line.strip())
            else:
                self.patterns = sorted(line.strip().split(', '), key=len, reverse=True)
                self.pattern = '^(' + '|'.join(line.strip().split(', ')) + ')*$'

    def max_munch(self, s, idx=0):
        if idx >= len(s):
            return True
        if idx in self.no_work:
            return False
        
        # print(idx, s[idx:], self.no_work)
        for pat in self.patterns:
            if idx + len(pat) <= len(s) and s[idx:len(pat) + idx] == pat:
                res = self.max_munch(s, idx + len(pat))
                if res:
                    return True
                
        self.no_work.add(idx)
        return False

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # print(self.patterns)
        res = 0
        # print(len(self.designs))
        for i, design in enumerate(self.designs):
            self.no_work = set()
            # if re.match(self.pattern, design):
            if self.max_munch(design, 0):
                res += 1
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

        

