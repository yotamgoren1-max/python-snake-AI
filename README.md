# 🐍 Autonomous Snake AI (Q-Learning)

An autonomous AI agent trained to master the classic Snake game using **Tabular Q-Learning** (Reinforcement Learning) and **Pygame**, built from scratch without deep neural network dependencies.

The project demonstrates modular software architecture, mathematical modeling of state spaces, the Bellman Optimality Equation, an $\epsilon$-Greedy exploration-exploitation policy, and a custom Gymnasium-like environment interface.

---

## 🚀 Features
* **Custom RL Environment (`SnakeEnv`):** Fully decoupled game environment with a standardized interface (`reset` and `step`) inspired by OpenAI Gym / Gymnasium.
* **Compact 11-Feature State Space:** An efficient binary state representation capturing relative dangers (straight, right, left), current heading direction, and relative apple coordinates.
* **Epsilon-Greedy ($\epsilon$-Greedy) Exploration:** Balances trial-and-error discovery with exploitation of learned Q-values, featuring exponential decay and random tie-breaking.
* **Bellman Equation Updates:** True reinforcement learning updating expected cumulative rewards dynamically across state-action transitions.
* **Headless High-Speed Training:** Modular `render_mode` toggle allows running thousands of simulation steps per second without GPU overhead or Pygame rendering bottlenecks.
* **Loop Prevention (Starvation Guard):** Built-in timeout mechanic prevents the snake from entering infinite non-productive loops.

---

## 📂 Project Structure
* `main.py`: The entry point running the reinforcement learning training loop across episodes and tracking performance metrics (Score, Record, $\epsilon$).
* `environment.py`: Implements `SnakeEnv`, managing game physics, reward calculations, terminal conditions, and Pygame rendering.
* `agent.py`: Houses the `Agent` class (Q-Table memory, $\epsilon$-greedy action selection, Bellman updates, epsilon decay) and state extraction logic (`get_state`, `check_danger`, `get_next_direction`).
* `game_objects.py`: Encapsulates the physical entities (`Snake` and `Apple`) and low-level boundary/collision checks.
* `config.py`: Central repository for all hyperparameters (Learning Rate, Discount Factor, Rewards, Grid Dimensions, Clock Speeds).

---

## 🧠 State Representation (11-Feature Vector)

Rather than feeding raw pixels, the agent perceives the world through a compact, rotation-invariant boolean tuple:

$$\text{State} = [D_{\text{straight}}, D_{\text{right}}, D_{\text{left}}, \text{Dir}_U, \text{Dir}_R, \text{Dir}_D, \text{Dir}_L, A_{\text{down}}, A_{\text{right}}, A_{\text{up}}, A_{\text{left}}]$$

* **Indices 0–2 (Relative Dangers):** Wall or body collision detected directly ahead, to the right, or to the left relative to the current heading.
* **Indices 3–6 (Current Direction):** One-hot encoding of whether the snake is moving Up, Right, Down, or Left.
* **Indices 7–10 (Relative Food Location):** Spatial direction of the apple relative to the snake's head coordinates.

---

## 🔄 Architecture & Logic Flow

```text
 ┌────────────────────────────────────────────────────────────────────────┐
 │                              main.py                                   │
 │                       (RL Training Pipeline)                           │
 └───────────────────┬────────────────────────────────┬───────────────────┘
                     │                                │
        1. Current State (11-tuple)       3. Action (0=Straight, 1=Right, 2=Left)
                     │                                │
                     ▼                                ▼
       ┌───────────────────────────┐    ┌───────────────────────────┐
       │         Agent             │    │         SnakeEnv          │
       │        (agent.py)         │    │      (environment.py)     │
       ├───────────────────────────┤    ├───────────────────────────┤
       │ • Q-Table Memory          │    │ • Translate to 2D Vector  │
       │ • Epsilon-Greedy Policy   │    │ • snake.move()            │
       │ • Bellman Update (Learn)  │    │ • Collision & Eat Checks  │
       │ • Epsilon Decay           │    │ • Reward Allocation       │
       └─────────────▲─────────────┘    └─────────────┬─────────────┘
                     │                                │
                     │ 4. Outcome: (next_state, reward, done, score)
                     └────────────────────────────────┘