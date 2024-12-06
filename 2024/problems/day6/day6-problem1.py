import os
import sys


class Solution:
    """Class for solution"""

    def __init__(self):
        self.visited_positions = set()
        self.obstacles = set()
        self.current_position = (-1, -1)
        self.row_count = 0

    def process_line(self, line: str, row: int):
        """How to process each line in the input"""
        self.row_count += 1
        self.col_count = len(line)
        for col, x in enumerate(line):
            if line[col] == '#':
                self.obstacles.add((row, col))
            elif line[col] == '^':
                self.current_position = (row, col)

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # print(self.visited_positions)
        # print(self.obstacles)
        # print(self.current_position)
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        cur_dir_idx = 0
        print(self.row_count, self.col_count)
        self.visited_positions.add(self.current_position)

        while self.current_position[0] >= 0 and self.current_position[0] < self.row_count and \
                self.current_position[1] >= 0 and self.current_position[1] < self.col_count:
            # print(self.current_position)
            self.visited_positions.add(self.current_position)
            cur_dir = dirs[cur_dir_idx % len(dirs)]
            nextpos = (
                self.current_position[0] + cur_dir[0], self.current_position[1] + cur_dir[1])
            while nextpos in self.obstacles:
                cur_dir_idx += 1
                cur_dir = dirs[cur_dir_idx % len(dirs)]
                nextpos = (
                    self.current_position[0] + cur_dir[0], self.current_position[1] + cur_dir[1])
            self.current_position = nextpos

        return len(self.visited_positions)


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
        for pos, line in enumerate(file):
            solution_class.process_line(line, pos)

    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)
