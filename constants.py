# 행동 설정

from collections import namedtuple

Agent = 1
Pit = 2
Wumpus = 3
Gold = 4
Wind = 5
Stench = 6

EnvSize = 4


def getMatrix(item):
    matrix = []
    try:
        copy = getattr(item, 'copy')
    except AttributeError:
        copy = None
    for i in range(EnvSize):
        matrix.append([])
        for j in range(EnvSize):
            if copy:
                matrix[i].append(copy())
            else:
                matrix[i].append(item)

    return matrix


def getDirections(index):
    x, y = index
    Dirs = namedtuple('Dirs', 'up right down left')
    directions = Dirs(down=(x + 1, y),
                      up=(x - 1, y),
                      right=(x, y + 1),
                      left=(x, y - 1))

    return directions


def getIndexes():
    Indexes = []
    for x in range(EnvSize):
        for y in range(EnvSize):
            Indexes.append((x, y))
    return Indexes
