# Disease Spread Simulation Project Tasks

## **Team Member 1: Project Setup & Dependencies**
**Objective:** Set up the project environment and dependencies.  
**Tasks:**  
1. Create a virtual environment and install packages:
   ```bash
   pip install mesa numpy matplotlib
   ```
2. Define the project structure:
   ```
   disease_simulation/
   ├── model.py
   ├── server.py
   ├── run.py
   └── requirements.txt
   ```
3. Ensure all dependencies are listed in `requirements.txt`.

---

## **Team Member 2: Agent States (SIR Model)**
**Objective:** Define agent states and movement.  
**Tasks:**  
1. Create a `Person` agent class with states: **S**, **I**, **R**.  
2. Implement random movement logic for agents on the grid.  
3. Example code for the `Person` class (see previous answer).

---

## **Team Member 3: Infection & Recovery Logic**
**Objective:** Implement disease transmission and recovery rules.  
**Tasks:**  
1. Add infection probability (`infection_rate`) between neighboring agents.  
2. Define recovery after `recovery_time` steps.  
3. Modify the `DiseaseModel` class to handle agent interactions.  
4. Test infection spread with initial conditions (e.g., 1 infected agent).

---

## **Team Member 4: Visualization (Mesa Server)**
**Objective:** Visualize agent states using Mesa.  
**Tasks:**  
1. Use `CanvasGrid` to display agents (green=S, red=I, blue=R).  
2. Set up the Mesa visualization server (`server.py`).  
3. Ensure the grid updates dynamically during simulation.

---

## **Team Member 5: Quarantine Strategy**
**Objective:** Add quarantine mechanics to reduce infections.  
**Tasks:**  
1. Designate a quarantine zone (e.g., left 5 grid columns).  
2. Modify infected agents’ movement to prioritize quarantine.  
3. Adjust interaction rules for quarantined agents.

---

## **Team Member 6: Data Collection & Analysis**
**Objective:** Track and analyze S/I/R data.  
**Tasks:**  
1. Use Mesa’s `DataCollector` to record agent states.  
2. Generate plots (e.g., infection curves) using Matplotlib.  
3. Export data to CSV for further analysis.

---

## **Team Member 7: Vaccination Impact**
**Objective:** Model vaccination effects.  
**Tasks:**  
1. Add a `vaccinated` property to agents.  
2. Define vaccination coverage (e.g., 30% start as vaccinated).  
3. Ensure vaccinated agents cannot be infected.  

---

## **Team Member 8: Experimentation & Final Report**
**Objective:** Test scenarios and compile documentation.  
**Tasks:**  
1. Run simulations with varied parameters (e.g., infection rates).  
2. Prepare:  
   - **Word File**: Code snippets, installation steps, run instructions.  
   - **Presentation**: Explain model design, results, and insights.  
   - **References**: Cite Mesa, SIR model papers, etc.  

---

# How to Run the Project
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the visualization:  
   ```bash
   mesa runserver server.py
   ```
3. Run simulations:  
   ```bash
   python run.py
   ```