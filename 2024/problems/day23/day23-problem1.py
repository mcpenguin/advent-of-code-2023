import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.graph = {}
        self.nodes = set()

    def process_line(self, line: str):
        """How to process each line in the input"""

        start, end = line.strip().split('-')
        if start not in self.graph:
            self.graph[start] = set()
        if end not in self.graph:
            self.graph[end] = set()
        self.graph[start].add(end)
        self.graph[end].add(start)
        self.nodes.add(start)
        self.nodes.add(end)

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        res = 0
        node_list = list(self.nodes)
        for i in range(0, len(node_list)):
            for j in range(i+1, len(node_list)):
                for k in range(j+1, len(node_list)):
                    node1 = node_list[i]
                    node2 = node_list[j]
                    node3 = node_list[k]
                    if node2 in self.graph[node1] and node3 in self.graph[node2] and node1 in self.graph[node3] and \
                        any([node[0] == 't' for node in [node1, node2, node3]]):
                        res += 1
        return res


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

        

