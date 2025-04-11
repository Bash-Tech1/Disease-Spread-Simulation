# Disease Spread Simulation

This project simulates the spread of an infectious disease using agent-based modeling with the [Mesa](https://mesa.readthedocs.io/en/stable/) framework.

## Features

- Agents can be Healthy, Infected, or Recovered
- Agents move randomly across a grid
- Infection spreads by contact
- Recovery happens after a fixed time
- Optional quarantine: infected agents stop moving
- Real-time visualization using Mesa web server
- CSV export of simulation results
- Matplotlib chart of infection trends

---

## Installation

```bash
git clone https://github.com/your-username/disease-simulation.git
cd disease-simulation
pip install -r requirements.txt
