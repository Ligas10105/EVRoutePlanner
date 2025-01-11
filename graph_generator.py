import random

class ChargingStation:
    def __init__(self, name, min_distance, max_distance, price_per_kwh, queue_time, max_power):
        self.name = name
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.price_per_kwh = price_per_kwh
        self.queue_time = queue_time
        self.max_power = max_power

    def __repr__(self):
        return (f"ChargingStation(name={self.name}, price_per_kwh={self.price_per_kwh}, "
                f"queue_time={self.queue_time}, max_power={self.max_power})")

def generate_graph():
    # Pobranie danych od użytkownika
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    num_stations = int(input("Podaj liczbę stacji w grafie: "))

    # Tworzenie kodu Python dla grafu
    nodes = [chr(65 + i) for i in range(num_vertices)]  # Tworzenie wierzchołków jako A, B, C, ...
    distances = {}

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            distance = random.randint(50, 500)  # Odległości w zakresie [50, 500]
            distances[(nodes[i], nodes[j])] = distance

    # Losowy rozstaw stacji w grafie
    station_nodes = random.sample(nodes, num_stations)
    stations = {}
    for node in station_nodes:
        price_per_kwh = round(random.uniform(0.4, 0.8), 2)
        queue_time = round(random.uniform(0.1, 0.5), 2)
        max_power = random.randint(30, 100)
        stations[node] = ChargingStation(node, 50, 500, price_per_kwh, queue_time, max_power)

    # Wyświetlenie wynikowego kodu
    print("# Definicja grafu")
    print("graph = Graph()")
    print(f"nodes = {nodes}")
    print("distances = {")
    for (start, end), distance in distances.items():
        print(f"    (\"{start}\", \"{end}\"): {distance},")
    print("}")

    print("\n# Dodawanie krawędzi do grafu")
    print("for (start, end), distance in distances.items():")
    print("    graph.add_edge(start, end, distance, difficulty=1.0)")
    print("    graph.add_edge(end, start, distance, difficulty=1.0)")

    print("\n# Stacje ładowania")
    print("stations = {")
    for node, station in stations.items():
        print(f"    \"{node}\": ChargingStation(\"{station.name}\", 50, 500, price_per_kwh={station.price_per_kwh}, queue_time={station.queue_time}, max_power={station.max_power}),")
    print("}")

    return nodes, distances, stations

# Uruchomienie funkcji
generated_graph_code = generate_graph()