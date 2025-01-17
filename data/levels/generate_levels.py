import random


for c in range(100):
    level = [[None for _ in range(11)] for _ in range(11)]

    data = ['.', '#']

    for x in range(11):
        for y in range(11):
            level[x][y] = random.choice(data)

    level[4][4] = '@'

    with open(str(c) + '.txt', 'w') as f:
        for i in level:
            f.write(''.join(i) + '\n')