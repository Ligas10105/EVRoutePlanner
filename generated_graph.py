from src.graph import Graph
from src.charging_station import ChargingStation

# Wygenerowany graf
graph = Graph()
graph.add_edge("N19", "N4", 14, difficulty=1.54)
graph.add_edge("N19", "N6", 81, difficulty=1.34)
graph.add_edge("N19", "N1", 85, difficulty=1.04)
graph.add_edge("N19", "N8", 97, difficulty=1.43)
graph.add_edge("N19", "N17", 57, difficulty=1.43)
graph.add_edge("N4", "N19", 14, difficulty=1.54)
graph.add_edge("N4", "N16", 51, difficulty=1.01)
graph.add_edge("N4", "N1", 43, difficulty=1.75)
graph.add_edge("N4", "N2", 33, difficulty=1.5)
graph.add_edge("N11", "N13", 40, difficulty=1.83)
graph.add_edge("N11", "N8", 90, difficulty=1.43)
graph.add_edge("N11", "N17", 81, difficulty=1.69)
graph.add_edge("N11", "N18", 35, difficulty=1.65)
graph.add_edge("N13", "N11", 40, difficulty=1.83)
graph.add_edge("N13", "N6", 19, difficulty=1.29)
graph.add_edge("N13", "N8", 23, difficulty=1.34)
graph.add_edge("N6", "N13", 19, difficulty=1.29)
graph.add_edge("N6", "N9", 58, difficulty=1.81)
graph.add_edge("N6", "N19", 81, difficulty=1.34)
graph.add_edge("N6", "N3", 20, difficulty=1.48)
graph.add_edge("N6", "N2", 34, difficulty=1.24)
graph.add_edge("N6", "N5", 94, difficulty=1.11)
graph.add_edge("N18", "N2", 94, difficulty=2.0)
graph.add_edge("N18", "N0", 75, difficulty=1.86)
graph.add_edge("N18", "N11", 35, difficulty=1.65)
graph.add_edge("N2", "N18", 94, difficulty=2.0)
graph.add_edge("N2", "N9", 82, difficulty=1.33)
graph.add_edge("N2", "N17", 53, difficulty=1.04)
graph.add_edge("N2", "N1", 92, difficulty=1.97)
graph.add_edge("N2", "N4", 33, difficulty=1.5)
graph.add_edge("N2", "N16", 42, difficulty=1.45)
graph.add_edge("N2", "N12", 62, difficulty=1.23)
graph.add_edge("N2", "N6", 34, difficulty=1.24)
graph.add_edge("N16", "N4", 51, difficulty=1.01)
graph.add_edge("N16", "N2", 42, difficulty=1.45)
graph.add_edge("N9", "N2", 82, difficulty=1.33)
graph.add_edge("N9", "N6", 58, difficulty=1.81)
graph.add_edge("N9", "N0", 49, difficulty=1.49)
graph.add_edge("N9", "N10", 24, difficulty=1.22)
graph.add_edge("N9", "N17", 86, difficulty=1.95)
graph.add_edge("N17", "N2", 53, difficulty=1.04)
graph.add_edge("N17", "N11", 81, difficulty=1.69)
graph.add_edge("N17", "N5", 16, difficulty=1.42)
graph.add_edge("N17", "N9", 86, difficulty=1.95)
graph.add_edge("N17", "N1", 43, difficulty=1.41)
graph.add_edge("N17", "N19", 57, difficulty=1.43)
graph.add_edge("N1", "N4", 43, difficulty=1.75)
graph.add_edge("N1", "N19", 85, difficulty=1.04)
graph.add_edge("N1", "N12", 50, difficulty=1.28)
graph.add_edge("N1", "N2", 92, difficulty=1.97)
graph.add_edge("N1", "N17", 43, difficulty=1.41)
graph.add_edge("N8", "N13", 23, difficulty=1.34)
graph.add_edge("N8", "N11", 90, difficulty=1.43)
graph.add_edge("N8", "N0", 64, difficulty=1.15)
graph.add_edge("N8", "N19", 97, difficulty=1.43)
graph.add_edge("N0", "N18", 75, difficulty=1.86)
graph.add_edge("N0", "N9", 49, difficulty=1.49)
graph.add_edge("N0", "N8", 64, difficulty=1.15)
graph.add_edge("N5", "N14", 76, difficulty=1.55)
graph.add_edge("N5", "N17", 16, difficulty=1.42)
graph.add_edge("N5", "N6", 94, difficulty=1.11)
graph.add_edge("N14", "N5", 76, difficulty=1.55)
graph.add_edge("N14", "N7", 15, difficulty=1.95)
graph.add_edge("N10", "N9", 24, difficulty=1.22)
graph.add_edge("N3", "N6", 20, difficulty=1.48)
graph.add_edge("N12", "N1", 50, difficulty=1.28)
graph.add_edge("N12", "N2", 62, difficulty=1.23)
graph.add_edge("N7", "N14", 15, difficulty=1.95)

# Wêz³y grafu
nodes = ['N0', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19']

# Odleg³oœci miêdzy wierzcho³kami
distances = {('N19', 'N4'): 14, ('N4', 'N19'): 14, ('N11', 'N13'): 40, ('N13', 'N11'): 40, ('N13', 'N6'): 19, ('N6', 'N13'): 19, ('N18', 'N2'): 94, ('N2', 'N18'): 94, ('N4', 'N16'): 51, ('N16', 'N4'): 51, ('N2', 'N9'): 82, ('N9', 'N2'): 82, ('N2', 'N17'): 53, ('N17', 'N2'): 53, ('N1', 'N4'): 43, ('N4', 'N1'): 43, ('N8', 'N13'): 23, ('N13', 'N8'): 23, ('N8', 'N11'): 90, ('N11', 'N8'): 90, ('N18', 'N0'): 75, ('N0', 'N18'): 75, ('N5', 'N14'): 76, ('N14', 'N5'): 76, ('N6', 'N9'): 58, ('N9', 'N6'): 58, ('N17', 'N11'): 81, ('N11', 'N17'): 81, ('N6', 'N19'): 81, ('N19', 'N6'): 81, ('N0', 'N9'): 49, ('N9', 'N0'): 49, ('N9', 'N10'): 24, ('N10', 'N9'): 24, ('N6', 'N3'): 20, ('N3', 'N6'): 20, ('N19', 'N1'): 85, ('N1', 'N19'): 85, ('N12', 'N1'): 50, ('N1', 'N12'): 50, ('N2', 'N1'): 92, ('N1', 'N2'): 92, ('N4', 'N2'): 33, ('N2', 'N4'): 33, ('N2', 'N16'): 42, ('N16', 'N2'): 42, ('N5', 'N17'): 16, ('N17', 'N5'): 16, ('N2', 'N12'): 62, ('N12', 'N2'): 62, ('N17', 'N9'): 86, ('N9', 'N17'): 86, ('N1', 'N17'): 43, ('N17', 'N1'): 43, ('N6', 'N2'): 34, ('N2', 'N6'): 34, ('N6', 'N5'): 94, ('N5', 'N6'): 94, ('N8', 'N0'): 64, ('N0', 'N8'): 64, ('N8', 'N19'): 97, ('N19', 'N8'): 97, ('N18', 'N11'): 35, ('N11', 'N18'): 35, ('N7', 'N14'): 15, ('N14', 'N7'): 15, ('N17', 'N19'): 57, ('N19', 'N17'): 57}

# Wygenerowane stacje ³adowania
stations = {
    "N15": ChargingStation("N15", 64, 52, price_per_kwh=0.7, queue_time=0.36, max_power=67),
    "N12": ChargingStation("N12", 65, 55, price_per_kwh=0.6, queue_time=0.18, max_power=87),
    "N14": ChargingStation("N14", 75, 41, price_per_kwh=0.72, queue_time=0.46, max_power=100),
    "N4": ChargingStation("N4", 24, 19, price_per_kwh=0.49, queue_time=0.16, max_power=36),
}
