import os
import sys
import copy

class Solution:
    """Class for solution"""

    def __init__(self):
        self.total = 0
        self.original_cards = {} # card n: (num of matches)

    def process_line(self, line: str):
        """How to process each line in the input"""

        if line != '\n':
            line = line.replace('\n', '').replace('  ', ' ')
            game_txt, nums = line.split(':')
            card_num = game_txt.split(' ')[-1]
            split = nums.split(' | ')
            winning_nums = [int(n) for n in split[0].strip().split(' ')]
            our_nums = [int(n) for n in split[1].strip().split(' ')]

            num_matches = len(set(winning_nums).intersection(set(our_nums)))
            self.original_cards[int(card_num)] = num_matches


    def post_processing(self):
        """Function that is called after all the lines have been read"""
        pass

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        max_card = max(self.original_cards.keys())
        total = len(self.original_cards.keys())
        cards = {card: 1 for card in self.original_cards.keys()}
        cur_card = 1
        while (cur_card <= len(cards.keys())):
            cards[cur_card] -= 1

            num_matches = self.original_cards[cur_card]
            if num_matches > 0:
                for i in range(cur_card+1, cur_card+num_matches+1):
                    cards[i] += 1
                    total += 1
            if cards[cur_card] == 0:
                cur_card += 1

        return total

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
    solution_class.post_processing()
    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

