# Action


from . environment import getEnv, getIndexes

Indexes = getIndexes()


def Solvable(env, x=0, y=0, Indexes=Indexes):

    Indexes.remove((x, y))

    # Base Step
    badVals = [2, 3]
    if env[x][y] in badVals:
        return False, (0, 0)
    elif env[x][y] == 4:
        return True, (x, y)

    # Go UP
    if (x, y + 1) in Indexes:
        found, index = Solvable(env, x, y + 1, Indexes=Indexes)
        if found: return (found, index)

    # Go Right
    if (x + 1, y) in Indexes:
        found, index = Solvable(env, x + 1, y, Indexes=Indexes)
        if found: return (found, index)

    # Go Down
    if (x, y - 1) in Indexes:
        found, index = Solvable(env, x, y - 1, Indexes=Indexes)
        if found: return (found, index)
        
    # Go Left
    if (x - 1, y) in Indexes:
        found, index = Solvable(env, x - 1, y, Indexes=Indexes)
        if found: return (found, index)

    return False, (0, 0)


if __name__ == '__main__':
    env = getEnv()
    print(env)
    print()
    print(Solvable(env))
