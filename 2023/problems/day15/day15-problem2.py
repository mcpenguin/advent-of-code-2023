import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.seq = [] # (label, operation, num?)
        self.boxes = {i: [] for i in range(256)} # each list has tuple (label, focal length)

    def split(self, txt):
        if '-' in txt:
            split = txt.split('-')
            return (split[0], '-')
        else:
            split = txt.split('=')
            return (split[0], '=', int(split[1]))

    def process_line(self, line):
        """How to process each line in the input"""

        if line != '\n':
            split = line[:-1].split(',')
            self.seq = [self.split(txt) for txt in split]

    def get_hash(self, text):
        total = 0
        for c in text:
            total = ((total + ord(c)) * 17) % 256
        return total

    def do_operation(self, tup):
        label = tup[0]
        op = tup[1]
        box_num = self.get_hash(label)
        if op == '-':
            try:
                labels = [x[0] for x in self.boxes[box_num]]
                index = labels.index(label)
                del self.boxes[box_num][index]
            except:
                pass
        elif op == '=':
            focal_len = tup[2]
            try:
                labels = [x[0] for x in self.boxes[box_num]]
                index = labels.index(label)
                self.boxes[box_num][index] = (label, focal_len)
            except: # label not found
                self.boxes[box_num].append((label, focal_len))

    def get_focusing_power(self):
        total = 0
        for idx, box in self.boxes.items():
            for pos_idx, (label, focal_len) in enumerate(box):
                total += (1 + idx) * (1 + pos_idx) * focal_len
        return total


    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        for tup in self.seq:
            self.do_operation(tup)
        return self.get_focusing_power()

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

        

