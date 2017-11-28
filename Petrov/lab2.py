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
from criterion.test_h import test as test_h
from math import factorial, exp
from itertools import groupby
rnd = random.Random()
rand = rnd.random

# Задаём уровень значимости альфа
print('Уровень значимости alpha:')
alpha = 0.05     
print(alpha)

print('Задача 1. Моделирование дискретной случайной величины с конечным числом значений')
print('Случай 1. Дан ряд распределения')

# Количество реализаций
print('Количество реализаций n:')
n1 = 100
print(n1)

# Значения дискретной случайной величины
print('Значения дискретной случайной величины ksi:')
ksi1 = [-8, -5, -1, 0, 3, 7]
print(ksi1)

#  теоретические вероятности
print('Теоритические вероятности P:')
P1 = [0.2, 0.2, 0.1, 0.2, 0.1, 0.2] 
print(P1)

# Массив псевдослучайных чисел
print('Массив псевдослучайных чисел альфа:')
genalpha1 = np.random.uniform(size=100)
print(genalpha1)

# количество частей отрезка (01)
print('Количество частей k:')
k1 = 6
print(k1)


# Точки для разбития отрезка (01)
U1=[0]
for kcount in range(k1):
    U1.append(P1[kcount] + U1[kcount])

print('U1:')
print(U1)

# Получим n-реализаций случайной величины кси с помощью моделирующей формулы
# Массив n-реализаций случайной величины кси A
print('Массив n-реализаций случайной величины кси A:')
A1 = []
for ncount in range(n1):
    if(genalpha1[ncount] <= U1[1]):
        A1.append(ksi1[0])
    elif (genalpha1[ncount] > U1[1] and genalpha1[ncount] <= U1[2]):
        A1.append(ksi1[1])
    elif (genalpha1[ncount] > U1[2] and genalpha1[ncount] <= U1[3]):
        A1.append(ksi1[2])
    elif (genalpha1[ncount] > U1[3] and  genalpha1[ncount] <= U1[4]):
        A1.append(ksi1[3])
    elif (genalpha1[ncount] > U1[4] and genalpha1[ncount] <= U1[5]):
        A1.append(ksi1[4])
    elif (genalpha1[ncount] > U1[5] and genalpha1[ncount] <= U1[6]):
        A1.append(ksi1[5])    


print(A1)

print('Применив критерий Пирсона хи-квадрат проверим, действительно ли эти реализации взяты из заданной величины кси на уровне значимости 0,05')
y = dict([(ksi1[i], P1[i]) for i in range(len(ksi1))])
task_1 = X2Discrete(A1, y).get_stat()
print('Проверка гипотезы H0:', test_h(task_1, alpha, k1 - 1))
# Pirson_1(A1, n1, alpha, k1, ksi1, P1)

print('------------------------------------------------------------------------------------------------------------------------------')

print('Случай 2. Дана функция распределения')

# Количество реализаций
print('Количество реализаций n:')
n2 = 1000
print(n2)


# Значения дискретной случайной величины
print('Значения дискретной случайной величины ksi:')
ksi2 = [-8, -5, 0, 3, 7]
print(ksi2)

#  теоретические вероятности
print('Теоритические вероятности P:')
P2 = [0.11, 0.21, 0.27, 0.36, 0.05] 
print(P2)

# Массив псевдослучайных чисел
print('Массив псевдослучайных чисел альфа:')
genalpha2 = np.random.uniform(size=n2)
print(genalpha2)
plt.hist(genalpha2)
plt.show()
# количество частей отрезка (01)
print('Количество частей k:')
k2 = 5
print(k2)

# Точки для разбития отрезка (01)
U2=[0]
for kcount in range(k2 - 1):
    U2.append(P2[kcount] + U2[kcount])

print('U2:', U2)
print(sum(U2))

# Получим n-реализаций случайной величины кси с помощью моделирующей формулы
# Массив n-реализаций случайной величины кси A
print('Массив n-реализаций случайной величины кси A:')
A2 = []
U2ksi2 = dict([(U2[i], ksi2[i]) for i in range(len(U2))])
print(U2ksi2)
for num in genalpha2:
    mx = max(filter(lambda a:num >= a, U2))
    A2.append(U2ksi2[mx])
    # if(genalpha2[ncount] <= U2[2]):
    #     A2.append(ksi2[0])
    # elif (genalpha2[ncount] > U2[2] and genalpha2[ncount] <= U2[3]):
    #     A2.append(ksi2[1])
    # elif (genalpha2[ncount] > U2[3] and genalpha2[ncount] <= U2[4]):
    #     A2.append(ksi2[2])
    # elif (genalpha2[ncount] > U2[4] and genalpha2[ncount] <= U2[5]):
    #     A2.append(ksi2[3])  
    # elif (genalpha2[ncount] > U2[5] and genalpha2[ncount] <= U2[6]):
    #     A2.append(ksi2[4])


print(A2)


print('Применив критерий Пирсона хи-квадрат проверим, действительно ли эти реализации взяты из заданной величины кси на уровне значимости 0,05')
y = dict([(ksi2[i], P2[i]) for i in range(len(ksi2))])
x2 = X2Discrete(A2, y)
task_2 = x2.get_stat()
print('Проверка гипотезы H0:', test_h(task_2, alpha, k2 - 1))
print('------------------------------------------------------------------------')

print('Случай3. Биномиальное распределение')

# Количество реализаций
print('Количество реализаций n:')
n3 = 100
print(n3)

# Параметр n
print('Параметр n:')
n = 8
print(n)

# Параметр p
print('Параметр p:')
p = 0.63
print(p)

# Смоделируем опыт, состоящий из n = 8 независимых испытаний и подсчитаем число испытаний, 
# в которых произошло событие А в данной серии. 
print('Массив n-испытаний случайной величины кси A:')
X = []
A3 = []
for _ in range(n3):
    B=0
    for _ in range(n):
        genalpha3 = rand()
        if genalpha3 < p:
            X.append(1)
            B = B + 1
        else:
            X.append(0)  
    print(X)
    A3.append(B)
print(A3)

# print('Применив критерий Пирсона хи-квадрат проверим, действительно ли эти реализации взяты из заданной величины кси на уровне значимости 0,05')

# function [result] = Pearson_2(A, n, alpha, int, p)

ver = p
k = n
# Формируем значения дискретной случайной величины
N = list(range(k))
nk = len(N)
print(nk)

# Теоретические вероятности
P = [0]
for i in range(1,nk):
    P.append((factorial(nk) / ((factorial(nk-i)) * factorial(i))) * (ver**i) * (1-p)**(nk-i))
P
y = dict([(N[i], P[i]) for i in range(1,len(N))])
q = X2Discrete(A3,y).get_stat()
print('Проверка критерия Пирсона %s' % test_h(q, alpha, n-1))
# Pearson_2(A3, n3, alpha, n, p)

print('------------------------------------------------------------------------')

print('Задача 2. Моделирование дискретной случайной величины с бесконечным числом значений')
print('Случай 1. Распределение Пуассона')

# Количество реализаций
print('Количество реализаций n:')
n4 = 100
print(n4)

# Параметр p
print('Параметр _lambda:')
_lambda = 2.5
print(_lambda)


print('Массив n-реализаций случайной величины кси A:')
A4 = np.random.poisson(_lambda, n4) 
print(A4)

print('Применив критерий Пирсона хи-квадрат проверим, действительно ли эти реализации взяты из заданной величины кси на уровне значимости 0,05')
I = list((k for k,_ in groupby(sorted(A4))))
I
# Для формулы считаем экспоненту в степени -лямда
expInAlpha = exp(-_lambda)

k = len(I)

# Теоретические вероятности
P = []
for i in range(k):
    P.append(((_lambda**i) / factorial(i)) * expInAlpha)
print(P, sum(P), sep='\r\n')
y = dict([(I[i], P[i]) for i in range(k)])
x2 = X2Discrete(A4, y).get_stat()
print('Проверка критерия Пирсона %s' % test_h(x2, alpha, k-1))
# Pearson_3(A4, n4, alpha, _lambda)

print('------------------------------------------------------------------------')

print('Случай 2. Геометрическое распределение')

# Количество реализаций
print('Количество реализаций n:')
n5 = 100
print(n5)

# Параметр p
print('Параметр p_geom:')
p_geom = 0.37
print(p_geom)

print('Массив n-реализаций случайной величины кси A:')
A5 = np.random.geometric(p_geom, n5)
 
print(A5)

print('Применив критерий Пирсона хи-квадрат проверим, действительно ли эти реализации взяты из заданной величины кси на уровне значимости 0,05')
# Pearson_4(A5, n5, alpha, p_geom)

# Формируем значения дискретной случайной величины из массива, выбирая
# уникальные значения
I = [k for k,_ in groupby(sorted(A5))]
I
# Для формулы считаем экспоненту в степени -лямда

k = len(I)

# Теоретические вероятности
P = []
for j in range(1,k+1):
   P.append(p_geom * ((1 - p_geom)**(j-1)))
print('\r\n'.join((str(i) for i in P)), sep='\r\n')
print('\r\n',sum(P))

y = dict([(I[i], P[i]) for i in range(k)])
x2 = X2Discrete(A5, y).get_stat()
print('Проверка критерия Пирсона %s' % test_h(x2, alpha, k-1))
