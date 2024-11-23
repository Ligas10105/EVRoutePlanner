class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, point1, point2, distance, difficulty=1.0):
        if point1 not in self.edges:
            self.edges[point1] = {}
        self.edges[point1][point2] = {"distance": distance, "difficulty": difficulty}

    def get_neighbors(self, point):
        return self.edges.get(point, {})