import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.total = 0

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line != '\n':
            line = line.replace('\n', '').replace('  ', ' ')
            game_txt, nums = line.split(':')
            split = nums.split(' | ')
            winning_nums = [int(n) for n in split[0].strip().split(' ')]
            our_nums = [int(n) for n in split[1].strip().split(' ')]

            num_matches = len(set(winning_nums).intersection(set(our_nums)))
            if num_matches >= 1:
                self.total += 2 ** (num_matches - 1)


    def post_processing(self):
        """Function that is called after all the lines have been read"""
        pass

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        return self.total

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
    solution_class.post_processing()
    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

