import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.board = []
        self.start_pos = (-1, -1)

    def get_dir_dict(self, cur_pos):
        return {
            'N': (cur_pos[0] - 1, cur_pos[1]),
            'S': (cur_pos[0] + 1, cur_pos[1]),
            'W': (cur_pos[0], cur_pos[1] - 1),
            'E': (cur_pos[0], cur_pos[1] + 1),
        }

    def process_line(self, line: str, row_idx: int):
        """How to process each line in the input"""

        if line != '\n':
            l = []
            for col_idx, c in enumerate(line):
                if c != '\n':
                    e = {
                        '|': ['N', 'S'],
                        '-': ['W', 'E'],
                        'L': ['N', 'E'],
                        'J': ['N', 'W'],
                        '7': ['S', 'W'],
                        'F': ['S', 'E'],
                        '.': [],
                        'S': ['Start'],
                    }[c]
                    l.append(e)
                if c == 'S':
                    self.start_pos = (row_idx, col_idx)

            self.board.append(l)

    def get_opposite(self, dir):
        return {
            'N': 'S',
            'S': 'N',
            'W': 'E',
            'E': 'W'
        }[dir]

    def get_valid_directions(self, cur_pos):
        val_dirs = []
        cur_e = self.board[cur_pos[0]][cur_pos[1]]
        for d, (r, c) in self.get_dir_dict(cur_pos).items():
            if (d in cur_e or 'Start' in cur_e) and self.get_opposite(d) in self.board[r][c]:
                val_dirs.append(d)

        return val_dirs

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        cur_pos = self.start_pos
        prev_pos = self.start_pos
        loop = [cur_pos]
        d = self.get_valid_directions(cur_pos)[0]

        cur_pos = self.get_dir_dict(cur_pos)[d]

        while cur_pos != self.start_pos:
            loop.append(cur_pos)

            ds = self.get_valid_directions(cur_pos)
            next_positions = [self.get_dir_dict(cur_pos)[d] for d in ds if self.get_dir_dict(cur_pos)[d] != prev_pos]
            if len(next_positions) == 0:
                break
            next_pos = next_positions[0]
            
            prev_pos = cur_pos
            cur_pos = next_pos
        
        return len(loop) // 2

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
        for col_idx, line in enumerate(file):
            solution_class.process_line(line, col_idx)

    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

