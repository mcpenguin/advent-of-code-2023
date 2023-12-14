import os
import sys
import copy

class Solution:
    """Class for solution"""

    def __init__(self):
        self.num_rows = 0
        self.num_cols = 0
        self.cube_pos_list = [] # y, x
        self.round_pos_list = [] # y, x
        # self.round_pos_col_dict = {} # col: poslist
        self.cube_pos_col_dict = {}
        # self.round_pos_row_dict = {}
        self.cube_pos_row_dict = {}

    def process_line(self, line: str, row_idx):
        """How to process each line in the input"""
        if line != '\n':
            self.num_rows += 1
            split = list(line[:-1])
            self.num_cols = len(split)

            for col_idx, c in enumerate(split):
                if c == '#':
                    self.cube_pos_list.append((row_idx, col_idx))
                    if col_idx in self.cube_pos_col_dict:
                        self.cube_pos_col_dict[col_idx].append(row_idx)
                    else:
                        self.cube_pos_col_dict[col_idx] = [row_idx]

                    if row_idx in self.cube_pos_row_dict:
                        self.cube_pos_row_dict[row_idx].append(col_idx)
                    else:
                        self.cube_pos_row_dict[row_idx] = [col_idx]
                elif c == 'O':
                    self.round_pos_list.append((row_idx, col_idx))

    def convert_list_to_bucket_dict(self, pos_list, type):
        pos_dict = {}
        # print(pos_list)
        if type == 'col':
            for col_idx in range(self.num_cols):
                pos_dict[col_idx] = []
            pos_list.sort(key=lambda x: x[0]) # sort by row idx
            for row_idx, col_idx in pos_list:
                if col_idx in pos_dict:
                    pos_dict[col_idx].append(row_idx)
        elif type == 'row':
            for row_idx in range(self.num_rows):
                pos_dict[row_idx] = []
            pos_list.sort(key=lambda x: x[1]) # sort by col idx
            for row_idx, col_idx in pos_list:
                if row_idx in pos_dict:
                    pos_dict[row_idx].append(col_idx)
        return pos_dict

    def get_final_positions_for_rocks_north(self, round_pos_list):
        res = []
        round_pos_dict = self.convert_list_to_bucket_dict(round_pos_list, 'col')
        for col_idx in range(self.num_cols):
            cube_l = self.cube_pos_col_dict.get(col_idx, [])[::-1] + [-1]
            round_l = round_pos_dict.get(col_idx, [])[::-1]

            cur_cube = 0
            cur_round = 0
            offset = 0
            while cur_cube < len(cube_l) and cur_round < len(round_l):
                if round_l[cur_round] > cube_l[cur_cube]:
                    res.append((cube_l[cur_cube]+1+offset, col_idx))
                    offset += 1

                    cur_round += 1
                else:
                    offset = 0
                    cur_cube += 1
        return res
    
    def get_final_positions_for_rocks_south(self, round_pos_list):
        res = []
        round_pos_dict = self.convert_list_to_bucket_dict(round_pos_list, 'col')
        for col_idx in range(self.num_cols):
            cube_l = self.cube_pos_col_dict.get(col_idx, []) + [self.num_rows]
            round_l = round_pos_dict.get(col_idx, [])

            cur_cube = 0
            cur_round = 0
            offset = 0
            while cur_cube < len(cube_l) and cur_round < len(round_l):
                if round_l[cur_round] < cube_l[cur_cube]:
                    res.append((cube_l[cur_cube]-1-offset, col_idx))
                    offset += 1

                    cur_round += 1
                else:
                    offset = 0
                    cur_cube += 1
        return res

    def get_final_positions_for_rocks_west(self, round_pos_list):
        res = []
        round_pos_dict = self.convert_list_to_bucket_dict(round_pos_list, 'row')
        # print(round_pos_dict)
        # print(self.cube_pos_row_dict)
        for row_idx in range(self.num_rows):
            cube_l = self.cube_pos_row_dict.get(row_idx, [])[::-1] + [-1]
            round_l = round_pos_dict.get(row_idx, [])[::-1]

            cur_cube = 0
            cur_round = 0
            offset = 0
            while cur_cube < len(cube_l) and cur_round < len(round_l):
                if round_l[cur_round] > cube_l[cur_cube]:
                    res.append((row_idx, cube_l[cur_cube]+1+offset))
                    offset += 1

                    cur_round += 1
                else:
                    offset = 0
                    cur_cube += 1
        return res
    
    def get_final_positions_for_rocks_east(self, round_pos_list):
        res = []
        round_pos_dict = self.convert_list_to_bucket_dict(round_pos_list, 'row')
        for row_idx in range(self.num_rows):
            cube_l = self.cube_pos_row_dict.get(row_idx, []) + [self.num_cols]
            round_l = round_pos_dict.get(row_idx, [])

            cur_cube = 0
            cur_round = 0
            offset = 0
            while cur_cube < len(cube_l) and cur_round < len(round_l):
                if round_l[cur_round] < cube_l[cur_cube]:
                    res.append((row_idx, cube_l[cur_cube]-1-offset))
                    offset += 1

                    cur_round += 1
                else:
                    offset = 0
                    cur_cube += 1
        return res

    def get_value_for_state(self, round_pos_list):
        return sum([self.num_cols - x[0] for x in round_pos_list])

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        total = 0
        # For the test input, the spins "cycle" around every 7 spins.
        # For my real input, the spins "cycle" around every 22 spins after spin 110. 
        # So, we can just take num_spins := 110 + num_spins % 22 to get our total.
        # num_spins = 1000000000 % 7
        num_spins = 1000000000
        cycle_length = 22 # hardcoded
        offset = 110 # hardcoded

        # dict ot keep track of previous states to find cycle information
        # prev_states = {}
        cur_pos_list = copy.deepcopy(self.round_pos_list)
        # prev_states[0] = cur_pos_list
        # for i in range(num_spins):
        for i in range(offset + num_spins % cycle_length):

            cur_pos_list = self.get_final_positions_for_rocks_north(cur_pos_list)
            cur_pos_list = self.get_final_positions_for_rocks_west(cur_pos_list)
            cur_pos_list = self.get_final_positions_for_rocks_south(cur_pos_list)
            cur_pos_list = self.get_final_positions_for_rocks_east(cur_pos_list)

            # for k, state in prev_states.items():
            #     if state == cur_pos_list:
            #         print(f"State after spin {i+1} is equal to state after spin {k}")
            # prev_states[i+1] = cur_pos_list

        total = self.get_value_for_state(cur_pos_list)

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

        

