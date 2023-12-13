import os
import sys
from math import prod

class Solution:
    """Class for solution"""

    def __init__(self):
        self.hands_bids = []
        self.type_order = ['five_of_kind', 'four_of_kind', 'full_house', 'three_of_kind', 'two_pair', 'one_pair', 'high_card']
        self.card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    def get_hand_type(self, hand):
        uniq = list(set([c for c in hand]))
        # print(hand, uniq)
        if len(uniq) == 1:
            return 'five_of_kind'
        elif len(uniq) == 2:
            c0, c1 = uniq
            if c0 == 'J' or c1 == 'J':
                return 'five_of_kind'
            elif hand.count(c0) == 4 or hand.count(c1) == 4:
                return 'four_of_kind'
            else:
                return 'full_house'
        elif len(uniq) == 3:
            c0, c1, c2 = uniq
            if hand.count(c0) == 3 or hand.count(c1) == 3 or hand.count(c2) == 3:
                if [c0, c1, c2].count('J') == 1:
                    return 'four_of_kind'
                else:
                    return 'three_of_kind'
            else:
                if hand.count('J') == 2:
                    return 'four_of_kind'
                elif hand.count('J') == 1:
                    f = [c for c in hand if c != 'J']
                    f0, f1 = list(set(f))
                    if hand.count(f0) == hand.count(f1):
                        return 'full_house'
                    else:
                        return 'three_of_kind'
                else:
                    return 'two_pair'
        elif len(uniq) == 4:
            if hand.count('J') >= 1:
                return 'three_of_kind'
            else:
                return 'one_pair'
        else:
            if hand.count('J') >= 1:
                return 'one_pair'
            else:
                return 'high_card'

    def get_key_for_hand(self, hand):
        k = 0
        hand_type = self.get_hand_type(hand)
        k += self.type_order.index(hand_type)
        # print(hand,hand_type,  k)
        for c in hand:
            k = k * len(self.card_order) + self.card_order.index(c)
        return k
    
    # 1 if hand1 > hand2, 0 if hand1 < hand2
    def is_hand_bigger_than_hand(self, hand1, hand2):
        hand1type = self.get_hand_type(hand1)
        hand2type = self.get_hand_type(hand2)
        i1 = self.type_order.index(hand1type)
        i2 = self.type_order.index(hand2type)
        if i1 < i2:
            return 0
        elif i1 > i2:
            return 1
        else:
            for c1, c2 in zip(hand1, hand2):
                c1i = self.card_order.index(c1)
                c2i = self.card_order.index(c2)
                if c1i < c2i:
                    return 0
                elif c1i > c2i:
                    return 1
        return -1 # invalid


    def process_line(self, line: str):
        """How to process each line in the input"""

        if line != '\n':
            split = line.split(' ')
            self.hands_bids.append((split[0], int(split[1])))

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        self.hands_bids.sort(key=lambda x: self.get_key_for_hand(x[0]), reverse=True)
        # print(self.hands_bids)
        total = 0
        for i, hb in enumerate(self.hands_bids):
            total += (i+1) * hb[1]        
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

    solution = solution_class.get_solution()
    print()

    print("--- SOLUTION ---")
    print(solution)

        

