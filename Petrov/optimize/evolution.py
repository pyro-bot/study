import abc
import math
import random
from collections import defaultdict


class RateOptimize(object):

    @staticmethod
    def fPopulate_t(): return {
        'vec': dict([(i, 0) for i in range(1, 6)]),
        'f': 0
    }

    @abc.abstractmethod
    def merge_gen(self, a, b, i):
        pass

    def __init__(self, find_number, e, max_n, len=5, mutation=0.05, len_new_population=5):
        # self.arr = arr
        self.find_number = find_number
        self.e = e
        self.max_n = max_n
        self.len = len
        self.len_new_population = len_new_population
        self.mutation = mutation * 100
        self.rand = random.Random()
        # self.group_arr = self.group_by(self.arr)

    def min_f(self, arr):
        sum = 0
        l = 0
        for k, v in arr.items():
            sum += k * v
            l += v
        return float(sum) / float(l)

    @abc.abstractmethod
    def create_DNA(self):
        pass

    @abc.abstractmethod
    def mutation_gen(self):
        pass

    def initPopulation(self):
        population = []
        # group_arr = self.group_arr
        for n in range(self.len * 5):
            buf = self.create_DNA()
            population.append(buf)
        return population

    def group_by(self, arr):
        group = defaultdict(lambda: 0)
        for a in arr:
            group[a] += 1
        return group

    def merge(self, a, b):
        res = dict(RateOptimize.fPopulate_t())
        for i, v in self.group_arr.items():
            if v == 0:
                continue
            if self.rand.randint(0, 100) < self.mutation:
                res['vec'][i] = self.mutation_gen()
            else:
                # 50%
                res['vec'][i] = self.merge_gen(a['vec'][i], b['vec'[i]], i)

        res['f'] = abs(self.min_f(res['vec']) - self.find_number)
        if res['f'] < a['f'] and res['f'] < b['f']:
            return res
        elif a['f'] < b['f']:
            return a
        else:
            return b

    def find(self):
        population = self.initPopulation()
        new_population = []
        for n in range(self.max_n):
            for item in population:
                if item['f'] <= self.e:
                    return item['vec']
                new_population.append(item)
            new_population = sorted(new_population, key=lambda x: x['f'])
            population = []
            l = min(len(new_population), self.len_new_population)
            for i in range(l):
                for j in range(l):
                    if i != j:
                        population.append(self.merge(
                            new_population[i], new_population[j]))
                        population.append(self.merge(
                            new_population[i], new_population[j]))
        return new_population[0]['vec']


class EvolutionOptimize(RateOptimize):

    @abc.abstractmethod
    def min_f(arr):
        pass

def main():
    opt = RateOptimize(
        [1, 1, 1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5],
        4.4,
        0.1,
        100
    )
    out = opt.find()
    print([out, opt.min_f(out)])


if __name__ == '__main__':
    main()
