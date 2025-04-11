# 🧪 Disease Spread Simulation – Explained Simply

This project is a small simulation that shows how a virus spreads in a population over time.

You don’t need real data or a real city. The idea is simple:
- Each **dot** on the screen is a person
- The dots move randomly on a grid
- Some dots are sick, and others are not

We use this setup to **test how the disease spreads**, how people **recover**, and how **quarantine** changes the results.

---

## 👥 Who are the dots?

Each dot is called an “agent.”  
Every agent can be in one of 3 states:

| State      | Color  | Meaning                             |
|------------|--------|-------------------------------------|
| Healthy    | Green  | Not infected yet                    |
| Infected   | Red    | Can infect others                   |
| Recovered  | Blue   | Got sick before, now immune         |

---

## 🧭 What happens in the simulation?

1. **Start with healthy people**
   - Most dots are healthy
   - A few are infected to begin with

2. **People move randomly**
   - Every dot walks around the grid in random directions

3. **Infection spreads**
   - If a healthy dot is next to an infected one, it *might* get infected too
   - The chance of getting infected is controlled by a number (e.g. 20%)

4. **People recover**
   - Infected people recover after a set time (e.g. 10 steps)
   - Once recovered, they turn blue and don’t get sick again

5. **Optional: Quarantine**
   - You can turn on a feature that makes infected people stop moving
   - This simulates real-world isolation and shows how it slows down the disease

---

## 📊 What can we track?

At each step, the simulation counts:
- How many people are **healthy**
- How many are **infected**
- How many are **recovered**

We save this data to a file and draw a graph to help you see what happened over time:
- You can see when the virus peaks
- How fast people recover
- Whether quarantine helped or not

---

## 🖥️ How do we use it?

You can run the simulation in two ways:

### 1. **With a Visual Interface**
Open it in your browser and watch the dots move and change color.  
You can control:
- Population size
- Infection chance
- Recovery time
- Quarantine ON/OFF

### 2. **Without a Visual Interface**
Run it from the terminal. It will:
- Simulate 50 steps
- Save results to a file called `results.csv`
- Show a graph of the results

---

## 💡 What does it teach?

This project is not about making a perfect model.  
It helps you understand:

- How diseases can spread even with a small number of infected people
- Why early isolation can slow things down
- How the infection curve rises and falls over time
- Why public health rules matter

---

## 🎓 Who should try this?

- Anyone who wants to understand virus spread
- Teachers showing how quarantine or recovery affects a population
- Students starting to learn programming or simulations
- Beginners in AI or data science
