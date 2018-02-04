# import gym
# import universe  # register the universe environments
#
# env = gym.make('flashgames.NeonRace-v0')  # You can run many environment in parallel
# env.configure(remotes=1)  # automatically creates a local docker container
# observation_n = env.reset()  # Initiate the environment and get list of observations of its initial state
# while True:
#     action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]  # your agent here
#     observation_n, reward_n, done_n, info = env.step(action_n)  # Reinforcement Learning action by agent
#     print("observation: ", observation_n)  # Observation of the environment
#     print("reward: ", reward_n)  # If the action had any postive impact +1/-1
#     env.render()  # Run the agent on the environment

import gym
import universe  # register the universe environments
import random

env = gym.make('flashgames.NeonRace-v0')
env.configure(remotes=1)  # automatically creates a local docker container
observation_n = env.reset()

# Create variable for moving the car
goleft = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True),
          ('KeyEvent', 'ArrowRight', False)]
goright = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False),
           ('KeyEvent', 'ArrowRight', True)]

# Move the car forward with nitroboost
boostforward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowRight', False),
                ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'n', True)]

sum_reward = 0
turn = 0
rewards = []
buffer_size = 100
action = boostforward

while True:

    turn -= 1
    if turn <= 0:
        action = boostforward
        turn = 0
    # choose action based on speed
    action_n = [action for ob in observation_n]

    # perform action
    observation_n, reward_n, done_n, info = env.step(action_n)

    sum_reward += reward_n[0]

    rewards += [reward_n[0]]
    # if stuck, try going one side for some time
    if len(rewards) >= buffer_size:
        mean = sum(rewards) / len(rewards)

        if mean == 0:
            turn = 25
            if random.random() < 0.5:
                action = goleft
            else:
                action = goright

        rewards = []

    env.render()