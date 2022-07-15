# Deep Q-Leaning and SARSA Algorithms on the Lunar Lander V2 Problem (OpenAI Gym)

## Abstract

This project aims to solve OpenAI’s Lunar Lander problem using reinforcement learning algorithms Sarsa algorithm and Deep Q-Learning. Their performances are compared, and several state space discretization strategies and the
effects of different ε-greedy schedules are explored. The results suggest that, while
adopting a more refined discretization strategy and ε-greedy schedule affects the
performance of SARSA agents, no visible difference in performance was found for
the Deep Q-Learning agents when modifying the ε-greedy schedule. Only the Deep
Q-Learning algorithm converged successfully, suggesting that Deep Q-Networks
are better suited for the complexity of the Lunar Lander problem’s state space.

## Files

- `play.py` allows you to control the lunar lander yourself
- `DQL.ipynb` and `SARSA.ipynd` contains the code for the deep Q-learning and SARSA approaches
- `LunarLanderReport.pdf` is the paper to this project