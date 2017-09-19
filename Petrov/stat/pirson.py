import abc

class Pirson(object):
    
    def __init__(self, x, y, r=False, interval=None, c=None, low=6, disable_check_len_interval=False):
        self.rnd = random.Random()
        if not r:
            self.count = Counter(x)
        elif isinstance(interval, list):
            self.count = Pirson.transform_range_to_array(x, set_range=interval, disable_check_len_interval=disable_check_len_interval)
        else:
            z = x if len(x)<=len(y) else y
            self.range = Pirson.find_optimal_interval(z, c or len(z)//2, low)
            self.count = self.range.y
        if isinstance(y, dict):
            self.y = y
            self.l = len(x)
        else:
            self.l = len(y)
            self.y = Pirson.get_squense_from_array(y, interval=self.range)

    

    @abc.abstractmethod
    def get_stat(self):
        pass