import os
import sys
import re

class Solution:
    """Class for solution"""

    def __init__(self):
        self.robots = {} # robot_idx: [pos, vel]
        self.robot_idx = 0
        self.height = 103 # 103
        self.width = 101 # 101

    def move_robot(self, robot_idx):
        p, v = self.robots[robot_idx]
        new_p = [(p[0] + v[0]) % self.width, (p[1] + v[1]) % self.height]
        self.robots[robot_idx] = [new_p, v]

    def safety_factor(self):
        quadrants = [
            [(0, self.width // 2), (0, self.height // 2)],
            [(0, self.width // 2), (self.height // 2 + 1, self.height)],
            [(self.width // 2 + 1, self.width), (0, self.height // 2)],
            [(self.width // 2 + 1, self.width), (self.height // 2 + 1, self.height)],

        ]
        counts = [0, 0, 0, 0]
        for robot in self.robots.values():
            for q_idx, quadrant in enumerate(quadrants):
                (x_low, x_high), (y_low, y_high) = quadrant
                if robot[0][0] >= x_low and robot[0][0] < x_high and \
                    robot[0][1] >= y_low and robot[0][1] < y_high:
                    counts[q_idx] += 1
                    break
        result = 1
        for count in counts:
            result *= count
        return result

    def process_line(self, line: str):
        """How to process each line in the input"""

        ps, vs = line.strip().split()
        p = [int(x) for x in re.split('=|,', ps) if x != 'p']
        v = [int(x) for x in re.split('=|,', vs) if x != 'v']
        self.robots[self.robot_idx] = [p, v]
        self.robot_idx += 1


    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        num_iterations = 100
        for i in range(num_iterations):
            for robot_idx in self.robots:
                self.move_robot(robot_idx)
        result = self.safety_factor()
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

        

