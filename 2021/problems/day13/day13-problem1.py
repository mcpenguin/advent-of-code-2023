import os
import sys
import copy

class Solution:
    """Class for solution"""

    def __init__(self):
        self.dot_pos_set = set() # (x, y)
        self.folds = [] # ('x' | 'y', num)
        self.atFold = False

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line == '\n':
            self.atFold = True
        else:
            if self.atFold:
                split = line[:-1].split(" ")
                xy, num = split[2].split("=")
                self.folds.append((xy, int(num)))
            else:
                split = line[:-1].split(",")
                self.dot_pos_set.add((int(split[0]), int(split[1])))

    def get_state_after_fold(self, state: set[tuple[int, int]], fold_xy, fold_num):
        new_state = set()
        for x, y in state:
            if fold_xy == 'y':
                if y > fold_num: # coord will never fall on fold line
                    new_state.add((x, 2 * fold_num - y))
                else:
                    new_state.add((x, y))
            elif fold_xy == 'x':
                if x > fold_num: # coord will never fall on fold line
                    new_state.add((2 * fold_num - x, y))
                else:
                    new_state.add((x, y))
        return new_state
    
    def print_state(self, state):
        max_x = max([e[0] for e in state])
        max_y = max([e[1] for e in state])

        lines = {i: ["."]*(max_x+1) for i in range(max_y+1)}
        # print(lines)
        for x, y in state:
            lines[y][x] = "#"

        res = ""
        for l in lines.values():
            res += "".join(l) + '\n'
        return res

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        cur_state = copy.deepcopy(self.dot_pos_set)
        for fold_xy, fold_num in self.folds[0:1]:
            cur_state = self.get_state_after_fold(cur_state, fold_xy, fold_num)

        return len(cur_state)

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

        

