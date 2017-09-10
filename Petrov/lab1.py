from collections import Counter, defaultdict, namedtuple
from functools import partial
import random
import os
import scipy.stats as stats
import numpy as np

class Pirson(object):
    
    def __init__(self, x, y, r=False, c=None, low=5):
        self.rnd = random.Random()
        if not r:
            self.count = Counter(x)
        else:
            self.count = Pirson.find_optimal_interval(x, c or len(x)//10, low)
        self.l = len(x)
        self.y = y

    @staticmethod
    def find_optimal_interval(x, start_count=20, low=5):
        get_interval = partial(Pirson.transform_range_to_array, x=x, disable_check_len_interval=True, get_interval=True)
        start_r = get_interval(c=start_count)
        r = start_r
        while list(filter(lambda item: item[1] < low, r.y.items())):
            next_r = r.range[:]
            for i in range(len(r.range)):
                if r.y[i] < low:
                    try:
                        if (r.y[i-1] + r.y[i]) >= (r.y[i] + r.y[i+1]):
                            next_r.remove(r.range[i])
                        else:
                            next_r.remove(r.range[i+1])
                    except Exception as e:
                        print(e)
            r = get_interval(set_range=next_r)
        return r
                    
            

    @staticmethod
    def transform_range_to_array(x, c=None, set_range=None, disable_check_len_interval=False, get_interval=False):
        x = sorted(x[:])
        y = defaultdict(int)
        if not set_range:
            walk = max(x) / c
            r = [min(x)] + [walk*(i+1) for i in range(c-1)]
        else:
            c = len(set_range)
            r = set_range
        for num, i in enumerate(reversed(r)):
            while x:
                mx = max(x)
                if i <= mx:
                    y[c-1-num]+=1
                    x.remove(mx)
                else:
                    break
        if not disable_check_len_interval:
            if y and min(y.items(), key=lambda k: k[1])[1] < 5:
                raise Exception('Мало значений попало в интервал')
        if not get_interval:
            return y
        else:
            return namedtuple('TransformRangeToArray', ['y', 'range'])(y=y, range=r)


    def get_stat(self):
        n = self.count
        l = self.l
        p = self.y
       
        X = sum(((n[i] - l*pi)**2) / (l * pi) for i, pi in p.items())
        
        return X


rnd = random.Random().random

def irnd (*args, **kwargs):
    while True:
        yield rnd()
    


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
    print(Pirson.find_optimal_interval(x))

if __name__ == '__main__':
    main()
