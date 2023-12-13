import os
import sys
import copy

class Solution:
    """Class for solution"""

    def __init__(self):
        self.seqs = []

    def is_diff_zero(self, diff):
        return all([x == 0 for x in diff])
    
    def get_elemwise_diffs(self, seq):
        res = []
        for i in range(0, len(seq)-1):
            res.append(seq[i+1] - seq[i])
        return res

    def get_next_e_of_seq(self, seq):
        diffs = []
        cur_diff = copy.deepcopy(seq)
        while not self.is_diff_zero(cur_diff):
            diffs.append(cur_diff)
            cur_diff = self.get_elemwise_diffs(cur_diff)
        diffs.append(cur_diff)
        
        diffs = diffs[::-1]
        # print(seq, diffs)
        cur_idx = 0
        diffs[cur_idx] = diffs[cur_idx] + [0]
        for cur_idx in range(1, len(diffs)):
            diff = diffs[cur_idx-1][-1]
            diffs[cur_idx].append(diff + diffs[cur_idx][-1])
        # print(diffs)
        # print()
        return diffs[len(diffs)-1][-1]

    def process_line(self, line):
        """How to process each line in the input"""

        if line == '\n':
            pass
        else:
            self.seqs.append([int(x) for x in line.split(" ")][::-1])

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        print(self.seqs)
        total = 0
        for seq in self.seqs:
            total += self.get_next_e_of_seq(seq)
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

    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

