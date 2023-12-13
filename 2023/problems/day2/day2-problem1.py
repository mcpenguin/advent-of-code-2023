import os
import sys
import re

class Solution:
    """Class for solution"""

    def __init__(self):
        self.game_id_total = 0
        self.max_subset = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }

    def check_if_subset_possible(self, subset):
        return subset['red'] <= self.max_subset['red'] and \
            subset['green'] <= self.max_subset['green'] and \
            subset['blue'] <= self.max_subset['blue']

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
                is_game_possible = is_game_possible and self.check_if_subset_possible(current_subset)
                current_subset = {
                    'red': 0,
                    'green': 0,
                    'blue': 0,
                }
                idx += 1

        if is_game_possible:
            self.game_id_total += game_id

    def post_processing(self):
        """Function that is called after all the lines have been read"""
        pass

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        return self.game_id_total #tmp

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

        

