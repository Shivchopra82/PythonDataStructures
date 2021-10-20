#1.Graph is complex data structure which can connect nodes with one or more than path called edges. 
# 2.Graph can be used to plan the routes between different cities and it can be helpful in calculating the shortest and most efficient path between different cities. 
# 3.If a graph has some value on their edges then it is called weighted graph.
# 4.Weighted graph is best suited for the mapping of path between cities as edges can represent the cost incurred for travelling on that path. 

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path



routes = [
    ("Mumbai","Pune"),
    ("Mumbai", "Surat"),
    ("Surat", "Bangaluru"),
    ("Pune","Hyderabad"),
    ("Pune","Mysuru"),
    ("Hyderabad","Bangaluru"),
    ("Hyderabad", "Chennai"),
    ("Mysuru", "Bangaluru"),
    ("Chennai", "Bangaluru")
]

route_graph = Graph(routes)

start = "Mumbai"
end = "Chennai"

print(f"All paths between: {start} and {end}: {route_graph.get_paths(start,end)}")
print(f"Shortest path between {start} and {end}: {route_graph.get_shortest_path(start,end)}")

start = "Pune"
end = "Chennai"

print(f"All paths between: {start} and {end}: {route_graph.get_paths(start,end)}")
print(f"Shortest path between {start} and {end}: {route_graph.get_shortest_path(start,end)}")