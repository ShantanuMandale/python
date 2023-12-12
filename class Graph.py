class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def dfs(self, start, goal, path=[]):
        path = path + [start]

        if start == goal:
            return path

        if start not in self.graph:
            return None

        for neighbor in self.graph[start]:
            if neighbor not in path:
                new_path = self.dfs(neighbor, goal, path)
                if new_path:
                    return new_path

        return None

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

initial_node = 2
goal_node = 7

path = graph.dfs(initial_node, goal_node)

if path:
    print(f"Path from {initial_node} to {goal_node}:", path)
else:
    print(f"No path found from {initial_node} to {goal_node}")


