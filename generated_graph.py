from src.graph import Graph
from src.charging_station import ChargingStation

# Wygenerowany graf
graph = Graph()
graph.add_edge("N13", "N11", 79, difficulty=1.69)
graph.add_edge("N13", "N17", 58, difficulty=1.89)
graph.add_edge("N13", "N1", 10, difficulty=1.68)
graph.add_edge("N13", "N19", 24, difficulty=1.47)
graph.add_edge("N13", "N14", 72, difficulty=1.78)
graph.add_edge("N13", "N12", 11, difficulty=1.32)
graph.add_edge("N11", "N13", 79, difficulty=1.69)
graph.add_edge("N11", "N1", 60, difficulty=1.47)
graph.add_edge("N2", "N3", 34, difficulty=1.07)
graph.add_edge("N2", "N10", 75, difficulty=1.74)
graph.add_edge("N2", "N0", 25, difficulty=1.7)
graph.add_edge("N2", "N16", 35, difficulty=1.89)
graph.add_edge("N2", "N14", 59, difficulty=1.78)
graph.add_edge("N3", "N2", 34, difficulty=1.07)
graph.add_edge("N3", "N5", 26, difficulty=1.44)
graph.add_edge("N3", "N10", 92, difficulty=1.54)
graph.add_edge("N3", "N6", 42, difficulty=1.23)
graph.add_edge("N3", "N19", 61, difficulty=1.54)
graph.add_edge("N3", "N17", 84, difficulty=1.91)
graph.add_edge("N17", "N15", 79, difficulty=1.5)
graph.add_edge("N17", "N13", 58, difficulty=1.89)
graph.add_edge("N17", "N7", 42, difficulty=1.97)
graph.add_edge("N17", "N10", 71, difficulty=1.82)
graph.add_edge("N17", "N3", 84, difficulty=1.91)
graph.add_edge("N15", "N17", 79, difficulty=1.5)
graph.add_edge("N15", "N6", 48, difficulty=1.19)
graph.add_edge("N15", "N10", 30, difficulty=1.35)
graph.add_edge("N15", "N8", 29, difficulty=1.04)
graph.add_edge("N15", "N14", 13, difficulty=1.92)
graph.add_edge("N5", "N3", 26, difficulty=1.44)
graph.add_edge("N5", "N16", 69, difficulty=1.32)
graph.add_edge("N14", "N19", 47, difficulty=1.74)
graph.add_edge("N14", "N15", 13, difficulty=1.92)
graph.add_edge("N14", "N13", 72, difficulty=1.78)
graph.add_edge("N14", "N2", 59, difficulty=1.78)
graph.add_edge("N19", "N14", 47, difficulty=1.74)
graph.add_edge("N19", "N6", 88, difficulty=1.5)
graph.add_edge("N19", "N3", 61, difficulty=1.54)
graph.add_edge("N19", "N13", 24, difficulty=1.47)
graph.add_edge("N19", "N4", 27, difficulty=1.66)
graph.add_edge("N12", "N8", 83, difficulty=1.35)
graph.add_edge("N12", "N13", 11, difficulty=1.32)
graph.add_edge("N8", "N12", 83, difficulty=1.35)
graph.add_edge("N8", "N15", 29, difficulty=1.04)
graph.add_edge("N1", "N11", 60, difficulty=1.47)
graph.add_edge("N1", "N13", 10, difficulty=1.68)
graph.add_edge("N6", "N19", 88, difficulty=1.5)
graph.add_edge("N6", "N15", 48, difficulty=1.19)
graph.add_edge("N6", "N3", 42, difficulty=1.23)
graph.add_edge("N10", "N3", 92, difficulty=1.54)
graph.add_edge("N10", "N2", 75, difficulty=1.74)
graph.add_edge("N10", "N15", 30, difficulty=1.35)
graph.add_edge("N10", "N17", 71, difficulty=1.82)
graph.add_edge("N10", "N18", 26, difficulty=1.21)
graph.add_edge("N10", "N0", 42, difficulty=1.86)
graph.add_edge("N0", "N2", 25, difficulty=1.7)
graph.add_edge("N0", "N10", 42, difficulty=1.86)
graph.add_edge("N7", "N17", 42, difficulty=1.97)
graph.add_edge("N16", "N2", 35, difficulty=1.89)
graph.add_edge("N16", "N5", 69, difficulty=1.32)
graph.add_edge("N4", "N18", 65, difficulty=1.37)
graph.add_edge("N4", "N19", 27, difficulty=1.66)
graph.add_edge("N18", "N4", 65, difficulty=1.37)
graph.add_edge("N18", "N10", 26, difficulty=1.21)

# Wêz³y grafu
nodes = ['N0', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19']

# Odleg³oœci miêdzy wierzcho³kami
distances = {('N13', 'N11'): 79, ('N11', 'N13'): 79, ('N2', 'N3'): 34, ('N3', 'N2'): 34, ('N17', 'N15'): 79, ('N15', 'N17'): 79, ('N5', 'N3'): 26, ('N3', 'N5'): 26, ('N14', 'N19'): 47, ('N19', 'N14'): 47, ('N12', 'N8'): 83, ('N8', 'N12'): 83, ('N11', 'N1'): 60, ('N1', 'N11'): 60, ('N19', 'N6'): 88, ('N6', 'N19'): 88, ('N3', 'N10'): 92, ('N10', 'N3'): 92, ('N15', 'N6'): 48, ('N6', 'N15'): 48, ('N2', 'N10'): 75, ('N10', 'N2'): 75, ('N0', 'N2'): 25, ('N2', 'N0'): 25, ('N17', 'N13'): 58, ('N13', 'N17'): 58, ('N13', 'N1'): 10, ('N1', 'N13'): 10, ('N7', 'N17'): 42, ('N17', 'N7'): 42, ('N6', 'N3'): 42, ('N3', 'N6'): 42, ('N2', 'N16'): 35, ('N16', 'N2'): 35, ('N19', 'N3'): 61, ('N3', 'N19'): 61, ('N4', 'N18'): 65, ('N18', 'N4'): 65, ('N13', 'N19'): 24, ('N19', 'N13'): 24, ('N10', 'N15'): 30, ('N15', 'N10'): 30, ('N15', 'N8'): 29, ('N8', 'N15'): 29, ('N17', 'N10'): 71, ('N10', 'N17'): 71, ('N14', 'N15'): 13, ('N15', 'N14'): 13, ('N14', 'N13'): 72, ('N13', 'N14'): 72, ('N13', 'N12'): 11, ('N12', 'N13'): 11, ('N17', 'N3'): 84, ('N3', 'N17'): 84, ('N2', 'N14'): 59, ('N14', 'N2'): 59, ('N19', 'N4'): 27, ('N4', 'N19'): 27, ('N10', 'N18'): 26, ('N18', 'N10'): 26, ('N16', 'N5'): 69, ('N5', 'N16'): 69, ('N0', 'N10'): 42, ('N10', 'N0'): 42}

# Wygenerowane stacje ³adowania
stations = {
    "N2": ChargingStation("N2", 98, 57, price_per_kwh=0.51, queue_time=0.39, max_power=84),
    "N16": ChargingStation("N16", 13, 31, price_per_kwh=0.56, queue_time=0.31, max_power=56),
    "N15": ChargingStation("N15", 77, 45, price_per_kwh=0.77, queue_time=0.25, max_power=36),
    "N19": ChargingStation("N19", 56, 45, price_per_kwh=0.6, queue_time=0.17, max_power=38),
}
