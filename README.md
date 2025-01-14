# **EV Route Planner**

**EV Route Planner** is an application designed to optimize route planning for electric vehicles using an Ant Colony Optimization (ACO) algorithm. The project allows for custom graph definitions, random graph generation, and detailed parameter configuration for vehicles and the optimization process. Additionally, it provides insights and visualizations to analyze the results effectively.

---

## **Features**
- 🛤 **Route Optimization**: Finds the most optimal route between two nodes in a graph for an electric vehicle.
- 🧩 **Custom Graph Definition**: Supports manual graph input or random graph generation.
- 🔋 **Custom Vehicle Configuration**: Configure vehicle parameters such as battery capacity, energy consumption, and more.
- 🐜 **Ant Colony Optimization**: Implements an advanced ACO algorithm with configurable parameters like pheromone importance, evaporation rate, and heuristic weight.
- 📊 **Result Analysis**: Outputs the best route, total distance, average iteration time, and generates visualizations of key metrics such as performance and pheromone levels.

---
![image](https://github.com/user-attachments/assets/c6a80f22-e124-416e-8b45-15cdd6a9fbe3)
![image](https://github.com/user-attachments/assets/b208e992-b0a5-4cf1-896a-15a1c2699d49)

## **Getting Started**

### **Prerequisites**
To run the project, you'll need the following installed on your system:
- Python 3.8+
- Required libraries:
  - `Tkinter` (for GUI)
  - `matplotlib` (for visualizations)
  - `networkx` (for graph manipulation)

### **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/KomendaKacper/EVRoutePlanner.git
   ```
2. Navigate to the project directory:
   ```bash
   cd EVRoutePlanner
   ```
3. Install the required Python packages
---

## **Usage**
1. **Run the Application**:
   ```bash
   python main.py
   ```
2. **Set Up the Environment**:
   - Define the graph manually or generate a random one.
   - Configure vehicle and algorithm parameters, such as:
     - Battery capacity
     - Energy consumption
     - Number of ants
     - Number of iterations
     - Pheromone evaporation rate
   - Select start and end nodes.
3. **Run Optimization**:
   - View the optimal route, total distance, iteration statistics, and performance metrics.
   - Analyze the results using the provided visualizations.

---

## **How It Works**
1. **Graph Definition**:
   - Nodes represent locations.
   - Edges represent paths with attributes like distance and difficulty.
2. **Ant Colony Optimization**:
   - Ants explore the graph, using pheromones and heuristics to find optimal routes.
   - Pheromones are updated based on the quality of the paths discovered.
3. **Result Analysis**:
   - The algorithm outputs the best route, total distance, unique paths, and visual performance statistics.

---

## **Project Structure**
- `src/`: Contains the core logic and algorithm implementation.
  - `objective_function.py`: Defines the scoring function for route evaluation.
  - `ant_colony_optimization.py`: Implements the ACO algorithm.
- `main.py`: Entry point for the application.
- `README.md`: Project documentation.

---

## **Contributing**
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the coding guidelines.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
