import os
import sys


class Solution:
    """Class for solution"""

    def __init__(self):
        self.map = []
        self.positions = {}  # (row_idx, col_idx): number or None
        self.row_idx = 0
        self.trailhead_pos = []

    def get_adj_pos(self, pos):
        adj = [
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
        ]
        adj = [a for a in adj if a[0] >= 0 and a[0] <
               self.num_rows and a[1] >= 0 and a[1] < self.num_cols]
        return adj

    def get_end_nodes(self, start_pos, start_num, ctx):
        if start_num == 9:
            return set([start_pos])
        adj = self.get_adj_pos(start_pos)
        adj = [a for a in adj if self.positions[a]
               == start_num + 1 and a not in ctx]
        if len(adj) == 0:
            return set()
        else:
            end_nodes = set()
            for a in adj:
                end_nodes = end_nodes.union(self.get_end_nodes(a, start_num + 1, ctx + [a]))
            return end_nodes
        
    def process_line(self, line: str):
        """How to process each line in the input"""

        for col_idx, x in enumerate(line.strip()):
            self.positions[(self.row_idx, col_idx)] = int(x)
            if x == '0':
                self.trailhead_pos.append((self.row_idx, col_idx))
        self.num_cols = col_idx + 1
        self.row_idx += 1

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        self.num_rows = self.row_idx

        self.result = 0
        for thead in self.trailhead_pos:
            self.result += len(self.get_end_nodes(thead, 0, [thead]))
        return self.result


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
