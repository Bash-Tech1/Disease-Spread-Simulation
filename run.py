import matplotlib.pyplot as plt
import pandas as pd
from model import DiseaseModel
from tqdm import tqdm  # Optional for progress bars

def run_simulation(params, num_runs=5, max_steps=100):
    """
    Run multiple simulations with given parameters
    Returns aggregated data for analysis
    """
    all_data = []
    
    for run in range(num_runs):
        model = DiseaseModel(
            N=params["N"],
            infection_rate=params["infection_rate"],
            recovery_time=params["recovery_time"],
            quarantine_effectiveness=params["quarantine_effectiveness"]
        )
        
        for step in range(max_steps):
            model.step()
            current_data = model.datacollector.get_model_vars_dataframe()
            current_data["Run"] = run
            current_data["Step"] = step
            all_data.append(current_data.iloc[-1])
            
    return pd.DataFrame(all_data)

def analyze_results(df):
    """
    Analyze and plot simulation results
    """
    # Calculate averages across runs
    avg_results = df.groupby("Step").agg({
        "Susceptible": "mean",
        "Infected": "mean",
        "Recovered": "mean"
    }).reset_index()
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(avg_results["Step"], avg_results["Susceptible"], label="Susceptible", color="green")
    plt.plot(avg_results["Step"], avg_results["Infected"], label="Infected", color="red")
    plt.plot(avg_results["Step"], avg_results["Recovered"], label="Recovered", color="blue")
    
    plt.title("Disease Spread Simulation Results")
    plt.xlabel("Time Steps")
    plt.ylabel("Number of Agents")
    plt.legend()
    plt.grid(True)
    
    # Save and show
    plt.savefig("simulation_results.png")
    plt.show()
    
    # Save raw data
    df.to_csv("simulation_data.csv", index=False)

if __name__ == "__main__":
    # Example parameters
    base_params = {
        "N": 200,
        "infection_rate": 0.4,
        "recovery_time": 7,
        "quarantine_effectiveness": 0.6
    }
    
    # Run simulations
    print("Running simulations...")
    results_df = run_simulation(base_params, num_runs=10, max_steps=50)
    
    # Analyze and plot
    print("Analyzing results...")
    analyze_results(results_df)
    
    print("Done! Check simulation_results.png and simulation_data.csv")