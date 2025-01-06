from src.graph import Graph
from src.charging_station import ChargingStation

# Wygenerowany graf
graph = Graph()
graph.add_edge("A", "BF", 226, difficulty=1.54)
graph.add_edge("BF", "A", 226, difficulty=1.54)
graph.add_edge("A", "AV", 116, difficulty=1.07)
graph.add_edge("AV", "A", 116, difficulty=1.07)
graph.add_edge("A", "BB", 263, difficulty=1.88)
graph.add_edge("BB", "A", 263, difficulty=1.88)
graph.add_edge("B", "D", 245, difficulty=1.23)
graph.add_edge("D", "B", 245, difficulty=1.23)
graph.add_edge("B", "N", 54, difficulty=1.96)
graph.add_edge("N", "B", 54, difficulty=1.96)
graph.add_edge("B", "AQ", 132, difficulty=1.8)
graph.add_edge("AQ", "B", 132, difficulty=1.8)
graph.add_edge("C", "BE", 263, difficulty=1.06)
graph.add_edge("BE", "C", 263, difficulty=1.06)
graph.add_edge("C", "BB", 181, difficulty=1.08)
graph.add_edge("BB", "C", 181, difficulty=1.08)
graph.add_edge("D", "I", 262, difficulty=1.97)
graph.add_edge("I", "D", 262, difficulty=1.97)
graph.add_edge("D", "BF", 249, difficulty=1.6)
graph.add_edge("BF", "D", 249, difficulty=1.6)
graph.add_edge("D", "AT", 72, difficulty=1.99)
graph.add_edge("AT", "D", 72, difficulty=1.99)
graph.add_edge("E", "AX", 124, difficulty=1.16)
graph.add_edge("AX", "E", 124, difficulty=1.16)
graph.add_edge("F", "H", 262, difficulty=1.48)
graph.add_edge("H", "F", 262, difficulty=1.48)
graph.add_edge("F", "A", 144, difficulty=1.64)
graph.add_edge("A", "F", 144, difficulty=1.64)
graph.add_edge("F", "AR", 274, difficulty=1.74)
graph.add_edge("AR", "F", 274, difficulty=1.74)
graph.add_edge("G", "BD", 168, difficulty=1.99)
graph.add_edge("BD", "G", 168, difficulty=1.99)
graph.add_edge("G", "BK", 273, difficulty=1.85)
graph.add_edge("BK", "G", 273, difficulty=1.85)
graph.add_edge("G", "AX", 52, difficulty=1.36)
graph.add_edge("AX", "G", 52, difficulty=1.36)
graph.add_edge("H", "L", 178, difficulty=1.49)
graph.add_edge("L", "H", 178, difficulty=1.49)
graph.add_edge("I", "AZ", 74, difficulty=1.11)
graph.add_edge("AZ", "I", 74, difficulty=1.11)
graph.add_edge("I", "AS", 109, difficulty=1.37)
graph.add_edge("AS", "I", 109, difficulty=1.37)
graph.add_edge("I", "BN", 291, difficulty=1.83)
graph.add_edge("BN", "I", 291, difficulty=1.83)
graph.add_edge("J", "AY", 104, difficulty=1.76)
graph.add_edge("AY", "J", 104, difficulty=1.76)
graph.add_edge("J", "BE", 211, difficulty=1.66)
graph.add_edge("BE", "J", 211, difficulty=1.66)
graph.add_edge("J", "BN", 236, difficulty=1.17)
graph.add_edge("BN", "J", 236, difficulty=1.17)
graph.add_edge("K", "AS", 145, difficulty=1.89)
graph.add_edge("AS", "K", 145, difficulty=1.89)
graph.add_edge("K", "BI", 111, difficulty=1.91)
graph.add_edge("BI", "K", 111, difficulty=1.91)
graph.add_edge("L", "AT", 215, difficulty=1.25)
graph.add_edge("AT", "L", 215, difficulty=1.25)
graph.add_edge("M", "J", 162, difficulty=1.48)
graph.add_edge("J", "M", 162, difficulty=1.48)
graph.add_edge("M", "BN", 163, difficulty=1.79)
graph.add_edge("BN", "M", 163, difficulty=1.79)
graph.add_edge("M", "D", 262, difficulty=1.81)
graph.add_edge("D", "M", 262, difficulty=1.81)
graph.add_edge("N", "BM", 135, difficulty=1.57)
graph.add_edge("BM", "N", 135, difficulty=1.57)
graph.add_edge("O", "K", 249, difficulty=1.08)
graph.add_edge("K", "O", 249, difficulty=1.08)
graph.add_edge("P", "AR", 211, difficulty=1.87)
graph.add_edge("AR", "P", 211, difficulty=1.87)
graph.add_edge("P", "AV", 73, difficulty=1.55)
graph.add_edge("AV", "P", 73, difficulty=1.55)
graph.add_edge("AQ", "BG", 278, difficulty=1.76)
graph.add_edge("BG", "AQ", 278, difficulty=1.76)
graph.add_edge("AQ", "L", 82, difficulty=1.69)
graph.add_edge("L", "AQ", 82, difficulty=1.69)
graph.add_edge("AR", "AT", 270, difficulty=1.92)
graph.add_edge("AT", "AR", 270, difficulty=1.92)
graph.add_edge("AS", "P", 133, difficulty=1.83)
graph.add_edge("P", "AS", 133, difficulty=1.83)
graph.add_edge("AT", "BH", 180, difficulty=1.92)
graph.add_edge("BH", "AT", 180, difficulty=1.92)
graph.add_edge("AT", "K", 259, difficulty=1.16)
graph.add_edge("K", "AT", 259, difficulty=1.16)
graph.add_edge("AU", "BE", 143, difficulty=1.11)
graph.add_edge("BE", "AU", 143, difficulty=1.11)
graph.add_edge("AU", "AY", 300, difficulty=1.86)
graph.add_edge("AY", "AU", 300, difficulty=1.86)
graph.add_edge("AU", "BN", 232, difficulty=1.29)
graph.add_edge("BN", "AU", 232, difficulty=1.29)
graph.add_edge("AV", "I", 79, difficulty=1.63)
graph.add_edge("I", "AV", 79, difficulty=1.63)
graph.add_edge("AV", "D", 217, difficulty=1.27)
graph.add_edge("D", "AV", 217, difficulty=1.27)
graph.add_edge("AV", "C", 295, difficulty=1.28)
graph.add_edge("C", "AV", 295, difficulty=1.28)
graph.add_edge("AW", "F", 264, difficulty=1.61)
graph.add_edge("F", "AW", 264, difficulty=1.61)
graph.add_edge("AX", "M", 123, difficulty=1.28)
graph.add_edge("M", "AX", 123, difficulty=1.28)
graph.add_edge("AX", "BH", 186, difficulty=1.97)
graph.add_edge("BH", "AX", 186, difficulty=1.97)
graph.add_edge("AY", "BE", 159, difficulty=1.48)
graph.add_edge("BE", "AY", 159, difficulty=1.48)
graph.add_edge("AY", "H", 273, difficulty=1.37)
graph.add_edge("H", "AY", 273, difficulty=1.37)
graph.add_edge("AY", "BJ", 99, difficulty=1.78)
graph.add_edge("BJ", "AY", 99, difficulty=1.78)
graph.add_edge("AZ", "O", 100, difficulty=1.71)
graph.add_edge("O", "AZ", 100, difficulty=1.71)
graph.add_edge("AZ", "D", 137, difficulty=1.04)
graph.add_edge("D", "AZ", 137, difficulty=1.04)
graph.add_edge("AZ", "BJ", 261, difficulty=1.74)
graph.add_edge("BJ", "AZ", 261, difficulty=1.74)
graph.add_edge("BA", "BM", 145, difficulty=1.66)
graph.add_edge("BM", "BA", 145, difficulty=1.66)
graph.add_edge("BA", "BJ", 255, difficulty=1.25)
graph.add_edge("BJ", "BA", 255, difficulty=1.25)
graph.add_edge("BA", "J", 262, difficulty=1.11)
graph.add_edge("J", "BA", 262, difficulty=1.11)
graph.add_edge("BB", "BD", 248, difficulty=1.15)
graph.add_edge("BD", "BB", 248, difficulty=1.15)
graph.add_edge("BB", "H", 57, difficulty=1.08)
graph.add_edge("H", "BB", 57, difficulty=1.08)
graph.add_edge("BC", "AT", 295, difficulty=1.66)
graph.add_edge("AT", "BC", 295, difficulty=1.66)
graph.add_edge("BC", "AU", 70, difficulty=1.98)
graph.add_edge("AU", "BC", 70, difficulty=1.98)
graph.add_edge("BD", "BG", 254, difficulty=1.31)
graph.add_edge("BG", "BD", 254, difficulty=1.31)
graph.add_edge("BE", "BC", 196, difficulty=1.15)
graph.add_edge("BC", "BE", 196, difficulty=1.15)
graph.add_edge("BE", "AX", 295, difficulty=1.61)
graph.add_edge("AX", "BE", 295, difficulty=1.61)
graph.add_edge("BE", "H", 107, difficulty=1.41)
graph.add_edge("H", "BE", 107, difficulty=1.41)
graph.add_edge("BF", "BC", 219, difficulty=1.68)
graph.add_edge("BC", "BF", 219, difficulty=1.68)
graph.add_edge("BF", "AV", 84, difficulty=1.04)
graph.add_edge("AV", "BF", 84, difficulty=1.04)
graph.add_edge("BF", "AU", 269, difficulty=1.67)
graph.add_edge("AU", "BF", 269, difficulty=1.67)
graph.add_edge("BG", "BH", 92, difficulty=1.75)
graph.add_edge("BH", "BG", 92, difficulty=1.75)
graph.add_edge("BH", "BL", 197, difficulty=1.26)
graph.add_edge("BL", "BH", 197, difficulty=1.26)
graph.add_edge("BI", "J", 250, difficulty=1.62)
graph.add_edge("J", "BI", 250, difficulty=1.62)
graph.add_edge("BJ", "AU", 290, difficulty=1.12)
graph.add_edge("AU", "BJ", 290, difficulty=1.12)
graph.add_edge("BJ", "K", 148, difficulty=1.83)
graph.add_edge("K", "BJ", 148, difficulty=1.83)
graph.add_edge("BK", "A", 277, difficulty=1.57)
graph.add_edge("A", "BK", 277, difficulty=1.57)
graph.add_edge("BL", "H", 118, difficulty=1.55)
graph.add_edge("H", "BL", 118, difficulty=1.55)
graph.add_edge("BL", "F", 126, difficulty=1.86)
graph.add_edge("F", "BL", 126, difficulty=1.86)
graph.add_edge("BM", "AT", 71, difficulty=1.02)
graph.add_edge("AT", "BM", 71, difficulty=1.02)
graph.add_edge("BN", "AT", 194, difficulty=1.92)
graph.add_edge("AT", "BN", 194, difficulty=1.92)
graph.add_edge("BN", "AW", 92, difficulty=1.97)
graph.add_edge("AW", "BN", 92, difficulty=1.97)

# W�z�y grafu
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN']

# Odleg�o�ci mi�dzy wierzcho�kami
distances = {
    ("A", "BF"): 226,
    ("A", "AV"): 116,
    ("A", "BB"): 263,
    ("B", "D"): 245,
    ("B", "N"): 54,
    ("B", "AQ"): 132,
    ("C", "BE"): 263,
    ("C", "BB"): 181,
    ("D", "I"): 262,
    ("D", "BF"): 249,
    ("D", "AT"): 72,
    ("E", "AX"): 124,
    ("F", "H"): 262,
    ("F", "A"): 144,
    ("F", "AR"): 274,
    ("G", "BD"): 168,
    ("G", "BK"): 273,
    ("G", "AX"): 52,
    ("H", "L"): 178,
    ("I", "AZ"): 74,
    ("I", "AS"): 109,
    ("I", "BN"): 291,
    ("J", "AY"): 104,
    ("J", "BE"): 211,
    ("J", "BN"): 236,
    ("K", "AS"): 145,
    ("K", "BI"): 111,
    ("L", "AT"): 215,
    ("M", "J"): 162,
    ("M", "BN"): 163,
    ("M", "D"): 262,
    ("N", "BM"): 135,
    ("O", "K"): 249,
    ("P", "AR"): 211,
    ("P", "AV"): 73,
    ("AQ", "BG"): 278,
    ("AQ", "L"): 82,
    ("AR", "AT"): 270,
    ("AS", "P"): 133,
    ("AT", "BH"): 180,
    ("AT", "K"): 259,
    ("AU", "BE"): 143,
    ("AU", "AY"): 300,
    ("AU", "BN"): 232,
    ("AV", "I"): 79,
    ("AV", "D"): 217,
    ("AV", "C"): 295,
    ("AW", "F"): 264,
    ("AX", "M"): 123,
    ("AX", "BH"): 186,
    ("AY", "BE"): 159,
    ("AY", "H"): 273,
    ("AY", "BJ"): 99,
    ("AZ", "O"): 100,
    ("AZ", "D"): 137,
    ("AZ", "BJ"): 261,
    ("BA", "BM"): 145,
    ("BA", "BJ"): 255,
    ("BA", "J"): 262,
    ("BB", "BD"): 248,
    ("BB", "H"): 57,
    ("BC", "AT"): 295,
    ("BC", "AU"): 70,
    ("BD", "BG"): 254,
    ("BE", "BC"): 196,
    ("BE", "AX"): 295,
    ("BE", "H"): 107,
    ("BF", "BC"): 219,
    ("BF", "AV"): 84,
    ("BF", "AU"): 269,
    ("BG", "BH"): 92,
    ("BH", "BL"): 197,
    ("BI", "J"): 250,
    ("BJ", "AU"): 290,
    ("BJ", "K"): 148,
    ("BK", "A"): 277,
    ("BL", "H"): 118,
    ("BL", "F"): 126,
    ("BM", "AT"): 71,
    ("BN", "AT"): 194,
    ("BN", "AW"): 92,
}

# Wygenerowane stacje �adowania
stations = {
    "AS": ChargingStation("AS", 50, 300, price_per_kwh=0.7, queue_time=0.19, max_power=87),
    "BL": ChargingStation("BL", 50, 300, price_per_kwh=0.44, queue_time=0.22, max_power=49),
    "BD": ChargingStation("BD", 50, 300, price_per_kwh=0.61, queue_time=0.23, max_power=81),
    "AR": ChargingStation("AR", 50, 300, price_per_kwh=0.67, queue_time=0.33, max_power=68),
    "E": ChargingStation("E", 50, 300, price_per_kwh=0.66, queue_time=0.2, max_power=88),
    "AU": ChargingStation("AU", 50, 300, price_per_kwh=0.77, queue_time=0.33, max_power=76),
    "M": ChargingStation("M", 50, 300, price_per_kwh=0.68, queue_time=0.21, max_power=62),
    "BJ": ChargingStation("BJ", 50, 300, price_per_kwh=0.44, queue_time=0.42, max_power=75),
    "AW": ChargingStation("AW", 50, 300, price_per_kwh=0.76, queue_time=0.49, max_power=64),
    "BB": ChargingStation("BB", 50, 300, price_per_kwh=0.6, queue_time=0.17, max_power=100),
    "J": ChargingStation("J", 50, 300, price_per_kwh=0.5, queue_time=0.5, max_power=30),
    "F": ChargingStation("F", 50, 300, price_per_kwh=0.73, queue_time=0.22, max_power=63),
}
