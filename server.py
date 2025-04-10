from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter
from model import DiseaseModel

# Agent portrayal with vaccination distinction
def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "Layer": 0,
        "r": 0.5,
        "text": "🩹" if agent.vaccinated else "",
        "text_color": "white"
    }
    
    # Color coding with vaccine distinction
    if agent.state == "S":
        portrayal["Color"] = "yellow" if agent.vaccinated else "green"
    elif agent.state == "I":
        portrayal["Color"] = "red"
    else:  # Recovered
        portrayal["Color"] = "blue"
    
    # Quarantine border
    if agent.quarantined:
        portrayal["stroke_color"] = "black"
        portrayal["stroke_width"] = 2
        
    return portrayal

# Create grid visualization
grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)

# Chart for S/I/R tracking
chart = ChartModule([{"Label": "Susceptible", "Color": "green"},
                    {"Label": "Infected", "Color": "red"},
                    {"Label": "Recovered", "Color": "blue"}])

# Interactive parameters
model_params = {
    "N": UserSettableParameter(
        "slider", "Number of Agents", 100, 10, 300, 10,
        description="Initial population size"
    ),
    "infection_rate": UserSettableParameter(
        "slider", "Infection Rate", 0.3, 0.1, 1.0, 0.05,
        description="Probability of infection transmission"
    ),
    "recovery_time": UserSettableParameter(
        "slider", "Recovery Time (days)", 7, 3, 14, 1,
        description="Days until recovery"
    ),
    "quarantine_effectiveness": UserSettableParameter(
        "slider", "Quarantine Effectiveness", 0.5, 0.0, 1.0, 0.1,
        description="Probability infected enter quarantine"
    ),
    "width": 20,
    "height": 20
}

# Create server
server = ModularServer(DiseaseModel,
                       [grid, chart],
                       "Disease Spread Simulation",
                       model_params)

# Optional: For direct execution
if __name__ == "__main__":
    server.launch()