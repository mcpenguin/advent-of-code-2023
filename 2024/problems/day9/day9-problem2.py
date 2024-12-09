import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        pass

    def process_line(self, line: str):
        """How to process each line in the input"""
        self.file = []
        self.file_indexes = [] # (n, start, end), end exclusive
        self.gap_indexes = [] # (start, end), end exclusive
        file_idx = 0
        idx = 0
        is_file = True

        for x in [int(x) for x in line if x != '\n']:
            if is_file:
                # self.file += [file_idx] * x
                self.file_indexes.append([file_idx, idx, idx + x])
                file_idx += 1
                is_file = False
            else:
                # self.file += [None] * x
                self.gap_indexes.append([idx, idx + x])
                is_file = True
            idx += x

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        self.file_indexes = self.file_indexes[::-1]
        self.new_positions = [] # (n, start, end)

        # print(self.file_indexes)
        # print(self.gap_indexes)

        file_indexes_idx = 0
        while file_indexes_idx < len(self.file_indexes):
            found_gap_for_file = False
            file_block = self.file_indexes[file_indexes_idx]
            file_sz = file_block[2] - file_block[1]
            
            for gap_block in self.gap_indexes:
                if file_block[2] <= gap_block[0]:
                    break
                gap_sz = gap_block[1] - gap_block[0]
                if file_sz <= gap_sz:
                    # print(file_indexes_idx, gap_block, file_block)
                    found_gap_for_file = True
                    self.new_positions.append([file_block[0], gap_block[0], gap_block[0] + file_sz])
                    gap_block[0] += file_sz
                    break

            if not found_gap_for_file:
                self.new_positions.append(file_block)
            file_indexes_idx += 1

        # compute checksum
        checksum = 0
        for n, start, end in self.new_positions:
            checksum += n * ((end - start) / 2 * (end + start - 1))
        return checksum
        

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

        

