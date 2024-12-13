import os
import sys
import numpy as np
from scipy.linalg import lu


class Solution:
    """Class for solution"""

    def __init__(self):
        self.games = []
        self.game = []

    def process_line(self, line: str):
        """How to process each line in the input"""
        if line == '\n':
            self.games.append(self.game)
            self.game = []
        else:
            inp = line.strip().split(': ')
            lhs = inp[0]
            rhs = inp[1].split(', ')
            if 'Button' in lhs:
                x = int(rhs[0].split('+')[1])
                y = int(rhs[1].split('+')[1])
                self.game.append([x, y])
            else:
                x = int(rhs[0].split('=')[1])
                y = int(rhs[1].split('=')[1])
                self.game.append([x, y])

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        """
        min(button_a_pressed * 3 + button_b_pressed * 1)
        0 <= button_a_pressed <= 100
        0 <= button_b_pressed <= 100
        a_x * button_a_pressed + b_x * button_b_pressed = prize_x
        a_y * button_a_pressed + b_y * button_b_pressed = prize_y

        [[a_x, a_y], [b_x, b_y]] * [button_a, button_b] = [prize_x, prize_y]
        
        """
        self.games.append(self.game)
        # print(self.games)
        result = 0
        for game in self.games:
            # print(game)
            button_a, button_b, prize = game
            a_x, a_y = button_a
            b_x, b_y = button_b
            prize_x, prize_y = prize

            mat = np.array([[a_x, b_x], [a_y, b_y]])
            prize = np.array([prize_x, prize_y]) + 10000000000000
            # pl, u = lu(mat, permute_l=True)
            # print(u)
            presses = np.round(np.linalg.matmul(np.linalg.inv(mat), prize), decimals=0)
            # print(np.linalg.matrix_rank(mat), presses)
            if np.array_equal(np.linalg.matmul(mat, presses), prize):
                # min(presses) >= 0 and max(presses) <= 100:
                # solution valid
                # print('yes')
                result += np.dot(presses, np.array([3, 1]))

        return result
                


# don't change this
if __name__ == '__main__':
    solution_class = Solution()
    assert len(
        sys.argv) > 1, "Please provide the name of the input file in the second terminal argument."
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
