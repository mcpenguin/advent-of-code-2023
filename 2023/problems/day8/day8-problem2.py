import os
import sys
import copy
from math import prod

class Solution:
    """Class for solution"""

    def __init__(self):
        self.steps = []
        self.locations = {}

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line != '\n':
            if len(self.steps) == 0:
                self.steps = [c for c in line if c != '\n']
            else:
                split = line.split(" = ")
                start = split[0]                
                rest = split[1][1:-2].split(", ")
                self.locations[start] = rest

    def is_finished(self, locations):
        letters = [l[-1] for l in locations]
        return letters.count('Z') == len(letters)

    def get_solution(self):
        locations = [l for l in self.locations.keys() if l[-1] == 'A']
        num_steps = 0
        # store the map for one pass thru of the steps
        agg_map = { l: l for l in self.locations }
        for s in self.steps:
            tmp = copy.deepcopy(agg_map)
            for source, val in tmp.items():
                
                if s == 'L':
                    tmp[source] = self.locations[tmp[source]][0]
                else:
                    tmp[source] = self.locations[tmp[source]][1]
            agg_map = tmp

        cmap = {}
        for l in locations:
            cmap[l] = []
            i = 1
            cur = agg_map[l]
            while i < len(self.locations.keys()):
                if cur[-1] == 'Z':
                    cmap[l].append(i)
                i += 1
                cur = agg_map[cur]

        num_steps = prod([li[0] for li in cmap.values()]) * len(self.steps)
        return num_steps

# don't change
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

        

