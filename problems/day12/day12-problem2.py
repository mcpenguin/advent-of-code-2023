import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.records = []
        self.counts = []
        self.multiplier = 5

        # 2D array for memoization
        # (record idx, count idx)
        self.memo_array = []

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line != '\n':
            split = line.split(" ")
            record = []
            for i in range(self.multiplier-1):
                record.extend(list(split[0]))
                record.append('?')
            record.extend(list(split[0]))

            self.records.append(record)
            self.counts.append([int(x) for x in split[1].replace('\n', '').split(',')]*self.multiplier)

    # Returns tuple of num_arrangements, num_arrangements_that_use_last_position
    def get_num_arrangements_for_record(self, 
        record, counts, cum_count, cur_record_idx=0, cur_count_idx=0) -> int:

        if cur_count_idx == len(counts):
            if '#' not in record[cur_record_idx:]:
                return 1
            else:
                return 0
        if len(record) - cur_record_idx < cum_count + len(counts) - cur_count_idx - 1:
            if len(record) - cur_record_idx == 0:
                return 0
            else:
                return 0
        if self.memo_array[cur_record_idx][cur_count_idx] != -1:
            return self.memo_array[cur_record_idx][cur_count_idx]
        
        total = 0
        num_arr_that_use_last_spot = 0

        # We use sliding windows
        i = cur_record_idx
        head_counts = counts[cur_count_idx]
        num_dot_in_window = record[i:i+head_counts].count('.')
        while i <= len(record) - head_counts:
            if num_dot_in_window == 0 and \
                (i+head_counts == len(record) or record[i+head_counts] != '#'):

                num_arr = self.get_num_arrangements_for_record(
                    record = record, 
                    counts = counts,
                    cur_record_idx = i + head_counts + 1,
                    cur_count_idx = cur_count_idx + 1,
                    cum_count = cum_count - head_counts
                )
                total += num_arr

            # Update sliding window values if while condition is still vallid
            if i < len(record) - head_counts:
                if record[i] == '#':
                    break
                if record[i] == '.':
                    num_dot_in_window -= 1
                if record[i+head_counts] == '.':
                    num_dot_in_window += 1

            i += 1

        # Update memo array
        if self.memo_array[cur_record_idx][cur_count_idx] == -1:
            self.memo_array[cur_record_idx][cur_count_idx] = total

        return total

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""

        total = 0
        for idx, (record, count) in enumerate(zip(self.records, self.counts)):
            # Initialize memo dict
            self.memo_array = []
            for i in range(len(record)):
                self.memo_array.append([-1]*len(count))
            num_arr = self.get_num_arrangements_for_record(record, count, sum(count))
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

        

