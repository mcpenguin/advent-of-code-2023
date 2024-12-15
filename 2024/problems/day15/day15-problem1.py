import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.inp_actions = False
        self.map = []
        self.num_rows = 0
        self.actions = []

        self.robot_position = (0, 0)

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line == '\n':
            if not self.inp_actions:
                self.inp_actions = True
        else:
            if not self.inp_actions:
                self.map.append([x for x in line.strip()])
                self.num_cols = len(line)
                for col_idx, x in enumerate(line.strip()):
                    if x == '@':
                        self.robot_position = (self.num_rows, col_idx)
            else:
                self.actions.extend([x for x in line.strip()])
        
        self.num_rows += 1

    def process_action(self, action):
        direction = {
            '^': (-1, 0),
            'v': (1, 0),
            '<': (0, -1),
            '>': (0, 1),
        }[action]
        obj_in_way = []
        cur_pos = (self.robot_position[0] + direction[0], self.robot_position[1] + direction[1])
        while True:
            if self.map[cur_pos[0]][cur_pos[1]] == 'O':
                obj_in_way.append(cur_pos)
            elif self.map[cur_pos[0]][cur_pos[1]] == '#':
                break # wall
            elif self.map[cur_pos[0]][cur_pos[1]] == '.':
                # print(obj_in_way)
                for obj_pos in obj_in_way[::-1]:
                    new_obj_pos = (obj_pos[0] + direction[0], obj_pos[1] + direction[1])
                    self.map[obj_pos[0]][obj_pos[1]] = '.'
                    self.map[new_obj_pos[0]][new_obj_pos[1]] = 'O'

                new_robot_pos = (self.robot_position[0] + direction[0], self.robot_position[1] + direction[1])
                self.map[self.robot_position[0]][self.robot_position[1]] = '.'
                self.map[new_robot_pos[0]][new_robot_pos[1]] = '@'
                self.robot_position = new_robot_pos
                break

            cur_pos = (cur_pos[0] + direction[0], cur_pos[1] + direction[1])

    def print_state(self):
        for l in self.map:
            print(''.join(l))


    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        self.print_state()
        print()
        for a_idx, action in enumerate(self.actions):
            self.process_action(action)
            print(a_idx+1, action)
            self.print_state()
            print()
        
        result = 0
        for i, l in enumerate(self.map):
            for j, x in enumerate(l):
                if x == 'O':
                    result += 100 * i + j
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

        

