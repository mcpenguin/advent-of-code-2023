import os
import sys
from collections import Counter

class Solution:
    """Class for solution"""

    def __init__(self):
        self.seeds = []

    def process_line(self, line: str):
        """How to process each line in the input"""

        self.seeds.append(int(line.strip()))

    def mix(self, n1, n2):
        return n1 ^ n2
    
    def prune(self, n1):
        return n1 % 16777216
    
    def get_next(self, n):
        r = n * 64
        n = self.mix(n, r)
        n = self.prune(n)
        r = n // 32
        n = self.mix(n, r)
        n = self.prune(n)
        r = n * 2048
        n = self.mix(n, r)
        n = self.prune(n)
        return n


    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        it = 2000
        hist = (0, 0, 0, 0)
        all_counter = Counter()
        for seed in self.seeds:
            counter = Counter()
            cur = seed
            for i in range(it):
                nxt = self.get_next(cur)
                delta = (nxt % 10) - (cur % 10)
                hist = (hist[1], hist[2], hist[3], delta)
                if i >= 3 and hist not in counter:
                    counter[hist] = nxt % 10
                cur = nxt

            for k, v in counter.items():
                all_counter[k] += v

        # print(all_counter)
        return max(all_counter.values())

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

        

