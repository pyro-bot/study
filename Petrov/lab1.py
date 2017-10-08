from collections import Counter, defaultdict, namedtuple
from itertools import count
from functools import partial
from math import exp, log
import random
import os
import scipy.stats as stats
import scipy.optimize as opt
import numpy as np
from matplotlib import pyplot as plt

from criterion.x2 import X2Discrete
from criterion.exp_range import ExpRange
from optimize.evolution import EvolutionOptimize
    

class FindOptimizeInterval(EvolutionOptimize):

    def __init__(self, a, x, y):
        self.max = max(x)
        self.a = a
        self.y = y
        super().__init__()

    def megre_gen(self, a, b, i):
        if i==0:
            return self.rand.randint(100)
        else:
            return (a + b) / 2

    def min_f(self, arr):
        P = ExpRange(_x, y, 1.5, list(arr))
        z = P.get_stat()
        return z

    def create_DNA(self):
        n = self.rand.randint(100)
        buf=[0, self.max]
        for i in range(n-2):


def exp_range(a, x_gen):
    while True:
        y = exp_f(a, next(x_gen))
        yield y if y>=0 else 0

def exp_f(x, a):
    y = (-1/a)*log(x)
    # y = 1-exp(-a * x)
    return y if y>=0 else 0



def read_file():
    lines = []
    with open(os.path.join(os.path.abspath(os.curdir) , 'Petrov', 'lab1_range.txt'), mode='r', encoding='utf-8') as f:
        lines = f.readlines()
    x = []
    for line in lines:
        for s in line.split(';'):
            try:
                x.append(float(s.replace(',', '.')))
            except Exception as e:
                print(e)
    # print(Pirson(x, y, r=True, c=1))
    # print(Pirson.find_optimal_interval(x,start_count=100))
    return x


def main():
    x = [
            5,3,9,2,12,3,3,3,3,12,2,3,2,3,5,9,5,2,12,12,
            12,12,5,7,2,3,3,5,7,9,9,5,12,9,5,2,3,5,12,3,
            9,9,9,2,12,3,2,12,3,5,12,3,3,9,5,2,9,12,9,9,
            3,12,2,12,5,3,12,12,3,2,2,12,9,7,3,9,5,5,9,3,
            3,9,12,9,5,5,3,9,5,9,9,7,3,2,7,3,3,9,7,5
        ]
    y = {2:0.1, 3:0.2, 5:0.15, 7:0.05, 9:0.3, 12:0.2}
    print(X2Discrete(x,y).get_stat())


if __name__ == '__main__':
    # main()
    rnd = random.Random()
    _x = read_file()
    _r = ExpRange.find_optimal_interval(_x, start_count=len(_x))
    # e = exp_range(0.01,(rnd.random()for _ in count()))
    x = np.array([rnd.random() for _ in range(100)])
    y = np.fromiter(map(lambda i: exp_f(i,1.5), _x ), dtype=np.float)
    P = ExpRange(_x, y, 1.5, [0, 0.3, 0.6, 0.9, 1.2, 1.8, 5.7])
    z = P.get_stat()
    print(z, P.range)
