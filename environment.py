# 환경 설정


import random
from . import constants as C
from . constants import getIndexes


env = C.getMatrix(0)


Indexes = getIndexes()


def setElement(index, value):

    x, y = index
    env[x][y] = value
    Indexes.remove(index)


def randomize_pits():

    pit_probability = [1, 0, 0, 0, 0]
    for index in Indexes:
        setPit = random.choice(pit_probability)
        if setPit:
            setElement(index, C.Pit)

# 웜푸스, 금 랜덤하게 위치
def setWumpus():
    index = random.choice(Indexes)
    setElement(index, C.Wumpus)


def setGold():
    index = random.choice(Indexes)
    setElement(index, C.Gold)


# 에이전트는 (0,0)에서 시작
def setAgent():
    index = (0, 0)
    setElement(index, C.Agent)


# 다시 시작
def refreshGlobals():
    global Indexes
    global env
    Indexes = getIndexes()
    env = C.getMatrix(0)


def getEnv(fair=False):
    refreshGlobals()
    if fair:
        Indexes.remove((0, 1))
        Indexes.remove((1, 0))
    setAgent()
    setGold()
    setWumpus()
    randomize_pits()
    return env


if __name__ == '__main__':
    print('Agent = 1', 'Pit = 2', 'Wumpus = 3', 'Gold = 4\n', sep='\n')
    setAgent()
    setGold()
    setWumpus()
    randomize_pits()
    print(env)
