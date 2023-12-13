import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.seeds = []
        self.maps_list = [] # list of [(dest range start, source range start, range length)]
        self.curMap = []

    def map_from_source_to_dest(self, source_dest_map, source):
        for dest_range_start, source_range_start, range_len in source_dest_map:
            diff_source = source - source_range_start
            if diff_source >= 0 and diff_source < range_len:
                return dest_range_start + diff_source
        return source

    def process_line(self, line: str):
        """How to process each line in the input"""
        if len(self.seeds) == 0: # seeds line
            self.seeds = [int(x) for x in line.replace('\n', '').split(': ')[1].split(' ')]
        elif line == '\n':
            if len(self.curMap) > 0:
                self.maps_list.append(self.curMap)
                self.curMap = []
        else: # maps line
            if line.split(' ')[0].isdigit():
                dest_range_start, source_range_start, range_len = [int(x) for x in line.split(' ')]
                self.curMap += [(dest_range_start, source_range_start, range_len)]

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        destinations = self.seeds
        for sdmap in self.maps_list:
            destinations = [self.map_from_source_to_dest(sdmap, seed) for seed in destinations] 
        return min(destinations)

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
        for idx, line in enumerate(file):
            solution_class.process_line(line)
    solution_class.process_line('\n')
    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

