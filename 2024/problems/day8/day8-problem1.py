import os
import sys
from collections import defaultdict

class Solution:
    """Class for solution"""

    def __init__(self):
        self.nodes = defaultdict(list[tuple[int, int]])
        self.row_idx = 0

    def process_line(self, line: str):
        """How to process each line in the input"""
        for col_idx, x in enumerate(line):
            if x != '\n' and x != '.':
                self.nodes[x].append((self.row_idx, col_idx))
        self.row_idx += 1
        self.num_cols = col_idx
        

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        self.num_rows = self.row_idx
        print(self.num_rows, self.num_cols)
        anode_set = set()
        for letter, nlist in self.nodes.items():
            for i in range(len(nlist)):
                for j in range(i+1, len(nlist)):
                    x = nlist[i]
                    y = nlist[j]
                    delta = (x[0] - y[0], x[1] - y[1])
                    if delta != (0, 0):
                        anodes = [
                                (x[0] + delta[0], x[1] + delta[1]),
                                (y[0] - delta[0], y[1] - delta[1])
                            ]
                        anodes = [k for k in anodes if k[0] >= 0 and k[0] < self.num_rows and k[1] >= 0 and k[1] < self.num_cols]
                        print(letter, x, y, len(anodes))
                        for anode in anodes:
                            anode_set.add(anode)
        
        return len(anode_set)

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

        

