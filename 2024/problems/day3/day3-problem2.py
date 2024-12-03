import os
import sys
import re

class Solution:
    """Class for solution"""

    def __init__(self):
        self.line = ""

    def process_line(self, line: str):
        """How to process each line in the input"""
        self.line += line

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        result = 0
        activate = True
        for mul in re.finditer('mul\([0-9]+\,[0-9]+\)|do\(\)|don\'t\(\)', self.line):
            s = self.line[mul.start(0):mul.end(0)]
            if 'don\'t' in s:
                activate = False
            elif 'do' in s:
               activate = True
            else:
                l = re.split('[\(\)\,]', s)
                n1 = int(l[1])
                n2 = int(l[2])
                if activate and n1 < 1000 and n2 < 1000:
                    result += n1 * n2
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

        

