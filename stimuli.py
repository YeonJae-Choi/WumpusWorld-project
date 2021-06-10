# 실행 코드

from environment import getEnv, getIndexes
from . import constants as C

env = getEnv()
Indexes = getIndexes()

senseMapping = SMap = {C.Pit: C.Wind,
                       C.Wumpus: C.Stench}


class Stimuli:
    def __init__(self, env):
        self.stimArr = C.getMatrix(set())

        for x, y in Indexes:
            if env[x][y] and env[x][y] != 1:
                self.addSense((x, y), env[x][y])

            if (x + 1, y) in Indexes:
                num = SMap.get(env[x + 1][y], None)
                if num:
                    self.addSense((x, y), num)

            if (x - 1, y) in Indexes:
                num = SMap.get(env[x - 1][y], None)
                if num:
                    self.addSense((x, y), num)

            if (x, y + 1) in Indexes:
                num = SMap.get(env[x][y + 1], None)
                if num:
                    self.addSense((x, y), num)

            if (x, y - 1) in Indexes:
                num = SMap.get(env[x][y - 1], None)
                if num:
                    self.addSense((x, y), num)

    def addSense(self, index, num):
        x, y = index
        self.stimArr[x][y].add(num)


if __name__ == '__main__':
    stimArr = Stimuli(env).stimArr
    print(env, end='\n\n')
    for row in stimArr:
        print(row)
