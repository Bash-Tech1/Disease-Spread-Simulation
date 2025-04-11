# Disease Spread Simulation

This project shows how a disease like COVID-19 can spread in a population.

It doesn’t use real people or cities. It uses simple moving dots (we call them “agents”) on a grid. Each dot can be:
- Healthy (not sick yet)
- Infected (can infect others)
- Recovered (got better and can’t get sick again)

The simulation helps you understand:
- How quickly a disease can spread
- How quarantine helps stop the spread
- What happens when people recover

You can see everything visually in your browser.

---

## 🔍 What This Project Does

### Step 1: Imagine a Town of Dots
- Each dot is a person.
- All the dots walk around randomly.

### Step 2: One Dot Gets Sick
- A few dots start off as “infected”.

### Step 3: Infection Spreads
- If a healthy dot gets close to an infected one, it might get sick too.
- The chance of getting infected is controlled by a number you can change.

### Step 4: People Recover
- After a certain number of steps (like days), infected dots become recovered.
- They don’t get sick again.

### Step 5: Quarantine Option
- You can turn on a rule that makes infected dots stop moving.
- This shows how isolation helps slow down infections.

### Step 6: Watch It Happen
- You can watch the dots in real-time in your browser.
- Green = healthy  
- Red = infected  
- Blue = recovered

### Step 7: Track the Numbers
- The system counts how many are healthy, infected, or recovered each step.
- It saves this data so you can open it in Excel or Google Sheets.

---

## ✅ What You Learn

- How diseases spread in crowded areas
- Why recovery time matters
- How quarantine flattens the curve
- What happens when people stop interacting

This is not just for coding—it’s for learning how society reacts to viruses.

---

## Installation

```bash
git clone https://github.com/your-username/disease-simulation.git
cd disease-simulation
pip install -r requirements.txt
