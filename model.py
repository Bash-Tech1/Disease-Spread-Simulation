from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random

class Person(Agent):
    """
    Agent representing a person in the SIR model.
    States: Susceptible (S), Infected (I), Recovered (R)
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "S"  # Initial state: Susceptible
        self.infection_duration = 0
        self.vaccinated = False
        self.quarantined = False
        
        # Randomly vaccinate 30% of population
        if random.random() < 0.3:
            self.vaccinated = True

    def move(self):
        """
        Move agent to random adjacent cell if not quarantined
        """
        if not self.quarantined:
            possible_steps = self.model.grid.get_neighborhood(
                self.pos, moore=True, include_center=False
            )
            if possible_steps:
                new_position = self.random.choice(possible_steps)
                self.model.grid.move_agent(self, new_position)

    def step(self):
        """
        Handle agent behavior during each step
        """
        self.move()
        
        # Check for recovery
        if self.state == "I":
            self.infection_duration += 1
            if self.infection_duration >= self.model.recovery_time:
                self.state = "R"
                self.quarantined = False  # Release from quarantine


class DiseaseModel(Model):
    """
    Main model for disease spread simulation
    """
    def __init__(self, N=100, width=20, height=20, infection_rate=0.3, 
                 recovery_time=7, quarantine_effectiveness=0.5):
        super().__init__()
        self.num_agents = N
        self.infection_rate = infection_rate
        self.recovery_time = recovery_time
        self.quarantine_effectiveness = quarantine_effectiveness
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        
        # Create agents
        for i in range(self.num_agents):
            agent = Person(i, self)
            self.schedule.add(agent)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))
        
        # Infect initial patient zero
        patient_zero = self.random.choice(self.schedule.agents)
        patient_zero.state = "I"
        self.move_to_quarantine(patient_zero)
        
        # Set up data collection
        self.datacollector = DataCollector(
            agent_reporters={"State": "state"},
            model_reporters={
                "Susceptible": lambda m: self.count_agents(m, "S"),
                "Infected": lambda m: self.count_agents(m, "I"),
                "Recovered": lambda m: self.count_agents(m, "R")
            }
        )

    def move_to_quarantine(self, agent):
        """
        Move infected agents to quarantine zone (left 5 columns)
        """
        if random.random() < self.quarantine_effectiveness:
            x = self.random.randint(0, 4)  # Quarantine zone columns 0-4
            y = self.random.randint(0, self.grid.height - 1)
            self.grid.move_agent(agent, (x, y))
            agent.quarantined = True

    @staticmethod
    def count_agents(model, state):
        """
        Helper method to count agents in specific state
        """
        return sum(1 for agent in model.schedule.agents if agent.state == state)

    def step(self):
        """
        Advance the model by one step
        """
        # Collect data first
        self.datacollector.collect(self)
        
        # Infect neighboring agents
        for agent in self.schedule.agents:
            if agent.state == "I" and not agent.quarantined:
                neighbors = self.grid.get_neighbors(agent.pos, moore=True)
                for neighbor in neighbors:
                    if (neighbor.state == "S" and 
                        not neighbor.vaccinated and 
                        random.random() < self.infection_rate):
                        neighbor.state = "I"
                        self.move_to_quarantine(neighbor)
        
        # Advance all agents
        self.schedule.step()