import gym
import win32api

env = gym.make('LunarLander-v2')

a = 0
run = True
env.reset()
while run:
    a = 0
    env.render()
    if win32api.GetAsyncKeyState(ord('Q')):
        env.reset()

    if win32api.GetAsyncKeyState(ord('W')):
        a = 2

    if win32api.GetAsyncKeyState(ord('D')):
        a = 1

    if win32api.GetAsyncKeyState(ord('A')):
        a = 3

    env.step(a)

env.close()
