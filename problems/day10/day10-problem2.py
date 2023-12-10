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
        start_dirs = self.get_valid_directions(cur_pos)
        d = start_dirs[0]

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
        
        loop.sort()
        self.board[self.start_pos[0]][self.start_pos[1]] = start_dirs

        total = 0
        for r in range(len(self.board)):
            loop_fil = [p for p in loop if p[0] == r]
            loop_fil_not_we = [p for p in loop_fil if self.board[p[0]][p[1]] != ['W', 'E']]
            subtotal = 0
            isIn = False
            # print(loop_fil_not_we)
            
            # We consider successive consecutive instances of "vertical" pipes;
            # ie pipes which are not NE
            for i in range(0, len(loop_fil_not_we)-1):
                end = loop_fil_not_we[i+1][1]
                start = loop_fil_not_we[i][1]
                # print(start, end, isIn)

                start_dirs = self.board[r][start]
                end_dirs = self.board[r][end]

                # Case 1: both directions of the pair are not NS,
                # and they form a "U" shape (LJ or F7), or a "tri" shape (JL or 7F).
                # This means that the directions is either a horizontal 'border' of the pipe,
                # or just came after it.
                # In this case, we "maintain" the value of isIn.
                if (start_dirs == ['N', 'E'] and end_dirs == ['N', 'W']) or \
                    (start_dirs == ['S', 'E'] and end_dirs == ['S', 'W']):
                    pass
                # Case 2: both directions of the pair are not NS,
                # and they form a "cubic" shape (L7 or FJ).
                # This means that the directions is a horizontal 'border' of the pipe.
                # In this case, we "invert" the value of isIn.
                elif (start_dirs == ['N', 'E'] and end_dirs == ['S', 'W']) or \
                    (start_dirs == ['S', 'E'] and end_dirs == ['N', 'W']):
                    isIn = not isIn

                elif (start_dirs == ['N', 'S']):

                    isIn = not isIn
                    if isIn:
                        subtotal += end - start - 1
                    # isIn = not isIn

                elif (start_dirs == ['N', 'W'] and end_dirs == ['N', 'S']) or \
                    (start_dirs == ['S', 'W'] and end_dirs == ['N', 'S']) or \
                    (start_dirs == ['N', 'W'] and end_dirs == ['N', 'E']) or \
                    (start_dirs == ['S', 'W'] and end_dirs == ['S', 'E']) or \
                    (start_dirs == ['N', 'W'] and end_dirs == ['S', 'E']) or \
                    (start_dirs == ['S', 'W'] and end_dirs == ['N', 'E']) :

                    if isIn:
                        subtotal += end - start - 1
                    # isIn = not isIn

                # Case 4: both directions forms an "inverted" tri shape
                # We invert isIn. If isIn is true, add the number of empty spaces
                # to the total
                # elif (start_dirs == ['N', 'W'] and end_dirs == ['S', 'E']) or \
                #     (start_dirs == ['S', 'W'] and end_dirs == ['N', 'E']):
                #     # isIn = not isIn
                #     if isIn:
                #         subtotal += end - start - 1
                # Case 5: Anything else; the pipes are *not* a border of the pipe.
                # W invert isIn. If isIn is true, add the number of empty spaces
                # to the total
                else:
                    raise Exception(f"unexpected: start={start_dirs}, end={end_dirs}")
                    # isIn = not isIn
                    # if isIn:
                    #     subtotal += end - start - 1

            # subtotal -= len(loop_fil_we)
            # print(subtotal)

            total += subtotal
            # for i in range(0, )
        # print(loop)
        
        
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
        for col_idx, line in enumerate(file):
            solution_class.process_line(line, col_idx)

    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

