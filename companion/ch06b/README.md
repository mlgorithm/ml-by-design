# Chapter 11 Companion: Learning from Interaction: Reinforcement Learning (`ch06b`)

This chapter supports learning from interaction through reinforcement learning.

It focuses on five ideas:

- Markov decision processes and value functions
- tabular Q-learning and temporal difference updates
- exploration-exploitation tradeoffs and epsilon-greedy strategies
- the importance of reward specification and alignment
- connecting RL to human feedback through RLHF concepts

## Minimal example

`minimal/q_learning_gridworld.py`

What it shows:

- a 4x4 grid world with walls and a goal state
- tabular Q-learning with epsilon-greedy exploration
- training over 500 episodes and visualizing the learned policy
- extracting and displaying the optimal path from start to goal

Run it with:

```bash
python3 companion/ch06b/minimal/q_learning_gridworld.py
```

What to notice:

- Q-values converge toward discounted return, balancing the `-1` step cost against the `+10` goal reward
- the learned policy (greedy action per state) forms a coherent path
- the training curve shows steady improvement and convergence
- the agent discovers the path despite the walls blocking the naive route

Prerequisites:

- Markov decision processes and state-action-reward dynamics
- value functions and Bellman equations
- discount factors and cumulative rewards
- the Q-learning update rule

Pre-lab primer:

- If the Q-learning update was treated as optional in lecture, spend ten minutes on one hand update before running the gridworld. For current value `Q(s,a)`, reward `r`, discount `gamma`, best next value `max Q(s',a')`, and learning rate `alpha`, compute `target = r + gamma * max Q(s',a')`, then update `Q(s,a) <- Q(s,a) + alpha * (target - Q(s,a))`.

## Practical example

`practical/rl_exploration_lab.ipynb`

What it shows:

- a grid world environment built from scratch (no gym dependency)
- Q-learning agent training and the effect of the learning curve
- comparing exploration strategies: fixed epsilon vs. decaying epsilon
- reward misspecification: how a bad proxy reward distorts learned behavior
- policy evaluation: computing state value functions under different discount factors

Run it with:

```bash
jupyter notebook companion/ch06b/practical/rl_exploration_lab.ipynb
```

What to notice:

- higher exploration (larger epsilon) helps initially but hurts long-term performance
- decaying epsilon balances exploration and exploitation better
- reward misspecification causes the agent to pursue unintended objectives
- discount factor gamma changes how much future rewards matter—low gamma myopic, high gamma far-sighted
- policy evaluation reveals the true value of a fixed policy under different planning horizons

Prerequisites:

- MDPs and the Bellman equation
- temporal difference learning and Q-learning
- reward functions and their alignment with actual objectives
- policy evaluation under a fixed policy
