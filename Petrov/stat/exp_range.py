from . import x2
from collections import defaultdict

class ExpRange(x2.X2Float):
    def __init__(self, x, y, interval=None, c=None, low=6, disable_check_len_interval=False):
        super().__init__(x,y,interval,c,low,disable_check_len_interval)
        self.y = defaultdict(float)
        for k, v in self.range.y.items():
            pass
