from src.graph import Graph
from src.charging_station import ChargingStation

# Wygenerowany graf
graph = Graph()
graph.add_edge("N4", "N3", 47, difficulty=1.19)
graph.add_edge("N4", "N5", 64, difficulty=1.12)
graph.add_edge("N4", "N9", 48, difficulty=1.53)
graph.add_edge("N4", "N7", 69, difficulty=1.15)
graph.add_edge("N4", "N18", 30, difficulty=1.56)
graph.add_edge("N4", "N15", 87, difficulty=1.98)
graph.add_edge("N3", "N4", 47, difficulty=1.19)
graph.add_edge("N3", "N18", 43, difficulty=1.96)
graph.add_edge("N19", "N10", 77, difficulty=1.53)
graph.add_edge("N19", "N5", 40, difficulty=1.8)
graph.add_edge("N19", "N12", 11, difficulty=1.06)
graph.add_edge("N10", "N19", 77, difficulty=1.53)
graph.add_edge("N10", "N11", 39, difficulty=1.32)
graph.add_edge("N10", "N17", 91, difficulty=1.39)
graph.add_edge("N10", "N18", 73, difficulty=1.12)
graph.add_edge("N10", "N7", 57, difficulty=1.02)
graph.add_edge("N7", "N6", 62, difficulty=1.14)
graph.add_edge("N7", "N15", 34, difficulty=1.29)
graph.add_edge("N7", "N1", 66, difficulty=1.91)
graph.add_edge("N7", "N4", 69, difficulty=1.15)
graph.add_edge("N7", "N10", 57, difficulty=1.02)
graph.add_edge("N6", "N7", 62, difficulty=1.14)
graph.add_edge("N6", "N18", 84, difficulty=1.42)
graph.add_edge("N12", "N5", 76, difficulty=1.1)
graph.add_edge("N12", "N15", 71, difficulty=1.77)
graph.add_edge("N12", "N14", 32, difficulty=1.82)
graph.add_edge("N12", "N0", 55, difficulty=1.99)
graph.add_edge("N12", "N19", 11, difficulty=1.06)
graph.add_edge("N12", "N11", 16, difficulty=1.28)
graph.add_edge("N5", "N12", 76, difficulty=1.1)
graph.add_edge("N5", "N19", 40, difficulty=1.8)
graph.add_edge("N5", "N4", 64, difficulty=1.12)
graph.add_edge("N5", "N1", 48, difficulty=1.9)
graph.add_edge("N5", "N17", 52, difficulty=1.9)
graph.add_edge("N8", "N16", 72, difficulty=1.36)
graph.add_edge("N16", "N8", 72, difficulty=1.36)
graph.add_edge("N16", "N15", 88, difficulty=1.95)
graph.add_edge("N13", "N11", 45, difficulty=1.23)
graph.add_edge("N11", "N13", 45, difficulty=1.23)
graph.add_edge("N11", "N17", 32, difficulty=1.42)
graph.add_edge("N11", "N10", 39, difficulty=1.32)
graph.add_edge("N11", "N1", 13, difficulty=1.57)
graph.add_edge("N11", "N14", 28, difficulty=1.79)
graph.add_edge("N11", "N12", 16, difficulty=1.28)
graph.add_edge("N9", "N18", 23, difficulty=1.66)
graph.add_edge("N9", "N4", 48, difficulty=1.53)
graph.add_edge("N9", "N14", 69, difficulty=1.63)
graph.add_edge("N18", "N9", 23, difficulty=1.66)
graph.add_edge("N18", "N2", 64, difficulty=1.69)
graph.add_edge("N18", "N4", 30, difficulty=1.56)
graph.add_edge("N18", "N3", 43, difficulty=1.96)
graph.add_edge("N18", "N6", 84, difficulty=1.42)
graph.add_edge("N18", "N1", 60, difficulty=1.64)
graph.add_edge("N18", "N10", 73, difficulty=1.12)
graph.add_edge("N15", "N7", 34, difficulty=1.29)
graph.add_edge("N15", "N12", 71, difficulty=1.77)
graph.add_edge("N15", "N4", 87, difficulty=1.98)
graph.add_edge("N15", "N16", 88, difficulty=1.95)
graph.add_edge("N2", "N1", 47, difficulty=1.98)
graph.add_edge("N2", "N18", 64, difficulty=1.69)
graph.add_edge("N1", "N2", 47, difficulty=1.98)
graph.add_edge("N1", "N7", 66, difficulty=1.91)
graph.add_edge("N1", "N18", 60, difficulty=1.64)
graph.add_edge("N1", "N5", 48, difficulty=1.9)
graph.add_edge("N1", "N11", 13, difficulty=1.57)
graph.add_edge("N17", "N11", 32, difficulty=1.42)
graph.add_edge("N17", "N10", 91, difficulty=1.39)
graph.add_edge("N17", "N5", 52, difficulty=1.9)
graph.add_edge("N14", "N9", 69, difficulty=1.63)
graph.add_edge("N14", "N12", 32, difficulty=1.82)
graph.add_edge("N14", "N11", 28, difficulty=1.79)
graph.add_edge("N0", "N12", 55, difficulty=1.99)

# Wêz³y grafu
nodes = ['N0', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19']

# Odleg³oœci miêdzy wierzcho³kami
distances = {('N4', 'N3'): 47, ('N3', 'N4'): 47, ('N19', 'N10'): 77, ('N10', 'N19'): 77, ('N7', 'N6'): 62, ('N6', 'N7'): 62, ('N12', 'N5'): 76, ('N5', 'N12'): 76, ('N8', 'N16'): 72, ('N16', 'N8'): 72, ('N5', 'N19'): 40, ('N19', 'N5'): 40, ('N13', 'N11'): 45, ('N11', 'N13'): 45, ('N9', 'N18'): 23, ('N18', 'N9'): 23, ('N15', 'N7'): 34, ('N7', 'N15'): 34, ('N12', 'N15'): 71, ('N15', 'N12'): 71, ('N5', 'N4'): 64, ('N4', 'N5'): 64, ('N2', 'N1'): 47, ('N1', 'N2'): 47, ('N1', 'N7'): 66, ('N7', 'N1'): 66, ('N18', 'N2'): 64, ('N2', 'N18'): 64, ('N4', 'N9'): 48, ('N9', 'N4'): 48, ('N7', 'N4'): 69, ('N4', 'N7'): 69, ('N18', 'N4'): 30, ('N4', 'N18'): 30, ('N17', 'N11'): 32, ('N11', 'N17'): 32, ('N11', 'N10'): 39, ('N10', 'N11'): 39, ('N18', 'N3'): 43, ('N3', 'N18'): 43, ('N15', 'N4'): 87, ('N4', 'N15'): 87, ('N18', 'N6'): 84, ('N6', 'N18'): 84, ('N17', 'N10'): 91, ('N10', 'N17'): 91, ('N9', 'N14'): 69, ('N14', 'N9'): 69, ('N14', 'N12'): 32, ('N12', 'N14'): 32, ('N18', 'N1'): 60, ('N1', 'N18'): 60, ('N1', 'N5'): 48, ('N5', 'N1'): 48, ('N18', 'N10'): 73, ('N10', 'N18'): 73, ('N12', 'N0'): 55, ('N0', 'N12'): 55, ('N19', 'N12'): 11, ('N12', 'N19'): 11, ('N1', 'N11'): 13, ('N11', 'N1'): 13, ('N14', 'N11'): 28, ('N11', 'N14'): 28, ('N12', 'N11'): 16, ('N11', 'N12'): 16, ('N16', 'N15'): 88, ('N15', 'N16'): 88, ('N7', 'N10'): 57, ('N10', 'N7'): 57, ('N5', 'N17'): 52, ('N17', 'N5'): 52}

# Wygenerowane stacje ³adowania
stations = {
    "N10": ChargingStation("N10", 71, 62, price_per_kwh=0.47, queue_time=0.21, max_power=45),
    "N8": ChargingStation("N8", 70, 74, price_per_kwh=0.69, queue_time=0.39, max_power=41),
    "N4": ChargingStation("N4", 9, 38, price_per_kwh=0.65, queue_time=0.42, max_power=68),
    "N17": ChargingStation("N17", 99, 57, price_per_kwh=0.61, queue_time=0.33, max_power=31),
    "N13": ChargingStation("N13", 96, 59, price_per_kwh=0.57, queue_time=0.31, max_power=32),
}
