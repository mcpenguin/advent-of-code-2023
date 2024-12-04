import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.is_first_line = True
        self.words = []

    def process_line(self, line: str):
        """How to process each line in the input"""

        self.words.append(line)

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # horizontal
        count = 0
        for i in range(len(self.words) - 2):
            for j in range(len(self.words[0]) - 2):
                if (
                    self.words[i+1][j+1] == 'A' and
                    len(set([self.words[i][j], self.words[i+2][j+2]]).intersection(['M', 'S'])) == 2 and
                    len(set([self.words[i+2][j], self.words[i][j+2]]).intersection(['M', 'S'])) == 2
                ):
                    count += 1
        return count

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

        

