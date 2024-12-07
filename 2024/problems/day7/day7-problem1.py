import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.current_elf_calories = 0
        self.elf_calories_list = []
        self.result = 0

    def process_line(self, line: str):
        """How to process each line in the input"""
        sol, nlist = line.split(': ')
        sol = int(sol)
        nlist = [int(x) for x in nlist.split()]
        if self.is_eqn_poss(nlist, sol):
            self.result += sol
        
    def is_eqn_poss(self, nlist, sol):
        alist_poss = self.gen_alist_poss(len(nlist) - 1)
        for alist in alist_poss:
            if self.get_results_of_eqn(nlist, alist) == sol:
                return True
        return False

    def gen_alist_poss(self, length):
        if length == 0:
            return []
        else:
            ll = self.gen_alist_poss(length - 1)
            addl = [l + ['+'] for l in ll]
            mull = [l + ['*'] for l in ll]
            conl = [l + ['||'] for l in ll]
            return addl + mull + conl

    def get_results_of_eqn(self, nlist, alist):
        result = nlist[0]
        for i in range(len(nlist)-1):
            a = alist[i]
            n = nlist[i+1]
            if a == '+':
                result += n
            elif a == '*':
                result *= n
            elif a == '||':
                result = result * 10 + n
        return result

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        return self.result

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

        

