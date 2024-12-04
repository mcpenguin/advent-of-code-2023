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
        word = 'XMAS'
        count = 0
        for i in range(len(self.words)):
            for j in range(0, len(self.words[0]) - len(word) + 1):
                substr = ''.join([self.words[i][k] for k in range(j, j + len(word))])
                if substr == word:
                    print(i, j, 'h')
                    count += 1
                if substr == word[::-1]:
                    print(i, j, 'hr')
                    count += 1
        # vertical
        for i in range(len(self.words) - len(word) + 1):
            for j in range(0, len(self.words[0])):
                substr = ''.join([self.words[k][j] for k in range(i, i + len(word))])
                if substr == word:
                    print(i, j, 'v')
                    count += 1
                if substr == word[::-1]:
                    print(i, j, 'vr')
                    count += 1
        # diagonal right
        for i in range(len(self.words) - len(word) + 1):
            for j in range(len(self.words[0]) - len(word) + 1):
                substr = ''.join([self.words[i+k][j+k] for k in range(len(word))])
                if substr == word:
                    print(i, j, 'dr')
                    count += 1
                if substr == word[::-1]:
                    print(i, j, 'drr')
                    count += 1
        # diagonal left
        for i in range(len(self.words) - len(word) + 1):
            for j in range(len(word) - 1, len(self.words[0])):
                substr = ''.join([self.words[i+k][j-k] for k in range(len(word))])
                if substr == word:
                    print(i, j, 'dl')
                    count += 1
                if substr == word[::-1]:
                    print(i, j, 'dlr')
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

        

