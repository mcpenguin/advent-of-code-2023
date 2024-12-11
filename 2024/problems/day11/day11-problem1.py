import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        pass

    def process_line(self, line: str):
        """How to process each line in the input"""

        self.nums = line.strip().split(' ')

    def change_stone(self, num):
        if num == '0':
            return ['1']
        elif len(num) % 2 == 0:
            return [str(int(str(num[:len(num) // 2]))), str(int(str(num[len(num) // 2:])))]
        else:
            return [str(int(num) * 2024)]

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        iterations = 25
        for i in range(iterations):
            new_nums = []
            for num in self.nums:
                new_nums.extend(self.change_stone(num))
            self.nums = new_nums
        return len(self.nums)


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

        

