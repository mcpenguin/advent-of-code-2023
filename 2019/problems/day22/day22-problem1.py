import os
import sys
import copy

class Solution:
    """Class for solution"""

    def __init__(self):
        self.num = 10007
        self.cards = list(range(self.num))
        self.shuffles = []

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

    def apply_shuffle(self, shuffle, cards):
        if shuffle == 'deal_into_new_stack':
            return cards[::-1]
        elif shuffle[0] == 'cut':
            num = shuffle[1]
            # print(num)
            return cards[num:] + cards[:num]
        elif shuffle[0] == 'deal_with_increment':
            result = [-1]*len(cards)
            cur = 0
            for i in range(len(cards)):
                result[cur] = cards[i]
                cur = (cur + shuffle[1]) % len(cards)
            return result
        else:
            raise Exception('invalid shuffle encountered')

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        cards = copy.deepcopy(self.cards)
        for shuffle in self.shuffles:
            cards = self.apply_shuffle(shuffle, cards)
            # print(shuffle, cards)
        # print(cards)
        return cards[2019]
        # return cards.index(2019)

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

        

