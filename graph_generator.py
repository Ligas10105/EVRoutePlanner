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
    max_edges_per_vertex = int(input("Podaj maksymalną liczbę połączeń dla jednego wierzchołka: "))
    max_distance = int(input("Podaj maksymalną odległość między wierzchołkami: "))

    # Funkcja do generowania nazw wierzchołków z liter i powtórzeń liter
    def generate_node_names(n):
        names = []
        index = 0
        while len(names) < n:
            name = "".join(chr(65 + (index // 26 ** i) % 26) for i in range(index.bit_length() // 5 + 1))[::-1]
            names.append(name)
            index += 1
        return names

    # Tworzenie kodu Python dla grafu
    nodes = generate_node_names(num_vertices)  # Generowanie wierzchołków jako A, B, ..., AA, AB, ...
    distances = {}
    edges = []

    # Tworzenie połączeń na podstawie użytkownika
    for i in range(num_vertices):
        connections = random.randint(1, max_edges_per_vertex)  # Każdy wierzchołek ma od 1 do max_edges_per_vertex połączeń
        possible_nodes = [node for node in nodes if node != nodes[i]]
        connected_nodes = random.sample(possible_nodes, connections)
        for connected_node in connected_nodes:
            if (nodes[i], connected_node) not in [(x[0], x[1]) for x in edges] and (connected_node, nodes[i]) not in [(x[0], x[1]) for x in edges]:
                distance = random.randint(50, max_distance)
                edges.append((nodes[i], connected_node, distance))

    # Konwersja krawędzi na distances
    for start, end, distance in edges:
        distances[(start, end)] = distance

    # Losowy rozstaw stacji w grafie
    if num_stations > len(nodes):
        num_stations = len(nodes)

    station_nodes = random.sample(nodes, num_stations)
    stations = {}
    for node in station_nodes:
        price_per_kwh = round(random.uniform(0.4, 0.8), 2)
        queue_time = round(random.uniform(0.1, 0.5), 2)
        max_power = random.randint(30, 100)
        stations[node] = ChargingStation(node, 50, max_distance, price_per_kwh, queue_time, max_power)

    # Tworzenie grafu jako obiektu
    class Graph:
        def __init__(self):
            self.edges = []

        def add_edge(self, start, end, distance, difficulty):
            self.edges.append((start, end, distance, difficulty))

    graph = Graph()
    for (start, end), distance in distances.items():
        difficulty = round(random.uniform(1.0, 2.0), 2)
        graph.add_edge(start, end, distance, difficulty)
        graph.add_edge(end, start, distance, difficulty)

    return graph, stations, nodes, distances, max_distance

# Generowanie grafu i zapisywanie do pliku
if __name__ == "__main__":
    graph, stations, nodes, distances, max_distance = generate_graph()

    with open("EVRoutePlanner\generated_graph.py", "w") as file:
        file.write("from src.graph import Graph\n")
        file.write("from src.charging_station import ChargingStation\n\n")
        file.write("# Wygenerowany graf\n")
        file.write("graph = Graph()\n")
        for edge in graph.edges:
            file.write(f"graph.add_edge(\"{edge[0]}\", \"{edge[1]}\", {edge[2]}, difficulty={edge[3]})\n")
        file.write("\n# Węzły grafu\n")
        file.write(f"nodes = {nodes}\n\n")
        file.write("# Odległości między wierzchołkami\n")
        file.write("distances = {\n")
        for (start, end), distance in distances.items():
            file.write(f"    (\"{start}\", \"{end}\"): {distance},\n")
        file.write("}\n\n")
        file.write("# Wygenerowane stacje ładowania\n")
        file.write("stations = {\n")
        for node, station in stations.items():
            file.write(f"    \"{node}\": ChargingStation(\"{station.name}\", 50, {max_distance}, price_per_kwh={station.price_per_kwh}, queue_time={station.queue_time}, max_power={station.max_power}),\n")
        file.write("}\n")
