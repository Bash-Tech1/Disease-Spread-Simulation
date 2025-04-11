from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector


class DiseaseAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "Healthy"  # Healthy, Infected, Recovered
        self.infection_duration = 0
        self.quarantined = False

    def step(self):
        if not self.quarantined:
            self.move()
        self.infect_or_recover()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def infect_or_recover(self):
        if self.state == "Infected":
            if not self.quarantined and self.model.use_quarantine:
                self.quarantined = True
            self.infection_duration += 1
            if self.infection_duration >= self.model.recovery_time:
                self.state = "Recovered"
                self.quarantined = False
        elif self.state == "Healthy":
            neighbors = self.model.grid.get_neighbors(
                self.pos,
                moore=True,
                include_center=False
            )
            for neighbor in neighbors:
                if neighbor.state == "Infected" and not neighbor.quarantined:
                    if self.random.random() < self.model.infection_chance:
                        self.state = "Infected"
                        break


class DiseaseModel(Model):
    def __init__(self, N, width, height, infection_chance=0.2, recovery_time=10, use_quarantine=True):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.infection_chance = infection_chance
        self.recovery_time = recovery_time
        self.use_quarantine = use_quarantine

        self.datacollector = DataCollector(
            model_reporters={
                "Healthy": lambda m: self.count_state("Healthy"),
                "Infected": lambda m: self.count_state("Infected"),
                "Recovered": lambda m: self.count_state("Recovered")
            }
        )

        for i in range(self.num_agents):
            a = DiseaseAgent(i, self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        # Infect 10% of agents
        infected_agents = self.random.sample(self.schedule.agents, max(1, N // 10))
        for agent in infected_agents:
            agent.state = "Infected"

        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

    def count_state(self, state_name):
        return sum(1 for a in self.schedule.agents if a.state == state_name)

    def export_data(self, filename="simulation_results.csv"):
        df = self.datacollector.get_model_vars_dataframe()
        df.to_csv(filename)
