import os
import sys
from collections import defaultdict
import copy

class Solution:
    """Class for solution"""

    def __init__(self):
        self.map = []
        self.positions = defaultdict[str, set]()
        self.region_indexes = defaultdict[str, int]()
        self.num_rows = 0

    def get_adj_pos(self, pos, care_abt_bounds = True):
        adj = [
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
        ]
        if care_abt_bounds:
            adj = [a for a in adj if a[0] >= 0 and a[0] <
                self.num_rows and a[1] >= 0 and a[1] < self.num_cols]
        return adj

    def get_perimeter(self, region):
        total_perimeter = len(region) * 4
        for pos in region:
            num_adj = len([x for x in self.get_adj_pos(pos, care_abt_bounds=False) if x in region])
            total_perimeter -= num_adj
        return total_perimeter
    
    def sep_into_regions(self, c):
        region_list = []
        positions = copy.deepcopy(self.positions[c])
        while len(positions) > 0:
            current_region = set()
            start = next(iter(positions))
            stack = [start]
            while len(stack) > 0:
                head = stack[-1]
                current_region.add(head)
                adj = self.get_adj_pos(head)
                neighbors = [pos for pos in adj if pos in self.positions[c] and pos not in current_region]
                
                stack.pop()
                positions.discard(head)
                stack.extend(neighbors)

            region_list.append(current_region)
            current_region = set()
        
        return region_list
            


    def process_line(self, line: str):
        """How to process each line in the input"""

        self.map.append(line.strip())
        for col_idx, x in enumerate(line.strip()):
            if x not in self.positions:
                self.positions[x] = set()

            self.positions[x].add((self.num_rows, col_idx))
        self.num_rows += 1
        self.num_cols = col_idx + 1

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        all_region_list = []
        for c in self.positions.keys():
            all_region_list.extend(self.sep_into_regions(c))

        result = 0
        for region in all_region_list:
            area = len(region)
            perimeter = self.get_perimeter(region)
            price = area * perimeter
            result += price
            print(c, area, perimeter)
        return result

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

        

