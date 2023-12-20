import os
import sys
import math
import copy

class Solution:
    """Class for solution"""

    def __init__(self):
        self.grid = []
        self.num_rows = 0
        self.num_cols = 0

        self.unvisited: set[tuple[int, int]] = set([]) # set of unvisited nodes
        # 2D array (row_idx, col_idx); each value is (min_val, {(dir, num): val})
        # where the value associated with the key (dir, num)
        # means the minimum distance of the path 
        # from the start to the node that ends with a consecutive 
        # “run” of exactly num “dir” (with the preceding direction 
        # before the run being different)
        # the directions represent "flowing into" the associated node
        self.min_heat_loss_arr: dict[tuple[int, int], dict] = {}
        
        self.nums = range(1, 4)
        self.direction_dict = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1),
        }
        self.directions = self.direction_dict.keys()

    def process_line(self, line):
        """How to process each line in the input"""

        if line != '\n':
            self.grid.append([int(x) for x in line[:-1]])

    def is_valid_pos(self, pos):
        row_idx, col_idx = pos
        return row_idx >= 0 and row_idx < self.num_rows and \
            col_idx >= 0 and col_idx < self.num_cols

    # def get_min_heat_loss(self, row_idx, col_idx):
    #     if row_idx == self.num_rows - 1 and col_idx == self.num_cols - 1:
    #         return (self.grid[row_idx][col_idx], [(row_idx, col_idx)])
        
    #     up = (row_idx - 1, col_idx)
    #     down = (row_idx + 1, col_idx)
    #     left = (row_idx, col_idx - 1)
    #     right = (row_idx, col_idx + 1)
    #     min_vals = []
    #     if self.is_valid_pos(up):
    #         min_val_up, min_path_up = self.min_heat_loss_arr[up[0]][up[1]]
    #         # if the last three elements of the min path is not a straight line
    #         # going down, then adding this position to the minpath is valid
    #         if min_path_up is not None and \
    #             min_path_up[-3:] != [(row_idx + i, col_idx) for i in range(3)]:
    #             min_vals.append((min_path_up + [up], min_val_up + ))
    #     if self.is_valid_pos(down):
    #         min_val_down, min_path_down = self.min_heat_loss_arr[down[0]][down[1]]
    #         if min_path_down is not None and \
    #             min_path_down[-3:] != [(row_idx - i, col_idx) for i in range(3)]:
    #             min_vals.append((down, min_val_down + [down]))
    #     if self.is_valid_pos(left):
    #         min_val_left, min_path_left = self.min_heat_loss_arr[left[0]][left[1]]
    #         if min_path_left is not None and \
    #             min_path_left[-3:] != [(row_idx, col_idx - i) for i in range(3)]:
    #             min_vals.append((left, min_val_left + [left]))
    #     if self.is_valid_pos(right):
    #         min_val_right, min_path_right = self.min_heat_loss_arr[right[0]][right[1]]
    #         if min_path_right is not None and \
    #             min_path_right[-3:] != [(row_idx, col_idx + i) for i in range(3)]:
    #             min_vals.append((right, min_val_right + [right]))
        
    #     min_val, min_path = min(min_vals, key=lambda x: x[1])
    #     return min_val, min_path

    def get_neighbors_of_pos(self, row_idx, col_idx):
        up_l = [('up', i, (row_idx - i, col_idx), [(row_idx - j, col_idx) for j in range(1, i+1)]) for i in self.nums]
        down_l = [('down', i, (row_idx + i, col_idx), [(row_idx + j, col_idx) for j in range(1, i+1)]) for i in self.nums]
        left_l = [('left', i, (row_idx, col_idx - i), [(row_idx, col_idx - j) for j in range(1, i+1)]) for i in self.nums]
        right_l = [('right', i, (row_idx, col_idx + i), [(row_idx, col_idx + j) for j in range(1, i+1)]) for i in self.nums]
        # if last_direction == 'up':
        #     up_l = up_l[:-1]
        # elif last_direction == 'down':
        #     down_l = down_l[:-1]
        # elif last_direction == 'left':
        #     left_l = left_l[:-1]
        # elif last_direction == 'right':
        #     right_l = right_l[:-1]
        
        dir_list = up_l + down_l + left_l + right_l
        return [(name, d, pos_head, pos_list) for name, d, pos_head, pos_list in dir_list \
                if all([self.is_valid_pos(pos) for pos in pos_list + [pos_head]])]

    def does_path_have_consecutive_steps_for_direction(self, dir_name, path):
        return path[-4:] == 4*[dir_name]
        # row_idx, col_idx = path[-1]
        # bound = 3
        # if last_direction == dir_name:
        #     bound = 2
        
        # if dir_name == 'up':
        #     return path[-1 * bound:] == [(row_idx+j, col_idx) for j in range(bound, -1, -1)]
        # if dir_name == 'down':
        #     return path[-1 * bound:] == [(row_idx+j, col_idx) for j in range(-1 * bound, 1, 1)]
        # if dir_name == 'left':
        #     return path[-1 * bound:] == [(row_idx, col_idx+j) for j in range(bound, -1, -1)]
        # if dir_name == 'right':
        #     return path[-1 * bound:] == [(row_idx, col_idx+j) for j in range(-1 * bound, 1, 1)]

    def get_perpend_directions(self, direction):
        return {
            'up': ['left', 'right'],
            'down': ['left', 'right'],
            'left': ['up', 'down'],
            'right': ['up', 'down'],
        }[direction]

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # init min heat loss arr
        self.num_rows, self.num_cols = len(self.grid), len(self.grid[0])
        default = {
            'min_val': math.inf,
            'min_path_vals': {
                (direction, num): math.inf for direction in self.directions for num in self.nums
            }
        }
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.min_heat_loss_arr[(i, j)] = copy.deepcopy(default)
                self.unvisited.add((i, j))

        self.min_heat_loss_arr[(0, 0)] = {
            'min_val': 0,
            'min_path_vals': copy.deepcopy({
                (direction, num): 0 \
                    for direction in self.directions 
                    for num in self.nums
            })
        }
        # self.min_heat_loss_arr[(0, 1)] = {
        #     'min_val': self.grid[0][1],
        #     'min_path_vals': copy.deepcopy({
        #         (direction, num): self.grid[0][1] \
        #             for direction in self.directions 
        #             for num in self.nums
        #     })
        # }
        # self.min_heat_loss_arr[(1, 0)] = {
        #     'min_val': self.grid[1][0],
        #     'min_path_vals': copy.deepcopy({
        #         (direction, num): self.grid[1][0] \
        #             for direction in self.directions 
        #             for num in self.nums
        #     })
        # }
        # print(self.min_heat_loss_arr)

        # assign None values to inaccessible paths
        # for row_idx in range(self.num_rows):
        #     for col_idx in range(self.num_cols):
        #         for num in self.nums:
        #             for direction in self.directions:
        #             #     print(row_idx, col_idx, direction, num, (direction == 'down' and row_idx < num) or \
        #             #         (direction == 'up' and row_idx >= self.num_rows - num) or \
        #             #         (direction == 'right' and col_idx < num) or \
        #             #         (direction == 'left' and col_idx >= self.num_cols - num))
        #                 if (direction == 'down' and row_idx < num) or \
        #                     (direction == 'up' and row_idx >= self.num_rows - num) or \
        #                     (direction == 'right' and col_idx < num) or \
        #                     (direction == 'left' and col_idx >= self.num_cols - num):
        #                     print(row_idx, col_idx, direction, num)
                            # self.min_heat_loss_arr[row_idx][col_idx]['min_path_vals'][(direction, num)] = None
        # print(self.min_heat_loss_arr[0][2])

        while len(self.unvisited) > 0:
            # print('unvisited', {p: self.min_heat_loss_arr[p]['min_val'] for p in self.unvisited})
            cur_pos = min(self.unvisited, key=lambda p: self.min_heat_loss_arr[p]['min_val'])
            cur_row_idx, cur_col_idx = cur_pos  
            # print(cur_pos)
            # print(self.min_heat_loss_arr[cur_row_idx][cur_col_idx])

            neighbors = self.get_neighbors_of_pos(cur_row_idx, cur_col_idx)
            for direction, num, pos_head, pos_list in neighbors:
                # print(cur_pos, direction, num, pos_list, pos_head)
                pos_head_row_idx, pos_head_col_idx = pos_head
                # print(cur_pos, pos_list, self.min_heat_loss_arr[pos_head_row_idx][pos_head_col_idx])
                # (direction, num) is the "distance" away from cur_pos to pos_head
                if pos_head in self.unvisited:
                    # update the min path for (direction, num) for neighbor
                    # print(cur_pos, pos_list)
                    # print(self.min_heat_loss_arr[pos_head_row_idx][pos_head_col_idx]['min_path_vals'][(direction, num)],
                    #     *[
                    #         self.min_heat_loss_arr[cur_pos]['min_path_vals'][(other_direction, other_num)] + sum([self.grid[pos[0]][pos[1]] for pos in pos_list])
                    #         for other_direction in filter(lambda d: d != direction, self.directions)
                    #         for other_num in self.nums
                    #     ])
                    self.min_heat_loss_arr[pos_head]['min_path_vals'][(direction, num)] = min(
                        self.min_heat_loss_arr[pos_head]['min_path_vals'][(direction, num)],
                        *[
                            self.min_heat_loss_arr[cur_pos]['min_path_vals'][(other_direction, other_num)] + sum([self.grid[pos[0]][pos[1]] for pos in pos_list])
                            for other_direction in self.get_perpend_directions(direction)
                            for other_num in self.nums
                        ]
                    )
                    # print(self.min_heat_loss_arr[pos_head_row_idx][pos_head_col_idx])
                    # update the "ultimate" min value for the tentative distance of the neighbor
                    self.min_heat_loss_arr[pos_head]['min_val'] = min(
                        self.min_heat_loss_arr[pos_head]['min_val'],
                        self.min_heat_loss_arr[pos_head]['min_path_vals'][(direction, num)]
                    )
                    # print('unvisited', {p: self.min_heat_loss_arr[p]['min_val'] for p in self.unvisited})

            # mark the current node as visited
            self.unvisited.remove(cur_pos)
            # crash
            # print(self.min_heat_loss_arr)

        # init visited
        # cur_pos = (0, 0) # original node
        # cur_row_idx, cur_col_idx = cur_pos
        # while cur_pos is not None:
        #     cur_tent_dist, cur_tent_path, cur_dir_path = self.min_heat_loss_arr[cur_row_idx][cur_col_idx]
        #     neighbors = self.get_neighbors_of_pos(cur_row_idx, cur_col_idx)
        #     # print(self.min_heat_loss_arr)
        #     # if cur_pos == (0, 3):
        #     #     print(cur_pos)

        #     for name, d, pos_list in neighbors:
        #         # if cur_pos == (0, 3):
        #         #     print(name, d, pos_list)

        #         pos_head = pos_list[-1]
        #         if pos_head in self.unvisited:
        #             old_tent_dist, old_tent_path, old_dir_path = self.min_heat_loss_arr[pos_head[0]][pos_head[1]]
        #             new_tent_dist = cur_tent_dist + sum([self.grid[pos[0]][pos[1]] for pos in pos_list])
        #             new_tent_path = cur_tent_path + pos_list
        #             new_dir_path = cur_dir_path + d * [name]
        #             # print(new_tent_dist, new_tent_path)
        #             if pos_head in [(1,4)]:
        #                 print(cur_pos, pos_list, new_tent_dist, new_tent_path, new_dir_path)

        #             if new_tent_dist < old_tent_dist and \
        #                 not self.does_path_have_consecutive_steps_for_direction(name, new_dir_path):
        #                 self.min_heat_loss_arr[pos_head[0]][pos_head[1]] = new_tent_dist, new_tent_path, new_dir_path
            
        #     self.unvisited.remove(cur_pos)
        #     # if cur_pos == (0, 3):
        #     #     crash
        #     if len(self.unvisited) == 0:
        #         cur_pos = None
        #     else:
        #         cur_pos = min(self.unvisited, key=lambda p: self.min_heat_loss_arr[p[0]][p[1]])
        #         cur_row_idx, cur_col_idx = cur_pos

        print({k: v['min_val'] for k, v in self.min_heat_loss_arr.items()})
        # print(self.min_heat_loss_arr[(self.num_rows - 1, self.num_cols - 1)]['min_path_vals'])

        return self.min_heat_loss_arr[(self.num_rows - 1, self.num_cols - 1)]['min_val']


        # print(self.min_heat_loss_arr)
        
        # for start_col in range(self.num_cols-1, -1, -1):
        #     col_idx = start_col
        #     row_idx = self.num_rows - 1
        #     print(col_idx, row_idx)
        #     while row_idx >= 0 and col_idx < self.num_cols:
        #         self.min_heat_loss_arr[row_idx][col_idx] = self.get_min_heat_loss(row_idx, col_idx)
        #         row_idx -= 1
        #         col_idx += 1

        # return self.min_heat_loss_arr

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

        

