import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.current_elf_calories = 0
        self.elf_calories_list = []

    def process_line(self, line):
        """How to process each line in the input"""

        if line == '\n':
            self.elf_calories_list.append(self.current_elf_calories)
            self.current_elf_calories = 0
        else:
            self.current_elf_calories += int(line)

    def post_processing(self):
        """Function that is called after all the lines have been read"""
        self.elf_calories_list.append(self.current_elf_calories)

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        self.elf_calories_list.sort(reverse=True)
        return sum(self.elf_calories_list[0:3])

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

        

