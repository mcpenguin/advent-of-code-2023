import os
import sys

class Solution:
    """Class for solution"""

    def __init__(self):
        self.graph = {}
        self.nodes = set()
        self.edges = []

    def process_line(self, line: str):
        """How to process each line in the input"""

        start, end = line.strip().split('-')
        if start not in self.graph:
            self.graph[start] = set()
        if end not in self.graph:
            self.graph[end] = set()

        # self.graph[start].add(start)
        self.graph[start].add(end)
        self.graph[end].add(start)
        # self.graph[end].add(end)
        self.nodes.add(start)
        self.nodes.add(end)

        self.edges.append(set([start, end]))

    def set_equal(self, s1, s2):
        return len(s1.difference(s2).union(s2.difference(s1))) == 0
    
    def fully_conn(self, node):
        edges = self.graph[node]
        print(node, edges)
        for end in edges:
            edges = edges.intersection(self.graph[end])
            print(end, self.graph[end], edges)
        return len(edges)

    def get_solution(self):
        """How to retrieve the solution once all lines have been processed"""
        size = 2
        while len(self.edges) > (size * (size + 1)) // 2:
            print(size, len(self.edges))
            cur = []
            for nodes in self.edges:
                for n in self.nodes:
                    if n not in nodes and all([n in self.graph[node] for node in nodes]):
                        cur.append(nodes.union(set([n])))
                        break
            self.edges = cur
            size += 1
        pw = ','.join(sorted(self.edges[0]))

        return pw


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

        

