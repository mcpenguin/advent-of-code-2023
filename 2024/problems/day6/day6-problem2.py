import os
import sys
import copy


class Solution:
    """Class for solution"""

    def __init__(self):
        self.visited_positions = set()
        self.obstacles = set()
        self.original_position = (-1, -1)
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
                self.original_position = (row, col)

    def with_new_obstacle_has_loop(self, new_obs_pos):
        visited_positions_dirs = set()  # tuple, (row, col, dir % 4)

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        cur_dir_idx = 0
        self.current_position = self.original_position
        first = True

        while self.current_position[0] >= 0 and self.current_position[0] < self.row_count and \
                self.current_position[1] >= 0 and self.current_position[1] < self.col_count:

            visited_positions_dirs.add(
                (self.current_position[0], self.current_position[1], cur_dir_idx % 4))
            cur_dir = dirs[cur_dir_idx % len(dirs)]
            nextpos = (
                self.current_position[0] + cur_dir[0], self.current_position[1] + cur_dir[1])
            while nextpos in self.obstacles or nextpos == new_obs_pos:
                cur_dir_idx += 1
                cur_dir = dirs[cur_dir_idx % len(dirs)]
                nextpos = (
                    self.current_position[0] + cur_dir[0], self.current_position[1] + cur_dir[1])

            self.current_position = nextpos
            if not first and (self.current_position[0], self.current_position[1], cur_dir_idx % 4) in visited_positions_dirs:
                return True
            
            first = False

        return False

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        count = 0
        for i in range(self.row_count):
            for j in range(self.col_count):
                if self.with_new_obstacle_has_loop((i, j)):
                    count += 1

        return count


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
