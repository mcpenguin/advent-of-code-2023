import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.num_rows = 0
        self.num_cols = 0
        self.round_pos_col_dict = {} # col: poslist
        self.cube_pos_col_dict = {}

    def process_line(self, line: str, row_idx):
        """How to process each line in the input"""
        if line != '\n':
            self.num_rows += 1
            split = list(line[:-1])
            self.num_cols = len(split)

            for col_idx, c in enumerate(split):
                if c == '#':
                    if col_idx in self.cube_pos_col_dict:
                        self.cube_pos_col_dict[col_idx].append(row_idx)
                    else:
                        self.cube_pos_col_dict[col_idx] = [row_idx]
                elif c == 'O':
                    if col_idx in self.round_pos_col_dict:
                        self.round_pos_col_dict[col_idx].append(row_idx)
                    else:
                        self.round_pos_col_dict[col_idx] = [row_idx]

    def get_final_positions_for_rocks_for_col(self, col_idx):
        # returns the final positions of all the round rocks
        cube_l = self.cube_pos_col_dict.get(col_idx, [])[::-1] + [-1]
        round_l = self.round_pos_col_dict.get(col_idx, [])[::-1]
        # cube_l, round_l is sorted in descending order
        res = []
        cur_cube = 0
        cur_round = 0
        offset = 0
        while cur_cube < len(cube_l) and cur_round < len(round_l):
            if round_l[cur_round] > cube_l[cur_cube]:
                res.append(cube_l[cur_cube]+1+offset)
                offset += 1
                cur_round += 1
            else:
                offset = 0
                cur_cube += 1
        # print(col_idx, res)

        return sum([self.num_cols - x for x in res])

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # print(self.cube_pos_col_dict)
        # print(self.round_pos_col_dict)
        total = 0
        for col_idx in range(self.num_cols):
            total += self.get_final_positions_for_rocks_for_col(col_idx)

        return total

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
        for row_idx, line in enumerate(file):
            solution_class.process_line(line, row_idx)

    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

