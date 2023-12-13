import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.steps = []
        self.locations = {}

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line != '\n':
            if len(self.steps) == 0:
                self.steps = [c for c in line if c != '\n']
            else:
                split = line.split(" = ")
                start = split[0]                
                rest = split[1][1:-2].split(", ")
                self.locations[start] = rest


    def get_solution(self):
        print(self.locations)
        print(self.steps)
        cur_loc = 'AAA'
        num_steps = 0
        while cur_loc != 'ZZZ':
            for s in self.steps:
                num_steps += 1
                if s == 'L':
                    cur_loc = self.locations[cur_loc][0]
                else:
                    cur_loc = self.locations[cur_loc][1]
        return num_steps

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

        

