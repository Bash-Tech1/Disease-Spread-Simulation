from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from model import DiseaseModel


def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "r": 0.8,
        "Layer": 0,
        "Color": "gray"
    }

    if agent.state == "Healthy":
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
    elif agent.state == "Infected":
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
    elif agent.state == "Recovered":
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 2

    return portrayal


grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)

model_params = {
    "N": UserSettableParameter("slider", "Population", 100, 10, 300, 10),
    "width": 20,
    "height": 20,
    "infection_chance": UserSettableParameter("slider", "Infection Chance", 0.2, 0.0, 1.0, 0.05),
    "recovery_time": UserSettableParameter("slider", "Recovery Time", 10, 1, 50, 1),
    "use_quarantine": UserSettableParameter("checkbox", "Enable Quarantine", True)
}

server = ModularServer(
    DiseaseModel,
    [grid],
    "Disease Spread Simulation",
    model_params
)

server.port = 8521
server.launch()
