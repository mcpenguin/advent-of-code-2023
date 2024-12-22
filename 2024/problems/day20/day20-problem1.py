import os
import sys
from collections import Counter

class Solution:
    """Class for solution"""

    def __init__(self):
        self.map = {}
        self.num_cols = 0
        self.num_rows = 0
        self.min_vals = {} # (pos[0], pos[1], num_cheats): val

    def is_wall(self, pos):
        return self.map[(pos[0], pos[1])] == '#'

    def get_adj_pos(self, pos):
        adj = [
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
        ]
        # if pos[2] < 2:
        #     adj.extend([(a[0], a[1], a[2]+1) for a in adj])

        adj = [a for a in adj if a[0] >= 0 and 
               a[0] < self.num_rows and a[1] >= 0 and a[1] < self.num_cols
                ]
        return adj

    def get_lines_from_pos(self, pos, length):
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        res = []
        for d in directions:
            spike = []
            add = True
            for l in range(1, length+1):
                a = (pos[0] + d[0] * l, pos[1] + d[1] * l)
                if not (a[0] >= 0 and a[0] < self.num_rows and a[1] >= 0 and a[1] < self.num_cols):
                    add = False
                    break
                spike.append(a)
            if add:
                res.append(spike)

        return res

    def process_line(self, line: str):
        """How to process each line in the input"""

        for col_idx, x in enumerate(line.strip()):
            self.map[(self.num_rows, col_idx)] = x
            if x == 'S':
                self.start_position = (self.num_rows, col_idx)
            elif x == 'E':
                self.end_position = (self.num_rows, col_idx)

        self.num_rows += 1
        self.num_cols = len(line.strip())

    # def print_min_vals(self):
    #     for i in range(self.num_rows):
    #         for j in range(self.num_cols):
    #             if (i, j) not in self.corrupted:
    #                 print(str(self.min_vals[(i, j)]) + ' ' * (4 - len(str(self.min_vals[(i, j)]))), end=' ')
    #             else:
    #                 print('■■■■', end = ' ')
    #         print()
    #     print()


    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        non_cheat_path = {}
        non_cheat_path[self.start_position] = 0
        cur = self.start_position
        idx = 0
        while cur != self.end_position:
            idx += 1
            adj_pos = self.get_adj_pos(cur)
            for a in adj_pos:
                if not self.is_wall(a) and a not in non_cheat_path:
                    non_cheat_path[a] = idx
                    cur = a
                    break
        # print(non_cheat_path)
        len_path = len(non_cheat_path) - 1

        path_lengths = Counter()
        for pos, start_idx in non_cheat_path.items():
            spikes = self.get_lines_from_pos(pos, length=2)
            for step1, step2 in spikes:
                if self.is_wall(step1) and not self.is_wall(step2):
                    delta = non_cheat_path[step2] - start_idx - 2
                    if delta > 0:
                        path_lengths[delta] += 1

        res = sum([v for k, v in path_lengths.items() if k >= 100])
        return res

        # self.print_corrupted()
        # for i in range(self.num_rows):
        #     for j in range(self.num_cols):
        #         for k in range(3):
        #             self.min_vals[(i, j, k)] = math.inf

        # self.min_vals[(0, 0, 0)] = 0
        # stack = [(0, 0, 0)]
        # while len(stack) > 0:
        #     # print(stack)
        #     head = stack[-1]
        #     stack.pop()

        #     adj_pos = self.get_adj_pos(head)
        #     for a in adj_pos:
        #         if not self.is_wall(a) and self.min_vals[a] > self.min_vals[head] + 1:
        #             self.min_vals[a] = self.min_vals[head] + 1
        #             stack.append(a)

        # # self.print_min_vals()
        # return self.min_vals[(self.num_cols-1), (self.num_rows-1)]

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

        

