import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.records = []
        self.counts = []

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line != '\n':
            split = line.split(" ")
            self.records.append(list(split[0]))
            self.counts.append([int(x) for x in split[1].replace('\n', '').split(',')])

    def get_num_arrangements_for_record(self, record, counts):
        # print(record, counts)
        if len(counts) == 0:
            if '#' not in record:
                return 1
            else:
                return 0
        # if len(record) == sum(counts):
        #     if len(set(record)) == 1 and '.' not in record:
        #         return 1
        #     else:
        #         return 0
        if len(record) < sum(counts) + len(counts) - 1:
            return 0
        
        total = 0
        for i in range(0, len(record) - counts[0] + 1):
            if '#' not in set(record[:i]) and \
                '.' not in set(record[i:i+counts[0]]) and \
                (i+counts[0] == len(record) or record[i+counts[0]] != '#'):
                total += self.get_num_arrangements_for_record(
                    record[i+counts[0]+1:], 
                    counts[1:]
                )
        return total

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        total = 0
        for record, count in zip(self.records, self.counts):
            num_arr = self.get_num_arrangements_for_record(record, count)
            # print(num_arr)
            # crash
            total += num_arr
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

        

