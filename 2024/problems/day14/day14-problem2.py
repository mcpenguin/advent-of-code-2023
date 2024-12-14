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

    def get_adj_pos(self, pos, care_abt_bounds = True):
        adj = [
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
        ]
        if care_abt_bounds:
            adj = [a for a in adj if a[0] >= 0 and a[0] <
                self.height and a[1] >= 0 and a[1] < self.height]
        return adj

    def max_region_size(self):
        region_list = []
        positions = set([tuple(r[0]) for r in self.robots.values()])
        while len(positions) > 0:
            current_region = set()
            start = next(iter(positions))
            stack = [start]
            while len(stack) > 0:
                head = stack[-1]
                current_region.add(head)
                adj = self.get_adj_pos(head)
                neighbors = [pos for pos in adj if pos in positions and pos not in current_region]
                
                stack.pop()
                positions.discard(head)
                stack.extend(neighbors)

            region_list.append(current_region)
            current_region = set()
        
        return max([len(region) for region in region_list])

    def print_robots(self, ppp=False):
        # print(self.height)
        s = []
        c = []
        for i in range(self.height):
            s.append([' '] * self.width)
            c.append([0] * self.width)
        # print(len(s), len(s[0]))
        for robot in self.robots.values():
            p = robot[0]
            # print(p)
            s[p[1]][p[0]] = '■'
            c[p[1]][p[0]] += 1
        m = 0
        for i in range(self.height):
            for j in range(self.width):
                m = max(m, c[i][j])
        if ppp:
            print('-'*25)
            for ss in s:
                print(''.join(ss))
            print('-'*25)
        return m

    def uniq_positions(self):
        return len(set([tuple(r[0]) for r in self.robots.values()]))

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # num_iterations = self.width * self.height
        num_iterations = 50000
        for i in range(num_iterations):
            for robot_idx in self.robots:
                self.move_robot(robot_idx)

            max_region_size = self.max_region_size()
            if max_region_size > 30:  
                print(i+1, self.max_region_size())
                self.print_robots(ppp=True)

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

        

