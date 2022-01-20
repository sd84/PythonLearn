import random


def create_tuple(val):
    random.seed(None, 2)
    arr = list()
    for x in range(val):
        arr.append(random.randint(0, 100))
    return arr


def show_tuple(tpl):
    for x in tpl:
        print(x, end=' ')


def optimize_tuple(arr):
    tmp = set(arr)
    return tmp
