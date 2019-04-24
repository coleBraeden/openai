import gym

env = gym.make('MountainCar-v0')
env.reset()

highestHeight = -9999;
farthestBackward = 9999
nextStep = env.action_space.sample()

for _ in range(1200):
    env.render()
    obs, reward, done, hint = env.step(nextStep)
    # obs[0] height from starting point?
    #obs[1] distance from starting point?

    #print(highestHeight)

    if(obs[0] > highestHeight):
        highestHeight = obs[0]
        nextStep = 0
    if(obs[1] < farthestBackward):
        farthestBackward = obs[1]
        nextStep = 2

env.close()
