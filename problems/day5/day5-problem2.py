import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.seed_ranges = [] # [(seed num, range len)]
        self.maps_list = [] # list of [(dest range start, source range start, range length)]
        self.curMap = []

    # assume input, source ranges are sorted in ascending order of their starts
    def split_input_range_by_source(self, input_ranges, source_ranges):
        input_ranges.sort(key=lambda x: x[0])
        source_bounds = list(set([s[0] for s in source_ranges] + [s[0] + s[1] for s in source_ranges]))
        source_bounds.sort()

        split_ints = []
        for input_range in input_ranges:
            start, end = input_range[0], input_range[0] + input_range[1]
            intermed = [s for s in source_bounds if s >= start and s < end]
            if len(intermed) == 0:
                split_ints.append(input_range)
            else:
                cur = start
                for inter in intermed + [end]:
                    pair = (cur, inter - cur + 1)
                    cur = inter
                    split_ints.append(pair)
        return split_ints


    # input_ranges: [(source, range_len), ...]
    # source_dest_map: [(dest, source, range_len), ...]
    # output: [(dest, range_len), ...]
    def map_from_source_to_dest(self, source_dest_map, input_ranges):
        source_ranges = [(s[1], s[2]) for s in source_dest_map]
        input_ranges_split = self.split_input_range_by_source(input_ranges, source_ranges)
        # Now input ranges are all "Disjoint" from the source ranges,
        # so we can just pass this directly into our map and reuse the same code
        output_range = []
        for input_start, input_len in input_ranges_split:
            isInMap = False
            for dest_range_start, source_range_start, range_len in source_dest_map:
                diff_source = input_start - source_range_start
                if diff_source >= 0 and diff_source < range_len:
                    output_range.append((dest_range_start + diff_source, input_len))
                    isInMap = True
                    continue
            if not isInMap:
                output_range.append((input_start, input_len))

        output_range.sort(key=lambda x: x[0])
        return output_range

    def process_line(self, line: str):
        """How to process each line in the input"""
        if len(self.seed_ranges) == 0: # seeds line
            split = [int(x) for x in line.replace('\n', '').split(': ')[1].split(' ')]
            for i in range(0, len(split), 2):
                self.seed_ranges += [(split[i], split[i+1])]
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
        destination_ranges = self.seed_ranges
        for sdmap in self.maps_list:
            destination_ranges = self.map_from_source_to_dest(sdmap, destination_ranges)
        return destination_ranges[0][0]

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

        

