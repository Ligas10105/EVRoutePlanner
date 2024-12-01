from src.util_functions import is_reachable

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
        # Jeśli visited nie zostało przekazane, przypisz pusty zbiór
        visited = visited if visited is not None else set()
        
        # Sprawdź dostępnych sąsiadów dla danego węzła
        neighbors = self.edges.get(node, {})
        valid_neighbors = {}

        for neighbor, edge_data in neighbors.items():
            # Pomijaj węzły, które już odwiedziliśmy
            if neighbor in visited:
                continue

            # Jeśli dostępne dane o pojeździe i poziomie naładowania, sprawdź, czy pojazd może przejechać do sąsiada
            if current_charge is not None and vehicle is not None:
                distance = edge_data["distance"]
                if not is_reachable(current_charge, distance, vehicle.energy_per_km):
                    continue

            # Dodaj sąsiada do wynikowego słownika
            valid_neighbors[neighbor] = edge_data

        return valid_neighbors
