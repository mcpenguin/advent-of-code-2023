import os
import sys
import heapq
import math

class Solution:
    """Class for solution"""

    def __init__(self):
        self.corrupted = set()
        self.num_cols = 71
        self.num_rows = 71
        self.limit = 3011
        self.min_vals = {}
        self.it = 0

    def get_adj_pos(self, pos, care_abt_bounds = True):
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

        x, y = [int(x) for x in line.strip().split(',')]
        if self.it < self.limit:
            self.corrupted.add((y, x)) # x, y
        self.it += 1

    def print_corrupted(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if (i, j) in self.corrupted:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print()

    def print_min_vals(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if (i, j) not in self.corrupted:
                    print(str(self.min_vals[(i, j)]) + ' ' * (4 - len(str(self.min_vals[(i, j)]))), end=' ')
                else:
                    print('■■■■', end = ' ')
            print()
        print()


    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # self.print_corrupted()
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.min_vals[(i, j)] = math.inf

        self.min_vals[(0, 0)] = 0
        stack = [(0, 0)]
        while len(stack) > 0:
            # print(stack)
            head = stack[-1]
            stack.pop()
            if head in self.corrupted:
                continue
            adj_pos = self.get_adj_pos(head)
            # print(head, adj_pos)
            for a in adj_pos:
                if a not in self.corrupted and self.min_vals[a] > self.min_vals[head] + 1:
                    self.min_vals[a] = self.min_vals[head] + 1
                    stack.append(a)

        self.print_min_vals()
        return self.min_vals[(self.num_cols-1), (self.num_rows-1)]

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

        

