from math import exp
# import stat.x2 as x2
from stat.x2 import X2Float
from collections import defaultdict

class ExpRange(X2Float):
    def __init__(self, x, y, a, interval=None, c=None, low=6):
        super().__init__(x,y,interval,c,low)
        self.y = defaultdict(float)
        self.range.range.remove(self.range.range[0])
        self.range.range.insert[0,0.0]
        self.range.range.remove(self.range.range[-1])
        _range = self.range.range
        for i in range(len(self.range.range)):
            y[i] = exp(-a + _range[i]) - exp(-a + _range[i+1])
        self.y = y


            

        
