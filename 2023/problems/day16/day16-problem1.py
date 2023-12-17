import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.grid = []
        self.num_rows = None
        self.num_cols = None
        self.energized = []
        self.next_beam_id = 1
        # dict to store beams: beam id
        self.beam_dict: dict[int, tuple[int, int, int, int]] = {0: (0, 0, 0, 1)} # beam id: (row_pos, col_pos, row_vel, col_vel)
        # row_vel: number of rows per turn (ie "y vel")
        # col_vel: number of cols per turn (ie "x vel")
        self.visited: set[tuple[int, int, int, int]] = set([])

    def process_line(self, line):
        """How to process each line in the input"""

        if line != '\n':
            self.grid.append(list(line[:-1]))

    def is_pos_valid(self, row_pos, col_pos):
        return row_pos >= 0 and row_pos < self.num_rows and \
            col_pos >= 0 and col_pos < self.num_cols
    
    def do_action(self, beam_idx):
        row_pos, col_pos, row_vel, col_vel = self.beam_dict[beam_idx]
        # if we've already encounted this state before
        # or if the position is invalid
        # then we delete the beam
        if not self.is_pos_valid(row_pos, col_pos) or \
            self.beam_dict[beam_idx] in self.visited:

            del self.beam_dict[beam_idx]
            return
        
        c = self.grid[row_pos][col_pos]
        self.energized[row_pos][col_pos] = 1
        self.visited.add(self.beam_dict[beam_idx])

        # mirror
        if c == '\\':
            if row_vel == 0 and col_vel == 1: # right
                self.beam_dict[beam_idx] = row_pos, col_pos, 1, 0 # down
            elif row_vel == 0 and col_vel == -1: # left
                self.beam_dict[beam_idx] = row_pos, col_pos, -1, 0 # up
            elif row_vel == 1 and col_vel == 0: # down
                self.beam_dict[beam_idx] = row_pos, col_pos, 0, 1 # right
            elif row_vel == -1 and col_vel == 0: # up
                self.beam_dict[beam_idx] = row_pos, col_pos, 0, -1 # left

            # self.visited.add(self.beam_dict[beam_idx])
            return
        elif c == '/':
            if row_vel == 0 and col_vel == 1: # right
                self.beam_dict[beam_idx] = row_pos, col_pos, -1, 0 # up
            elif row_vel == 0 and col_vel == -1: # left
                self.beam_dict[beam_idx] = row_pos, col_pos, 1, 0 # down
            elif row_vel == 1 and col_vel == 0: # down
                self.beam_dict[beam_idx] = row_pos, col_pos, 0, -1 # left
            elif row_vel == -1 and col_vel == 0: # up
                self.beam_dict[beam_idx] = row_pos, col_pos, 0, 1 # right

            # self.visited.add(self.beam_dict[beam_idx])
            return
        # split
        elif c == '|':
            if col_vel == 0: # vertical
                return
            elif row_vel == 0: # horizontal
                self.beam_dict[self.next_beam_id] = row_pos, col_pos, 1, 0
                self.visited.add(self.beam_dict[self.next_beam_id])
                self.beam_dict[self.next_beam_id + 1] = row_pos, col_pos, -1, 0
                self.visited.add(self.beam_dict[self.next_beam_id + 1])
                self.next_beam_id += 2

                del self.beam_dict[beam_idx]
                return
        elif c == '-':
            if row_vel == 0:
                return
            elif col_vel == 0:
                self.beam_dict[self.next_beam_id] = row_pos, col_pos, 0, 1
                self.visited.add(self.beam_dict[self.next_beam_id])
                self.beam_dict[self.next_beam_id + 1] = row_pos, col_pos, 0, -1
                self.visited.add(self.beam_dict[self.next_beam_id + 1])
                self.next_beam_id += 2

                del self.beam_dict[beam_idx]
                return
        elif c == '.':
            return
            
    def print_energized(self):
        for row in self.energized:
            for n in row:
                if n == 1:
                    c = '#'
                else:
                    c = '.'
                print(c, end="")
            print('\n')

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # init energized
        self.num_rows, self.num_cols = len(self.grid), len(self.grid[0])
        # print(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            self.energized.append([0]*self.num_cols)
        # simulate the beams  
        self.energized[0][0] = 1

        # do action for initial position
        self.do_action(0)
        while len(self.beam_dict) != 0:
            beam_idx = next(iter(self.beam_dict.keys()))
            row_pos, col_pos, row_vel, col_vel = self.beam_dict[beam_idx]
            # get new position
            new_row_pos = row_pos + row_vel
            new_col_pos = col_pos + col_vel
            self.beam_dict[beam_idx] = (new_row_pos, new_col_pos, row_vel, col_vel)
            # do action
            self.do_action(beam_idx) 

        # self.print_energized()
        return sum([sum(r) for r in self.energized])

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

        

