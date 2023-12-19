import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.hole_corners: list[tuple] = [(0, 0)] # list of x, y
        self.hole_set: set[tuple] = set([(0, 0)])
        self.colors = [None] # list of hexadecimal color codes for each edge
        self.cur_pos = (0, 0)

    def add_tuples(self, *tuples):
        return tuple([sum(x) for x in zip(*tuples)])

    def mult_tuple(self, tup, scalar):
        return tuple([x * scalar for x in tup])

    def process_line(self, line):
        """How to process each line in the input"""
        tup_dict = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1)
        }
        if line != '\n':
            split = line[:-1].split(' ')
            let = split[0]
            num = int(split[1])
            color = split[2][1:-1]
            for i in range(1, num+1):
                self.cur_pos = self.add_tuples(self.cur_pos, tup_dict[let])
                color = split[2][1:-1]
                self.colors.append(color)
                self.hole_set.add(self.cur_pos)
            # self.cur_pos = self.add_tuples(self.cur_pos, self.mult_tuple(tup_dict[let], num))

            self.colors.append(color)
            self.hole_corners.append(self.cur_pos)

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        
        self.hole_corners = self.hole_corners[:-1]
        self.hole_list = sorted(self.hole_set)
        print(self.hole_list)
        
        # bucket sort
        dic = {}
        unique_x = set([e[0] for e in self.hole_list])
        for x in unique_x:
            dic[x] = []
        for e in self.hole_list:
            dic[e[0]].append(e[1])
        # for x, l in dic.items():
        #     new_l = []
        #     for i in range(0, len(l)): # 1...len(l)-2
        #         if i == 0 or i == len(l)-1 or l[i+1] - l[i] != 1 or l[i] - l[i-1] != 1:
        #             new_l.append(l[i])
        #     dic[x] = new_l
        print(dic)
        # crash
        total = 0
        for x, l in dic.items():
            start_idx = 0
            end_idx = 1
            start = 0
            end = 0
            subtotal = 0
            is_in = False
            is_border = False
            while start_idx < len(l) - 1 and end_idx < len(l):
                start = l[start_idx]
                end = l[end_idx]
                if end - start != 1:
                    is_in = not is_in
                    is_border = False
                else:
                    is_border = True
                print(x, start, end, is_in, is_border)

                if is_in:
                    if is_border:
                        subtotal += 1
                    else:
                        subtotal += end - start + 1

                if not is_border:           
                    start_idx = end_idx
                end_idx += 1

            if is_in:
                if is_border:
                    subtotal += 1
                else:
                    subtotal += end - start + 1

            print(subtotal)
            total += subtotal

        print(total)
        return total


        total = 0
        cur_idx = 0
        cur_x = self.hole_corners[0][0]
        is_in = True
        while cur_idx < len(self.hole_list) - 1:
            start = self.hole_list[cur_idx]
            j = cur_idx + 1
            end = self.hole_list[j]
            diff = end[1] - start[1]
            while j < len(self.hole_list) and self.hole_list[j][0] == start[0] and diff == 1:
                end = self.hole_list[j]
                j += 1
                if j < len(self.hole_list):
                    diff = end[1] - start[1]
            
            print(start, end, is_in)
            if start[0] != cur_x:
                cur_x = start

            if is_in:
                total += end[1] - start[1] + 1
                
            if all([(cur_x, i) in self.hole_set for i in range(start[1], end[1]+1)]):
                # border, do nothing
                pass
            else:
                is_in = not is_in

            cur_idx += j

        print(self.hole_corners)
        print(sorted(self.hole_set))
        print(self.colors)
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

        

