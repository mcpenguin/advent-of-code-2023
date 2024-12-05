import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.is_proc_seqs = False
        self.seqs = []
        self.orders = []
        # key: [values], v \in d[k] means that v cannot come before k
        self.valid = dict[int, set[int]]()

    def update_valid(self, order):
        after, before = order
        if after not in self.valid:
            self.valid[after] = set()
        if before in self.valid[after]:
            return
        
        self.valid[after].add(before)
        for next_before in self.valid[after]:
            self.update_valid([after, next_before])

    def is_seq_valid(self, seq):
        for i in range(0, len(seq)-1):
            cur = seq[i]
            after = set(seq[i+1:])
            if not all([cur in self.valid and x in (self.valid[cur]) for x in after]):
                return False
        return True


    def process_line(self, line: str):
        """How to process each line in the input"""
        if line == '\n':
            self.is_proc_seqs = True
        elif self.is_proc_seqs:
            seq = [int(x) for x in line.split(',')]
            self.seqs.append(seq)
        else:
            order = [int(x) for x in line.split('|')]
            self.orders.append(order)
            self.update_valid(order)

    def sort_seq(self, seq):
        # insertion sort because i'm too lazy
        # returns True if a < b
        def lt(a, b):
            return a in self.valid and b in (self.valid[a])
        result = []
        for x in seq:
            i = 0
            stop = False
            while not stop and i < len(result):
                if lt(x, result[i]):
                    result.insert(i, x)
                    stop = True
                i += 1
            if not stop:
                result.append(x)
        return result

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        result = 0
        for seq in self.seqs:
            if not self.is_seq_valid(seq):
                seq = self.sort_seq(seq)
                result += seq[len(seq) // 2]
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

        

