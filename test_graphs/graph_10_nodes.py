from src.graph import Graph
from src.charging_station import ChargingStation

# Wygenerowany graf
graph = Graph()
graph.add_edge("N6", "N7", 91, difficulty=1.5)
graph.add_edge("N6", "N3", 80, difficulty=1.25)
graph.add_edge("N6", "N5", 43, difficulty=1.52)
graph.add_edge("N7", "N6", 91, difficulty=1.5)
graph.add_edge("N2", "N1", 20, difficulty=1.13)
graph.add_edge("N2", "N4", 24, difficulty=1.76)
graph.add_edge("N1", "N2", 20, difficulty=1.13)
graph.add_edge("N1", "N4", 67, difficulty=1.7)
graph.add_edge("N4", "N3", 85, difficulty=1.21)
graph.add_edge("N4", "N9", 42, difficulty=1.25)
graph.add_edge("N4", "N8", 70, difficulty=1.66)
graph.add_edge("N4", "N2", 24, difficulty=1.76)
graph.add_edge("N4", "N1", 67, difficulty=1.7)
graph.add_edge("N3", "N4", 85, difficulty=1.21)
graph.add_edge("N3", "N6", 80, difficulty=1.25)
graph.add_edge("N3", "N0", 53, difficulty=1.92)
graph.add_edge("N9", "N4", 42, difficulty=1.25)
graph.add_edge("N9", "N5", 24, difficulty=1.88)
graph.add_edge("N9", "N8", 84, difficulty=1.79)
graph.add_edge("N5", "N6", 43, difficulty=1.52)
graph.add_edge("N5", "N9", 24, difficulty=1.88)
graph.add_edge("N8", "N9", 84, difficulty=1.79)
graph.add_edge("N8", "N4", 70, difficulty=1.66)
graph.add_edge("N0", "N3", 53, difficulty=1.92)

# Wêz³y grafu
nodes = ['N0', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9']

# Odleg³oœci miêdzy wierzcho³kami
distances = {('N6', 'N7'): 91, ('N7', 'N6'): 91, ('N2', 'N1'): 20, ('N1', 'N2'): 20, ('N4', 'N3'): 85, ('N3', 'N4'): 85, ('N9', 'N4'): 42, ('N4', 'N9'): 42, ('N3', 'N6'): 80, ('N6', 'N3'): 80, ('N6', 'N5'): 43, ('N5', 'N6'): 43, ('N5', 'N9'): 24, ('N9', 'N5'): 24, ('N9', 'N8'): 84, ('N8', 'N9'): 84, ('N0', 'N3'): 53, ('N3', 'N0'): 53, ('N8', 'N4'): 70, ('N4', 'N8'): 70, ('N4', 'N2'): 24, ('N2', 'N4'): 24, ('N1', 'N4'): 67, ('N4', 'N1'): 67}

# Wygenerowane stacje ³adowania
stations = {
    "N2": ChargingStation("N2", 70, 33, price_per_kwh=0.49, queue_time=0.15, max_power=31),
    "N7": ChargingStation("N7", 6, 19, price_per_kwh=0.67, queue_time=0.43, max_power=42),
    "N0": ChargingStation("N0", 67, 38, price_per_kwh=0.59, queue_time=0.27, max_power=67),
}
