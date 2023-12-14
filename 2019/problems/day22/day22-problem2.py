import os
import sys
import copy

class Solution:
    """Class for solution"""

    def __init__(self):
        # self.num_cards = 10007
        self.num_cards = 100169

        self.cards = list(range(self.num_cards))
        self.shuffles = []
        self.num_iterations = 100000

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line != '\n':
            split = line[:-1].split(" ")
            if split[0] == 'cut':
                self.shuffles.append(('cut', int(split[1])))
            elif split[0] == 'deal' and split[1] == 'with':
                self.shuffles.append(('deal_with_increment', int(split[3])))
            elif split[0] == 'deal' and split[1] == 'into':
                self.shuffles.append(('deal_into_new_stack'))

    def get_pos_mapped_to_pos_in_shuffle(self, target_pos, shuffle):
        if shuffle == 'deal_into_new_stack':
            return self.num_cards - target_pos - 1
        elif shuffle[0] == 'cut':
            num = shuffle[1]
            if num < 0:
                num = self.num_cards + num
            if target_pos < self.num_cards - num:
                return target_pos + num
            else:
                return target_pos - (self.num_cards - num)
        elif shuffle[0] == 'deal_with_increment':
            num = shuffle[1]
            return target_pos * pow(num, -1, self.num_cards) % self.num_cards
        else:
            raise Exception('invalid shuffle encountered')

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        cards = copy.deepcopy(self.cards)
        positions_after_each_it = []
        # for it in range(self.num_iterations):
        cur_pos = 2019 # position we want
        positions_after_each_it.append(cur_pos)
        for it in range(self.num_iterations):
            for shuffle in self.shuffles[::-1]:
                cur_pos = self.get_pos_mapped_to_pos_in_shuffle(cur_pos, shuffle)
            
            try:
                index = positions_after_each_it.index(cur_pos)
            except:
                index = None
            if index is not None:
                print(f"Position after iteration {it+1} is the same as position after position after iteration {index}")
            positions_after_each_it.append(cur_pos)

        # print(cards)
        return cur_pos

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

        

