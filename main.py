"""
main.py
The main training loop for the Q-Learning Snake AI.
Connects the Agent with the SnakeEnv across multiple training episodes.
"""

import config
from environment import SnakeEnv
from agent import Agent


def train():
    """
    Runs the reinforcement learning training pipeline.
    """
    # 1. Initialize environment and agent
    # Set render_mode=False for fast/headless training, or True to watch the snake play
    env = SnakeEnv(render_mode=True)
    agent = Agent()

    record = 0
    total_score = 0

    print("--- Starting Training Session ---")

    # 2. Iterate through training episodes
    for episode in range(1, config.NUM_EPISODES + 1):
        # Reset game and get initial 11-feature state
        state = env.reset()
        done = False

        # 3. Inner loop: Step-by-step game execution
        while not done:
            # Agent decides relative action (0=straight, 1=right, 2=left)
            action = agent.choose_action(state)

            # Environment applies physics, collisions, and returns outcomes
            next_state, reward, done, score = env.step(action)

            # Agent updates its Q-Table using the Bellman equation
            agent.learn(state, action, reward, next_state, done)

            # Transition to the next state
            state = next_state

        # 4. Post-episode updates and metrics
        agent.decay_epsilon()
        total_score += score

        if score > record:
            record = score

        # Print training progress
        print(f"Episode: {episode:<5} | Score: {score:<3} | Record: {record:<3} | Epsilon: {agent.epsilon:.4f}")


if __name__ == "__main__":
    train()