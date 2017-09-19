import pirson
from functools import partial
from collections import Counter, defaultdict, namedtuple
import random

class X2Discrete (pirson.Pirson):
    def __init__(self, x, y):
        self.rnd = random.Random()
        self.count = Counter(x)
        self.l = len(x)
        self.y = y

    def get_stat(self):
        n = self.count
        l = self.l
        p = self.y
       
        X = sum(((n[i] - l*pi)**2) / (l * pi) for i, pi in p.items())
        
        return X

class X2Float(pirson.Pirson):
    def __init__(self, x, y, interval=None, c=None, low=6, disable_check_len_interval=False):
        if isinstance(interval, list):
            self.count = X2Float.transform_range_to_array(x, set_range=interval, disable_check_len_interval=disable_check_len_interval)
        else:
            z = x if len(x)<=len(y) else y
            self.range = X2Float.find_optimal_interval(z, c or len(z)//2, low)
            self.count = self.range.y
        if isinstance(y, dict):
            self.y = y
            self.l = len(x)
        else:
            self.l = len(y)
            self.y = X2Float.get_squense_from_array(y, interval=self.range)

    @staticmethod
    def find_optimal_interval(x, start_count=20, low=5):
        get_interval = partial(X2Float.transform_range_to_array, x=x, disable_check_len_interval=True, get_interval=True)
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
    def get_squense_from_array(y, interval=None):
        if not interval:
            r = X2Float.find_optimal_interval(y,start_count=len(y)//2).y
        else:
            r = interval.y.copy()
        sequnse = r
        l = len(y)
        for k,v in sequnse.items():
            sequnse[k]/=l
        return sequnse



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
        if x:
            y[-1] = len(x)
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