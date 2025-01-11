from src.graph import Graph
from src.charging_station import ChargingStation

# Wygenerowany graf
graph = Graph()
graph.add_edge("N1", "N4", 31, difficulty=1.69)
graph.add_edge("N1", "N18", 37, difficulty=1.98)
graph.add_edge("N1", "N10", 96, difficulty=1.11)
graph.add_edge("N4", "N1", 31, difficulty=1.69)
graph.add_edge("N4", "N11", 14, difficulty=1.31)
graph.add_edge("N4", "N9", 18, difficulty=1.8)
graph.add_edge("N14", "N2", 77, difficulty=1.2)
graph.add_edge("N14", "N3", 12, difficulty=1.92)
graph.add_edge("N14", "N5", 67, difficulty=1.29)
graph.add_edge("N14", "N16", 92, difficulty=1.46)
graph.add_edge("N14", "N15", 13, difficulty=1.47)
graph.add_edge("N2", "N14", 77, difficulty=1.2)
graph.add_edge("N2", "N12", 82, difficulty=1.53)
graph.add_edge("N18", "N1", 37, difficulty=1.98)
graph.add_edge("N18", "N12", 73, difficulty=1.23)
graph.add_edge("N18", "N19", 87, difficulty=1.65)
graph.add_edge("N18", "N16", 15, difficulty=1.34)
graph.add_edge("N18", "N13", 59, difficulty=1.54)
graph.add_edge("N18", "N6", 26, difficulty=1.02)
graph.add_edge("N12", "N18", 73, difficulty=1.23)
graph.add_edge("N12", "N2", 82, difficulty=1.53)
graph.add_edge("N11", "N4", 14, difficulty=1.31)
graph.add_edge("N11", "N9", 82, difficulty=1.22)
graph.add_edge("N7", "N3", 87, difficulty=1.96)
graph.add_edge("N7", "N5", 27, difficulty=1.59)
graph.add_edge("N3", "N7", 87, difficulty=1.96)
graph.add_edge("N3", "N14", 12, difficulty=1.92)
graph.add_edge("N3", "N5", 93, difficulty=1.87)
graph.add_edge("N3", "N8", 100, difficulty=1.53)
graph.add_edge("N3", "N16", 72, difficulty=1.2)
graph.add_edge("N3", "N13", 85, difficulty=1.57)
graph.add_edge("N19", "N18", 87, difficulty=1.65)
graph.add_edge("N19", "N0", 54, difficulty=1.9)
graph.add_edge("N19", "N17", 74, difficulty=1.73)
graph.add_edge("N19", "N5", 63, difficulty=1.18)
graph.add_edge("N19", "N8", 37, difficulty=1.21)
graph.add_edge("N9", "N11", 82, difficulty=1.22)
graph.add_edge("N9", "N4", 18, difficulty=1.8)
graph.add_edge("N5", "N3", 93, difficulty=1.87)
graph.add_edge("N5", "N7", 27, difficulty=1.59)
graph.add_edge("N5", "N14", 67, difficulty=1.29)
graph.add_edge("N5", "N13", 22, difficulty=1.1)
graph.add_edge("N5", "N6", 17, difficulty=1.53)
graph.add_edge("N5", "N19", 63, difficulty=1.18)
graph.add_edge("N0", "N19", 54, difficulty=1.9)
graph.add_edge("N0", "N6", 10, difficulty=1.58)
graph.add_edge("N8", "N3", 100, difficulty=1.53)
graph.add_edge("N8", "N15", 84, difficulty=1.26)
graph.add_edge("N8", "N19", 37, difficulty=1.21)
graph.add_edge("N17", "N19", 74, difficulty=1.73)
graph.add_edge("N17", "N6", 80, difficulty=1.8)
graph.add_edge("N10", "N15", 22, difficulty=1.25)
graph.add_edge("N10", "N1", 96, difficulty=1.11)
graph.add_edge("N10", "N13", 98, difficulty=1.93)
graph.add_edge("N15", "N10", 22, difficulty=1.25)
graph.add_edge("N15", "N6", 78, difficulty=1.61)
graph.add_edge("N15", "N8", 84, difficulty=1.26)
graph.add_edge("N15", "N14", 13, difficulty=1.47)
graph.add_edge("N16", "N3", 72, difficulty=1.2)
graph.add_edge("N16", "N18", 15, difficulty=1.34)
graph.add_edge("N16", "N14", 92, difficulty=1.46)
graph.add_edge("N6", "N0", 10, difficulty=1.58)
graph.add_edge("N6", "N15", 78, difficulty=1.61)
graph.add_edge("N6", "N5", 17, difficulty=1.53)
graph.add_edge("N6", "N18", 26, difficulty=1.02)
graph.add_edge("N6", "N17", 80, difficulty=1.8)
graph.add_edge("N13", "N5", 22, difficulty=1.1)
graph.add_edge("N13", "N3", 85, difficulty=1.57)
graph.add_edge("N13", "N18", 59, difficulty=1.54)
graph.add_edge("N13", "N10", 98, difficulty=1.93)

# Wêz³y grafu
nodes = ['N0', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19']

# Odleg³oœci miêdzy wierzcho³kami
distances = {('N1', 'N4'): 31, ('N4', 'N1'): 31, ('N14', 'N2'): 77, ('N2', 'N14'): 77, ('N18', 'N1'): 37, ('N1', 'N18'): 37, ('N18', 'N12'): 73, ('N12', 'N18'): 73, ('N4', 'N11'): 14, ('N11', 'N4'): 14, ('N7', 'N3'): 87, ('N3', 'N7'): 87, ('N18', 'N19'): 87, ('N19', 'N18'): 87, ('N3', 'N14'): 12, ('N14', 'N3'): 12, ('N9', 'N11'): 82, ('N11', 'N9'): 82, ('N5', 'N3'): 93, ('N3', 'N5'): 93, ('N19', 'N0'): 54, ('N0', 'N19'): 54, ('N7', 'N5'): 27, ('N5', 'N7'): 27, ('N3', 'N8'): 100, ('N8', 'N3'): 100, ('N5', 'N14'): 67, ('N14', 'N5'): 67, ('N12', 'N2'): 82, ('N2', 'N12'): 82, ('N19', 'N17'): 74, ('N17', 'N19'): 74, ('N10', 'N15'): 22, ('N15', 'N10'): 22, ('N3', 'N16'): 72, ('N16', 'N3'): 72, ('N10', 'N1'): 96, ('N1', 'N10'): 96, ('N9', 'N4'): 18, ('N4', 'N9'): 18, ('N0', 'N6'): 10, ('N6', 'N0'): 10, ('N6', 'N15'): 78, ('N15', 'N6'): 78, ('N13', 'N5'): 22, ('N5', 'N13'): 22, ('N18', 'N16'): 15, ('N16', 'N18'): 15, ('N5', 'N6'): 17, ('N6', 'N5'): 17, ('N3', 'N13'): 85, ('N13', 'N3'): 85, ('N16', 'N14'): 92, ('N14', 'N16'): 92, ('N13', 'N18'): 59, ('N18', 'N13'): 59, ('N6', 'N18'): 26, ('N18', 'N6'): 26, ('N10', 'N13'): 98, ('N13', 'N10'): 98, ('N5', 'N19'): 63, ('N19', 'N5'): 63, ('N8', 'N15'): 84, ('N15', 'N8'): 84, ('N17', 'N6'): 80, ('N6', 'N17'): 80, ('N14', 'N15'): 13, ('N15', 'N14'): 13, ('N19', 'N8'): 37, ('N8', 'N19'): 37}

# Wygenerowane stacje ³adowania
stations = {
    "N11": ChargingStation("N11", 92, 79, price_per_kwh=0.62, queue_time=0.4, max_power=84),
    "N6": ChargingStation("N6", 20, 1, price_per_kwh=0.41, queue_time=0.44, max_power=67),
    "N5": ChargingStation("N5", 38, 79, price_per_kwh=0.66, queue_time=0.26, max_power=68),
    "N14": ChargingStation("N14", 17, 33, price_per_kwh=0.66, queue_time=0.18, max_power=68),
}
