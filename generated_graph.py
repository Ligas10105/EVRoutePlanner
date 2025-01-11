from src.graph import Graph
from src.charging_station import ChargingStation

# Wygenerowany graf
graph = Graph()
graph.add_edge("N6", "N12", 78, difficulty=1.65)
graph.add_edge("N6", "N0", 89, difficulty=1.21)
graph.add_edge("N6", "N5", 38, difficulty=1.05)
graph.add_edge("N6", "N14", 23, difficulty=1.55)
graph.add_edge("N6", "N2", 42, difficulty=1.48)
graph.add_edge("N12", "N6", 78, difficulty=1.65)
graph.add_edge("N12", "N10", 85, difficulty=1.25)
graph.add_edge("N17", "N10", 77, difficulty=1.47)
graph.add_edge("N17", "N3", 32, difficulty=1.9)
graph.add_edge("N17", "N11", 22, difficulty=1.78)
graph.add_edge("N17", "N19", 30, difficulty=1.96)
graph.add_edge("N10", "N17", 77, difficulty=1.47)
graph.add_edge("N10", "N11", 29, difficulty=1.23)
graph.add_edge("N10", "N12", 85, difficulty=1.25)
graph.add_edge("N0", "N5", 56, difficulty=1.22)
graph.add_edge("N0", "N6", 89, difficulty=1.21)
graph.add_edge("N0", "N19", 17, difficulty=1.47)
graph.add_edge("N0", "N13", 47, difficulty=1.63)
graph.add_edge("N0", "N8", 82, difficulty=1.58)
graph.add_edge("N5", "N0", 56, difficulty=1.22)
graph.add_edge("N5", "N7", 32, difficulty=1.62)
graph.add_edge("N5", "N8", 100, difficulty=1.43)
graph.add_edge("N5", "N6", 38, difficulty=1.05)
graph.add_edge("N2", "N13", 83, difficulty=1.76)
graph.add_edge("N2", "N16", 23, difficulty=1.06)
graph.add_edge("N2", "N4", 82, difficulty=1.68)
graph.add_edge("N2", "N6", 42, difficulty=1.48)
graph.add_edge("N2", "N1", 24, difficulty=1.91)
graph.add_edge("N13", "N2", 83, difficulty=1.76)
graph.add_edge("N13", "N0", 47, difficulty=1.63)
graph.add_edge("N13", "N9", 33, difficulty=1.6)
graph.add_edge("N13", "N18", 42, difficulty=1.38)
graph.add_edge("N13", "N15", 72, difficulty=1.79)
graph.add_edge("N7", "N5", 32, difficulty=1.62)
graph.add_edge("N11", "N10", 29, difficulty=1.23)
graph.add_edge("N11", "N17", 22, difficulty=1.78)
graph.add_edge("N3", "N17", 32, difficulty=1.9)
graph.add_edge("N3", "N4", 17, difficulty=1.9)
graph.add_edge("N3", "N14", 97, difficulty=1.08)
graph.add_edge("N14", "N18", 71, difficulty=1.79)
graph.add_edge("N14", "N9", 26, difficulty=1.95)
graph.add_edge("N14", "N6", 23, difficulty=1.55)
graph.add_edge("N14", "N4", 45, difficulty=1.84)
graph.add_edge("N14", "N3", 97, difficulty=1.08)
graph.add_edge("N18", "N14", 71, difficulty=1.79)
graph.add_edge("N18", "N19", 33, difficulty=1.84)
graph.add_edge("N18", "N13", 42, difficulty=1.38)
graph.add_edge("N8", "N5", 100, difficulty=1.43)
graph.add_edge("N8", "N16", 94, difficulty=1.09)
graph.add_edge("N8", "N0", 82, difficulty=1.58)
graph.add_edge("N9", "N14", 26, difficulty=1.95)
graph.add_edge("N9", "N15", 97, difficulty=1.62)
graph.add_edge("N9", "N13", 33, difficulty=1.6)
graph.add_edge("N16", "N8", 94, difficulty=1.09)
graph.add_edge("N16", "N2", 23, difficulty=1.06)
graph.add_edge("N19", "N0", 17, difficulty=1.47)
graph.add_edge("N19", "N18", 33, difficulty=1.84)
graph.add_edge("N19", "N17", 30, difficulty=1.96)
graph.add_edge("N19", "N4", 21, difficulty=1.9)
graph.add_edge("N4", "N2", 82, difficulty=1.68)
graph.add_edge("N4", "N1", 35, difficulty=1.97)
graph.add_edge("N4", "N19", 21, difficulty=1.9)
graph.add_edge("N4", "N14", 45, difficulty=1.84)
graph.add_edge("N4", "N3", 17, difficulty=1.9)
graph.add_edge("N1", "N4", 35, difficulty=1.97)
graph.add_edge("N1", "N2", 24, difficulty=1.91)
graph.add_edge("N15", "N9", 97, difficulty=1.62)
graph.add_edge("N15", "N13", 72, difficulty=1.79)

# Wêz³y grafu
nodes = ['N0', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19']

# Odleg³oœci miêdzy wierzcho³kami
distances = {('N6', 'N12'): 78, ('N12', 'N6'): 78, ('N17', 'N10'): 77, ('N10', 'N17'): 77, ('N0', 'N5'): 56, ('N5', 'N0'): 56, ('N2', 'N13'): 83, ('N13', 'N2'): 83, ('N5', 'N7'): 32, ('N7', 'N5'): 32, ('N6', 'N0'): 89, ('N0', 'N6'): 89, ('N11', 'N10'): 29, ('N10', 'N11'): 29, ('N17', 'N3'): 32, ('N3', 'N17'): 32, ('N14', 'N18'): 71, ('N18', 'N14'): 71, ('N5', 'N8'): 100, ('N8', 'N5'): 100, ('N6', 'N5'): 38, ('N5', 'N6'): 38, ('N9', 'N14'): 26, ('N14', 'N9'): 26, ('N8', 'N16'): 94, ('N16', 'N8'): 94, ('N19', 'N0'): 17, ('N0', 'N19'): 17, ('N16', 'N2'): 23, ('N2', 'N16'): 23, ('N4', 'N2'): 82, ('N2', 'N4'): 82, ('N1', 'N4'): 35, ('N4', 'N1'): 35, ('N15', 'N9'): 97, ('N9', 'N15'): 97, ('N17', 'N11'): 22, ('N11', 'N17'): 22, ('N0', 'N13'): 47, ('N13', 'N0'): 47, ('N14', 'N6'): 23, ('N6', 'N14'): 23, ('N10', 'N12'): 85, ('N12', 'N10'): 85, ('N18', 'N19'): 33, ('N19', 'N18'): 33, ('N0', 'N8'): 82, ('N8', 'N0'): 82, ('N13', 'N9'): 33, ('N9', 'N13'): 33, ('N6', 'N2'): 42, ('N2', 'N6'): 42, ('N19', 'N17'): 30, ('N17', 'N19'): 30, ('N4', 'N19'): 21, ('N19', 'N4'): 21, ('N18', 'N13'): 42, ('N13', 'N18'): 42, ('N4', 'N14'): 45, ('N14', 'N4'): 45, ('N15', 'N13'): 72, ('N13', 'N15'): 72, ('N3', 'N4'): 17, ('N4', 'N3'): 17, ('N1', 'N2'): 24, ('N2', 'N1'): 24, ('N14', 'N3'): 97, ('N3', 'N14'): 97}

# Wygenerowane stacje ³adowania
stations = {
    "N9": ChargingStation("N9", 12, 43, price_per_kwh=0.78, queue_time=0.42, max_power=48),
    "N2": ChargingStation("N2", 74, 15, price_per_kwh=0.66, queue_time=0.29, max_power=44),
    "N5": ChargingStation("N5", 63, 28, price_per_kwh=0.71, queue_time=0.11, max_power=67),
    "N3": ChargingStation("N3", 75, 37, price_per_kwh=0.46, queue_time=0.19, max_power=30),
}
