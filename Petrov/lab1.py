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

from pirson import Pirson

    

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
    print(Pirson(x,y).get_stat())


if __name__ == '__main__':
    # main()
    rnd = random.Random()
    _x = read_file()
    _r = Pirson.find_optimal_interval(_x, start_count=len(_x)//2)
    # e = exp_range(0.01,(rnd.random()for _ in count()))
    x = np.array([rnd.random() for _ in range(100)])
    y = np.fromiter(map(lambda i: exp_f(i,1.5), x ), dtype=np.float)
    P = Pirson(_x,y, r=True)
    z = P.get_stat()
    print(z, P.range)

    # print(Pirson.get_squense_from_array(y))
    # def f_opt(z):
    #     r = Pirson.get_squense_from_array(np.fromiter(map(lambda i: exp_f(i,z), x ), dtype=np.float), interval=_r.range)
    #     p = Pirson(x, r.y, r=True, interval=r.range, disable_check_len_interval=True).get_stat()
    #     return p
    # o = opt.minimize_scalar(f_opt,bounds=(0.1,10), method='bounded')
    # print(o)

    # plt.plot(x,y,'o')
    # plt.show()
    # for _ in range(100):
    #     print(next(e))
        