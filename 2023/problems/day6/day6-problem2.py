import os
import sys
import re

class Solution:
    """Class for solution"""

    def __init__(self):
        self.times = {} # race n: time
        self.distances = {}

    def calc_dist(self, total_time, time_charged):
        return (total_time - time_charged) * time_charged

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line == '\n':
            pass
        else:
            split = line.split(':')
            rest = [x for x in split[1].strip().replace(' +', ' ').split(' ')
                    if x != '']
            v = int(''.join(rest))
            if split[0] == 'Time':
                self.times[0] = v
            else:
                self.distances[0] = v

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        total = 1
        for time, distance in zip(self.times.values(), self.distances.values()):
            num_record_beat = 0
            for t in range(time):
                if self.calc_dist(time, t) > distance:
                    num_record_beat += 1
            total *= num_record_beat
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
        for line in file:
            solution_class.process_line(line)
    solution_class.process_line('\n')

    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

