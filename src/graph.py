class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, point1, point2, distance, difficulty=1.0):
        if point1 not in self.edges:
            self.edges[point1] = {}
        self.edges[point1][point2] = {"distance": distance, "difficulty": difficulty}

    def get_neighbors(self, node, visited=None, current_charge=None, vehicle=None):
        """
        Zwraca sąsiadów dostępnych z danego węzła, uwzględniając odwiedzone węzły i ograniczenia pojazdu.
        :param node: Bieżący węzeł
        :param visited: Zbiór odwiedzonych węzłów (opcjonalnie)
        :param current_charge: Aktualny poziom baterii pojazdu (opcjonalnie)
        :param vehicle: Obiekt pojazdu elektrycznego (opcjonalnie)
        :return: Słownik sąsiadów (dostępnych węzłów)
        """
        neighbors = self.edges.get(node, {})
        valid_neighbors = {}
        for neighbor, edge_data in neighbors.items():
            # Pomijaj węzły, które już odwiedziliśmy
            if visited and neighbor in visited:
                continue
            valid_neighbors[neighbor] = edge_data
        return valid_neighbors
