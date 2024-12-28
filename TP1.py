# Implement Path-existance and test check for the graph pref prog language where they following behavior:
# 1. As user input 2 nodes
# 2. Return True if path exist and False if not

class Graph:
    def __init__(self, vertices):
        self.graph = {}
        for v in range(1,vertices+1):
            self.graph[v]=[]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def path_exists(self, start, target):
        visited = [False] * (len(self.graph) + 1)
        visited[start] = True
        newly_visited = [start]
        while newly_visited:
            next_newly_visited = []
            for u in newly_visited:
                for v in self.graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        next_newly_visited.append(v)
            newly_visited = next_newly_visited
        return visited[target]

if __name__ == "__main__":
    graph = Graph(7)
    edges = [(1, 2), (2, 5), (3, 6), (6, 4), (6, 7), (4, 7)]
    for u, v in edges:
        graph.add_edge(u, v)
    input = input("Enter 2 random nodes: ").split()
    start = int(input[0])
    target = int(input[1])
    if graph.path_exists(start, target):
        print("True")
    else:
        print("False")