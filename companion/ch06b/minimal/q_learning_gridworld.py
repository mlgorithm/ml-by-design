"""
Minimal Q-Learning Example: 4x4 Grid World
===========================================

Demonstrates tabular Q-learning with epsilon-greedy exploration
on a simple grid world with walls and a goal state.

Key concepts:
- State representation as (row, col) tuples
- Q-table mapping (state, action) -> value
- Temporal difference update: Q(s,a) <- Q(s,a) + alpha * [r + gamma * max Q(s',a') - Q(s,a)]
- Epsilon-greedy action selection
"""

import numpy as np
from typing import Tuple, List

# Set random seed for reproducibility
np.random.seed(42)

# ============================================================================
# Grid World Environment
# ============================================================================

class GridWorld:
    """Simple 4x4 grid world with walls and a goal."""

    def __init__(self):
        self.grid_size = 4
        self.start_pos = (0, 0)
        self.goal_pos = (3, 3)
        # Wall positions (obstacles)
        self.walls = {(1, 1), (1, 2)}
        self.pos = self.start_pos

    def reset(self):
        """Reset agent to start position."""
        self.pos = self.start_pos
        return self.pos

    def is_valid(self, row: int, col: int) -> bool:
        """Check if position is within bounds and not a wall."""
        in_bounds = 0 <= row < self.grid_size and 0 <= col < self.grid_size
        return in_bounds and (row, col) not in self.walls

    def step(self, action: int) -> Tuple[Tuple[int, int], float, bool]:
        """
        Execute action: 0=up, 1=right, 2=down, 3=left
        Returns: (next_state, reward, is_terminal)
        """
        row, col = self.pos

        # Action deltas
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        drow, dcol = deltas[action]
        new_row, new_col = row + drow, col + dcol

        # Stay in place if hitting wall or boundary
        if not self.is_valid(new_row, new_col):
            new_row, new_col = row, col

        self.pos = (new_row, new_col)

        # Reward: -1 per step (path cost), +10 for reaching goal
        reward = 10.0 if self.pos == self.goal_pos else -1.0

        is_terminal = self.pos == self.goal_pos

        return self.pos, reward, is_terminal

# ============================================================================
# Q-Learning Agent
# ============================================================================

class QLearningAgent:
    """Tabular Q-learning agent with epsilon-greedy exploration."""

    def __init__(self, num_states: int, num_actions: int = 4,
                 alpha: float = 0.1, gamma: float = 0.95, epsilon: float = 0.1):
        """
        Args:
            num_states: Total number of states (grid_size^2)
            num_actions: Number of actions (4 for grid: up, right, down, left)
            alpha: Learning rate
            gamma: Discount factor
            epsilon: Exploration probability
        """
        self.num_actions = num_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        # Q-table: map (state_idx, action) -> Q-value
        # Initialize to 0
        self.q_table = np.zeros((num_states, num_actions))

    def state_to_idx(self, state: Tuple[int, int], grid_size: int = 4) -> int:
        """Convert (row, col) to linear index."""
        row, col = state
        return row * grid_size + col

    def idx_to_state(self, idx: int, grid_size: int = 4) -> Tuple[int, int]:
        """Convert linear index to (row, col)."""
        return (idx // grid_size, idx % grid_size)

    def select_action(self, state: Tuple[int, int]) -> int:
        """Epsilon-greedy action selection."""
        state_idx = self.state_to_idx(state)

        if np.random.random() < self.epsilon:
            # Explore: random action
            return np.random.randint(self.num_actions)
        else:
            # Exploit: best action
            return np.argmax(self.q_table[state_idx])

    def update(self, state: Tuple[int, int], action: int,
               reward: float, next_state: Tuple[int, int], is_terminal: bool):
        """Q-learning update (temporal difference)."""
        state_idx = self.state_to_idx(state)
        next_state_idx = self.state_to_idx(next_state)

        current_q = self.q_table[state_idx, action]

        if is_terminal:
            target = reward
        else:
            max_next_q = np.max(self.q_table[next_state_idx])
            target = reward + self.gamma * max_next_q

        # TD update
        self.q_table[state_idx, action] += self.alpha * (target - current_q)

    def get_policy(self, grid_size: int = 4) -> np.ndarray:
        """Extract greedy policy: best action per state."""
        policy = np.argmax(self.q_table, axis=1)
        return policy.reshape((grid_size, grid_size))

# ============================================================================
# Training
# ============================================================================

def train_agent(env: GridWorld, agent: QLearningAgent,
                num_episodes: int = 500) -> List[float]:
    """Train agent and return rewards per episode."""
    rewards_per_episode = []

    for episode in range(num_episodes):
        state = env.reset()
        total_reward = 0.0
        done = False
        step_count = 0

        while not done and step_count < 100:  # Max 100 steps per episode
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)

            agent.update(state, action, reward, next_state, done)

            total_reward += reward
            state = next_state
            step_count += 1

        rewards_per_episode.append(total_reward)

        # Print progress
        if (episode + 1) % 50 == 0:
            avg_reward = np.mean(rewards_per_episode[-50:])
            print(f"Episode {episode + 1}: avg reward (last 50) = {avg_reward:.2f}")

    return rewards_per_episode

# ============================================================================
# Extract and Display Results
# ============================================================================

def extract_optimal_path(env: GridWorld, policy: np.ndarray) -> List[Tuple[int, int]]:
    """Follow the learned policy to extract the optimal path."""
    path = [env.start_pos]
    state = env.start_pos
    max_steps = 20

    action_names = ['up', 'right', 'down', 'left']

    for _ in range(max_steps):
        if state == env.goal_pos:
            break

        row, col = state
        action = policy[row, col]

        # Take step
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        drow, dcol = deltas[action]
        new_row, new_col = row + drow, col + dcol

        if env.is_valid(new_row, new_col):
            state = (new_row, new_col)

        path.append(state)

    return path

def visualize_policy(policy: np.ndarray, walls: set,
                     start: Tuple[int, int], goal: Tuple[int, int]):
    """Print grid world with learned policy."""
    grid_size = policy.shape[0]
    action_chars = ['^', '>', 'v', '<']  # up, right, down, left

    print("\nLearned Policy (greedy actions):")
    print("================================")

    for row in range(grid_size):
        line = ""
        for col in range(grid_size):
            if (row, col) in walls:
                line += "  # "
            elif (row, col) == start:
                line += "  S "
            elif (row, col) == goal:
                line += "  G "
            else:
                action = int(policy[row, col])
                line += f"  {action_chars[action]} "
        print(line)

# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("Q-Learning on 4x4 Grid World")
    print("=" * 50)

    env = GridWorld()
    agent = QLearningAgent(num_states=16, alpha=0.1, gamma=0.95, epsilon=0.1)

    print("Training for 500 episodes...")
    rewards = train_agent(env, agent, num_episodes=500)

    print(f"\nFinal episode reward: {rewards[-1]:.2f}")

    policy = agent.get_policy()
    visualize_policy(policy, env.walls, env.start_pos, env.goal_pos)

    path = extract_optimal_path(env, policy)
    print(f"\nOptimal path from start to goal:")
    print(" -> ".join(str(p) for p in path))
    print(f"Path length: {len(path) - 1} steps")
