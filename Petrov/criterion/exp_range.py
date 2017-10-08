from math import exp
# import stat.x2 as x2
from criterion.x2 import X2Float
from collections import defaultdict

class ExpRange(X2Float):
    def __init__(self, x, y, a, interval=None, c=None, low=6):
        super().__init__(x,y,interval,c,low)
        self.y = defaultdict(float)
        # self.range.range.remove(self.range.range[0])
        # self.range.range.insert(0,0.0)
        # self.range.range.remove(self.range.range[-1])
        _range = self.range.range
        for i, v in enumerate(_range[:-1]):#range(len(self.range.range)):
            self.y[i] = exp(-a * v) - exp(-a * _range[i+1])
        self.count = ExpRange.transform_range_to_array(x, set_range=_range)
        # self.y = y


            

        
