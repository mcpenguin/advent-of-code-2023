import os
import sys
import math


class Solution:
    """Class for solution"""

    def __init__(self):
        self.maze = []
        self.start_pos = (0, 0)
        self.end_pos = (0, 0)
        self.num_rows = 0
        self.num_cols = 0
        self.min_score_arr = []

    def get_adj_pos(self, pos, care_abt_bounds=True):
        adj = [
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
        ]
        if care_abt_bounds:
            adj = [a for a in adj if a[0] >= 0 and a[0] <
                   self.num_rows and a[1] >= 0 and a[1] < self.num_cols]
        return adj

    def process_line(self, line: str):
        """How to process each line in the input"""
        row = []
        score_row = []
        for col_idx, x in enumerate(line.strip()):
            row.append(x)
            if x == 'S':
                self.start_pos = (self.num_rows, col_idx)
            elif x == 'E':
                self.end_pos = (self.num_rows, col_idx)

            d = [math.inf] * 4
            score_row.append(d) # one for each direction

        self.maze.append(row)
        self.min_score_arr.append(score_row)
        self.num_rows += 1

    def print_min_score_arr(self):
        val_l = 6
        for i, (min_score_row, maze_row) in enumerate(zip(self.min_score_arr, self.maze)):
            s = ''
            for j, (min_score, x) in enumerate(zip(min_score_row, maze_row)):
                min_score = min(min_score)
                if x == '#':
                    s += '■' * val_l
                else:
                    s += ' ' * (val_l - len(str(min_score))) + str(min_score)
                s += ' '
            print(s)
        print()
                



    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # print(self.maze)
        self.min_score_arr[self.start_pos[0]][self.start_pos[1]] = [0] * 4
        directions = [
            (0, 1),  # east
            (1, 0),
            (0, -1),
            (-1, 0),
        ]

        stack = [(self.start_pos, 0)]  # position, direction index
        visited = set()
        num_it = 0
        while len(stack) > 0:

            head, direction_idx = stack[-1]
            stack.pop()

            # print(head, direction_idx)
            # print((head[0] + directions[direction_idx][0], head[1] + directions[direction_idx][1]))
            # print((head[0] + directions[((direction_idx + 1) % 4)][0], head[1] + directions[((direction_idx + 1) % 4)][1]))
            # print((head[0] + directions[(direction_idx - 1) % 4][0], head[1] + directions[(direction_idx - 1) % 4][1]))
            # print(stack)
            # print(self.min_score_arr)
            # print(visited)
            # print()

            # if wall just continue
            if self.maze[head[0]][head[1]] == '#':
                continue

            consider = [
                ((head[0] + directions[direction_idx][0], head[1] +
                 directions[direction_idx][1]), direction_idx, 1),
                ((head[0] + directions[(direction_idx + 1) % 4][0], head[1] +
                 directions[(direction_idx + 1) % 4][1]), (direction_idx + 1) % 4, 1001),
                ((head[0] + directions[(direction_idx - 1) % 4][0], head[1] +
                 directions[(direction_idx - 1) % 4][1]), (direction_idx - 1) % 4, 1001),
                # ((head[0] + directions[(direction_idx - 2) % 4][0], head[1] +
                #  directions[(direction_idx - 2) % 4][1]), (direction_idx - 2) % 4, 2001),
            ]

            for new_pos, d_idx, score_offset in consider:
                if self.min_score_arr[head[0]][head[1]][direction_idx] + score_offset < self.min_score_arr[new_pos[0]][new_pos[1]][d_idx]:
                    self.min_score_arr[new_pos[0]][new_pos[1]
                                                   ][d_idx] = self.min_score_arr[head[0]][head[1]][direction_idx] + score_offset
                    stack.append((new_pos, d_idx))

                # elif (new_pos, d_idx) not in visited:
                #     stack.append((new_pos, d_idx))

            # print(self.min_score_arr)
            # print(stack)
            # print(visited)
            # print()
        self.print_min_score_arr()
        return min(self.min_score_arr[self.end_pos[0]][self.end_pos[1]])


# don't change this
if __name__ == '__main__':
    solution_class = Solution()
    assert len(
        sys.argv) > 1, "Please provide the name of the input file in the second terminal argument."
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
