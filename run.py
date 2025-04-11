from model import DiseaseModel
import matplotlib.pyplot as plt

# Configuration
steps = 50
population = 100
grid_width = 20
grid_height = 20
infection_chance = 0.2
recovery_time = 10
use_quarantine = True

# Run simulation
model = DiseaseModel(
    N=population,
    width=grid_width,
    height=grid_height,
    infection_chance=infection_chance,
    recovery_time=recovery_time,
    use_quarantine=use_quarantine
)

for _ in range(steps):
    model.step()

# Export to CSV
model.export_data("results.csv")
print("Results saved to results.csv")

# Plot results
df = model.datacollector.get_model_vars_dataframe()
df.plot(title="Disease Spread Over Time", figsize=(10, 6))
plt.xlabel("Step")
plt.ylabel("Number of Agents")
plt.tight_layout()
plt.show()
