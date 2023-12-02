import os
import sys
import re
import pandas as pd
from math import prod

class Solution:
    """Class for solution"""

    def __init__(self):
        self.total = 0

    def get_min_subset(self, subsets):
        subsets_df = pd.DataFrame.from_records(subsets)
        return {
            color: subsets_df[color].max()
            for color in ['red', 'green', 'blue']
        }

    def process_line(self, line: str):
        """How to process each line in the input"""

        line_split = re.split(', | |:|;|\\n', line)
        game_id = int(line_split[1])
        is_game_possible = True
        subsets = [] # list of {red: R, green: G, blue: B}
        current_subset = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        idx = 3
        while idx != len(line_split): # eof
            if line_split[idx] == '':
                idx += 1
                continue
        
            num = int(line_split[idx])
            idx += 1
            color = line_split[idx]
            idx += 1
            current_subset[color] = num

            if line_split[idx] == '':
                subsets.append(current_subset)
                current_subset = {
                    'red': 0,
                    'green': 0,
                    'blue': 0,
                }
                idx += 1

        min_subset = self.get_min_subset(subsets)
        self.total += prod(min_subset.values())

    def post_processing(self):
        """Function that is called after all the lines have been read"""
        pass

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        return self.total #tmp

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
    solution_class.post_processing()
    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

