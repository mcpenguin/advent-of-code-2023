import os
import sys
import re

class Solution:
    """Class for solution"""

    def __init__(self):
        self.proc_reg = True
        self.registers = {}
        self.instruction_ptr = 0
        self.instructions = []
        self.output = []

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line == '\n':
            self.proc_reg = False
        else:
            if self.proc_reg:
                inp = re.split(': | ', line.strip())
                self.registers[inp[1]] = int(inp[2])
            else:
                inp = re.split(': |,', line.strip())
                self.instructions = [int(x) for x in inp[1:]]

    def get_combo_operand(self, operand):
        if 0 <= operand and operand <= 3:
            return operand
        elif 4 <= operand and operand <= 6:
            return self.registers[['A', 'B', 'C'][operand - 4]]
        else:
            return 0
        

    def process_instruction(self, opcode, operand):
        increase_instr_ptr = True
        if opcode == 0: # adv
            self.registers['A'] = self.registers['A'] // (2 ** self.get_combo_operand(operand))
        elif opcode == 1:
            self.registers['B'] = self.registers['B'] ^ operand
        elif opcode == 2:
            self.registers['B'] = self.get_combo_operand(operand) % 8
        elif opcode == 3:
            if self.registers['A'] == 0:
                pass
            else:
                self.instruction_ptr = operand
                increase_instr_ptr = False
        elif opcode == 4:
            self.registers['B'] = self.registers['B'] ^ self.registers['C']
        elif opcode == 5:
            self.output.append(self.get_combo_operand(operand) % 8)
        elif opcode == 6:
            self.registers['B'] = self.registers['A'] // (2 ** self.get_combo_operand(operand))
        elif opcode == 7:
            self.registers['C'] = self.registers['A'] // (2 ** self.get_combo_operand(operand))

        if increase_instr_ptr:
            self.instruction_ptr += 2
        return
        


    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        print(self.instructions)
        self.instruction_ptr = 0
        while self.instruction_ptr < len(self.instructions):
            opcode = self.instructions[self.instruction_ptr]
            operand = self.instructions[self.instruction_ptr + 1]
            # print(opcode, operand, self.instruction_ptr)
            self.process_instruction(opcode, operand)

        return ','.join([str(x) for x in self.output])


        

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

        

