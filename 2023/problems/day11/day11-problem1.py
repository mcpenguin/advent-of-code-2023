import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.image = []
        self.galaxy_coords = []
        self.rows_with_no_galax = []
        self.cols_with_no_galax = []

    def get_cell(self, pos):
        return self.image[pos[0]][pos[1]]

    def process_line(self, line, row_idx):
        """How to process each line in the input"""
        r = []
        for col_idx, c in enumerate(line):
            if c != '\n':
                r.append(c)
            if c == '#':
                self.galaxy_coords.append((row_idx, col_idx))
        self.image.append(r)

    def get_dist_between_pos(self, pos1, pos2):
        x = abs(pos1[0] - pos2[0])
        y = abs(pos1[1] - pos2[1])
        if pos1[0] <= pos2[0]:
            num_rows_no_galax = len([e for e in self.rows_with_no_galax if pos1[0] < e and e < pos2[0]])
        else:
            num_rows_no_galax = len([e for e in self.rows_with_no_galax if pos2[0] < e and e < pos1[0]])
        
        if pos1[1] <= pos2[1]:
            num_cols_no_galax = len([e for e in self.cols_with_no_galax if pos1[1] < e and e < pos2[1]])
        else:
            num_cols_no_galax = len([e for e in self.cols_with_no_galax if pos2[1] < e and e < pos1[1]])

        return x + y + num_rows_no_galax + num_cols_no_galax

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # print(self.image)
        # print(self.galaxy_coords)
        for row_idx in range(len(self.image)):
            if all([self.get_cell((row_idx, col_idx)) == '.' for col_idx in range(len(self.image[0]))]):
                self.rows_with_no_galax.append(row_idx)
        for col_idx in range(len(self.image[0])):
            if all([self.get_cell((row_idx, col_idx)) == '.' for row_idx in range(len(self.image))]):
                self.cols_with_no_galax.append(col_idx)
        # print(self.rows_with_no_galax, self.cols_with_no_galax)

        total = 0
        for i in range(len(self.galaxy_coords)):
            for j in range(i, len(self.galaxy_coords)):
                pos1 = self.galaxy_coords[i]
                pos2 = self.galaxy_coords[j]
                total += self.get_dist_between_pos(pos1, pos2)

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
        for row_idx, line in enumerate(file):
            solution_class.process_line(line, row_idx)

    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

