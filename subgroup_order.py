import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

name_weight = {'Max': 3,
               'Ryan': 3,
               'Kevin': 3,
               'Jesse': 3,
               'Luke': 3,
               'John': 3,
               'Carl': 3,
               'Andrew': 3,
               'Ashley': 2,
               'Arnaldo': 2,
               'Minseung': 2,
               'Ilana': 2,
               'Alex': 2,
               'Avery': 1,
               'Michelle': 1,
               'Sharon': 1}

names = list(name_weight.keys())
weights = list(name_weight.values())

presenters = []
for n_ind, name in enumerate(names):
    for x in range(weights[n_ind]):
        presenters.append(name)

refractory = 3 # minimum cycles to skip before going again

order = []
while len(presenters) > 0:
    previous = order[-refractory:]
    new_ind = np.random.choice(range(len(presenters)))
    new_draw = presenters[new_ind]
    while new_draw in previous:
        new_ind = np.random.choice(range(len(presenters)))
        new_draw = presenters[new_ind]

    presenters.pop(new_ind)
    # print(presenters)
    order.append(new_draw)


print('Check is {}'.format(weights == [order.count(x) for x in names]))

order
