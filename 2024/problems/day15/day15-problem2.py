import os
import sys
import copy

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
                row = []
                col_idx = 0
                for x in line.strip():
                    if x == '#':
                        row.extend(['#', '#'])
                    elif x == 'O':
                        row.extend(['[', ']'])
                    elif x == '.':
                        row.extend(['.', '.'])
                    elif x == '@':
                        row.extend(['@', '.'])
                        self.robot_position = (self.num_rows, col_idx)

                    col_idx += 2

                self.map.append(row)
                self.num_cols = len(line) * 2
                self.num_rows += 1
            else:
                self.actions.extend([x for x in line.strip()])

    def process_action(self, action):
        direction = {
            '^': (-1, 0),
            'v': (1, 0),
            '<': (0, -1),
            '>': (0, 1),
        }[action]
        obj_in_way = []
        cur_pos_list = set([(self.robot_position[0] + direction[0], self.robot_position[1] + direction[1])])
        next_cur_pos_list = set()
        all_empty_space = True
        stop = False
        while not stop:
            all_empty_space = True

            for cur_pos in copy.deepcopy(cur_pos_list):
                # print(cur_pos)
                if self.map[cur_pos[0]][cur_pos[1]] in ['[', ']']:
                    all_empty_space = False
                    obj_in_way.append((cur_pos, self.map[cur_pos[0]][cur_pos[1]]))

                    next_cur_pos_list.add((cur_pos[0] + direction[0], cur_pos[1] + direction[1]))

                    if direction[1] == 0: # vertical
                        if self.map[cur_pos[0]][cur_pos[1]] == '[':
                            next_cur_pos_list.add((cur_pos[0] + direction[0], cur_pos[1] + 1))
                            obj_in_way.append((
                                (cur_pos[0], cur_pos[1] + 1),
                                ']'
                            ))
                        else:
                            next_cur_pos_list.add((cur_pos[0] + direction[0], cur_pos[1] - 1))
                            obj_in_way.append((
                                (cur_pos[0], cur_pos[1] - 1),
                                '['
                            ))
                    else: # horizontal
                        next_cur_pos_list.add((cur_pos[0], cur_pos[1] + direction[1]))

                    next_cur_pos_list.discard(cur_pos)

                elif self.map[cur_pos[0]][cur_pos[1]] == '#':
                    all_empty_space = False
                    stop = True
                    break
            
            cur_pos_list = next_cur_pos_list
            if all_empty_space:
                stop = True

        if all_empty_space:
            for obj_pos, symbol in obj_in_way[::-1]:
                new_obj_pos = (obj_pos[0] + direction[0], obj_pos[1] + direction[1])
                self.map[obj_pos[0]][obj_pos[1]] = '.'
                self.map[new_obj_pos[0]][new_obj_pos[1]] = symbol

            new_robot_pos = (self.robot_position[0] + direction[0], self.robot_position[1] + direction[1])
            self.map[self.robot_position[0]][self.robot_position[1]] = '.'
            self.map[new_robot_pos[0]][new_robot_pos[1]] = '@'
            self.robot_position = new_robot_pos

    def print_state(self):
        for l in self.map:
            print(''.join(l))


    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        # self.print_state()
        # print()
        for a_idx, action in enumerate(self.actions):
            self.process_action(action)
            # print(a_idx+1, action)
            # self.print_state()
            # print()
        
        result = 0
        for i, l in enumerate(self.map):
            for j, x in enumerate(l):
                if x == '[':
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

        

