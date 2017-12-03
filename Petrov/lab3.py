import matplotlib.pyplot as plt
import numpy as np
import random
import sympy as sp

sp.init_printing(use_unicode=True, wrap_line=False, no_global=True)
print('Задача 1. Моделирование непрерывной случайной величины с помощью обратной функции.')
print('Дана плотность распределения')
print(' ')

rnd = random.Random('123')
rand = rnd.random

# Строим график плотности распределения
# шаг
step_x = 0.001
step_y = 0.0001
# Количество реализаций
num = 50
a = 3.0
b = 6.0
#  Задаём  интервала по x
x1 = np.linspace(-10, 3) #-10 : step_x : 3
x1_2 = np.zeros(num)
x1_2[:] = 3.0
x2 = np.linspace(a, b)  #3 : step_x : 6
x2_3 = np.zeros(num)
x2_3[:] = 6.0
x3 = np.linspace(6, 15) #6 : step_x : 15
x1_2
#  Считаем значения функций на всех интервалах
y1 = np.zeros(num)
y1[:] = 0.0
y1_2 = np.linspace(0, (1 / 63) * (x1_2[0]**2))#0:step_y:(1/63)*x1_2.^2
y2 = np.zeros(num)
y2[:] = (1/63) * (x2**2)
y2_3 = np.linspace(0, (1 / 63) * (x2_3[0]**2)) #0:step_y:(1/63)*x2_3.^2
y3 = np.zeros(num) 
#
plt.figure(1)
plt.plot(x1, y1,'k-')
plt.plot(x1_2, y1_2,'k-')
plt.plot(x2, y2,'k-')
plt.plot(x2_3, y2_3,'k-')
plt.plot(x3, y3,'k-')

plt.ylabel('f_ksi(x)')
plt.xlabel('x')
plt.hold(False)
plt.grid(True)
#  # hold off
#  # grid on
 
x = sp.Symbol('x')

F_x = sp.integrate((1/63) * (x**2), (x, 3, x))
print('F_x = {0}'.format(F_x))

# syms x, F_x = int((1/63)*x^2,3,x)
# print('F_x =')
# pretty(F_x)

print('-------------------------- ')
# Строим график функции распределения
# шаг
step_x = 0.001
step_y = 0.0001
#  Задаём  интервала по x
x1 = np.linspace(-10, 3) #-10: step_x : 3
x2 = np.linspace(3, 6) #3 : step_x : 6
x3 = np.linspace(6, 15) #6: step_x : 15
 
#  Считаем значения функций на всех интервалах
y1 = np.zeros(x1.shape)
y2 = np.zeros(x2.shape)
y2[:] = (1/189) * (x2**3-27)
y3 = np.ones(x3.shape) 

fig = plt.figure(0)
#  # hold on
lin1F = plt.plot(x1, y1,'R')
lin2F = plt.plot(x2, y2,'R')
lin3F = plt.plot(x3, y3,'R')

plt.ylabel('F_ksi(x)')
plt.xlabel('x')
#  # hold off
#  # grid on
 
print('-------------------------- ')
# Количество реализаций
print('Количество реализаций n:')
n1 = 100
print(n1)

#  # Массив псевдослучайных чисел
print('Массив псевдослучайных чисел альфа:')
genalpha1 = np.random.uniform(size=100) # rand(100,1)
print(genalpha1)

# Получим n-реализаций случайной величины кси с помощью моделирующей
# Массив n-реализаций случайной величины кси A
print('Массив n-реализаций случайной величины кси A:')
A1 = (189 * genalpha1 + 27) ** (1/3) 
# for ncount=1:n1
#     A1(ncount) = double((189*genalpha1(ncount)+27)^(1/3))
# end
print(A1)

print('-------------------------- ')
print('Задача 2. Моделирование непрерывной случайной величины с кусочно-линейной плотностью.')
print('Дана плотность распределения.')
print(' ')
# Строим график плотности распределения
# шаг
step_x = 0.001
step_y = 0.0001
#  Задаём  интервала по x
x1 = range(-2, 0, step_x) #-2 : step_x : 0
x1_2 = 0
x2 = range(0, 3, step_x) #0 : step_x : 3
x2_3 = 3
x3 = range(3, 4, step_x) #3 : step_x : 4
x3_4 = 4
x4 = range(4, 7, step_x) #4 : step_x : 7
x4_5 = 7
x5 = range(7, 8, step_X) #7 : step_x : 8
x5_6 = 8
x6 = range(8, 10, step_x) #8 : step_x : 10

#  Считаем значения функций на всех интервалах
y1 = 0
y1_2 = range(0, 0.15, step_y)#0:step_y:0.15
y2 = 0.15
y2_3 = range(0.1, -0.1*x3 + 0.45, step_y) #0.1:step_y:-0.1*x3 + 0.45
y3 = -0.1*x3 + 0.45 
y3_4 = range(-0.1*x3 + 0.45, ((1/30)*3) - (1/12), step_y) #-0.1*x3 + 0.45:step_y:((1/30)*3) - (1/12)
y4 = ((1/30)*x4) - (1/12)
y4_5 = range(((1/30)*x4) - (1/12), 0.15, step_y)#((1/30)*x4) - (1/12):step_y:0.15
y5 = 0.15
y5_6 = range(0, 0.15, step_y)#0:step_y:0.15
y6 = 0

plt.figure(3)
# hold on
lin1f = plt.plot(x1, y1,'R')
lin1_2f = plt.plot(x1_2, y1_2,'R')
lin2f = plt.plot(x2, y2,'R')
lin3f = plt.plot(x3, y3,'R')
lin4f = plt.plot(x4, y4,'R')
lin5f = plt.plot(x5, y5,'R')
lin5_6f = plt.plot(x5_6, y5_6,'R')
lin6f = plt.plot(x6, y6,'R')

ylabel('f_ksi(x)')
xlabel('x')
# hold off
# grid on

# Поиск площадей фигур
x = [0, 3, 4, 7, 8]
y = [0, 0.15, 0.05, 0.15, 0]

print('Массив S')
S = np.zeros(1,4)


S[1] = (x[2]-x[1])*y[2]

S[2] = (x[3]-x[2])*((y[2]+y[3])/2)

S[3] = (x[4]-x[3])*((y[3]+y[4])/2)

S[4] = (x[5]-x[4])*y[4]

print(S)

S_sum = S(1) + S(2) + S(3) + S(4)
 
# Количество реализаций
print('Количество реализаций n:')
n2 = 100
print(n2)

#  # Массив псевдослучайных чисел
print('Массив псевдослучайных чисел альфа:')
genalpha2 = rand(100,1)
# print(genalpha2)
 

#  # Массив n-реализаций случайной величины кси A
print('Массив n-реализаций случайной величины кси A:')
A2 = []
for ncount in range(n2):#ncount=1:n2
    alhpa = genalpha2[ncount]
    if(alhpa <= 0.45):
        A2.append(alhpa / 0.15)

    if(alhpa > 0.45 and alhpa <= 0.55):
        A2.append(4.5 - sqrt(11.25-20*alhpa))


    if(alhpa > 0.55 and alhpa <= 0.85):
        A2.append(2.5 + sqrt(-30.75+60*alhpa))


    if(alhpa > 0.85):
        A2.append((4/3) + (alhpa / 0.15))

print(A2)

print('---------------------------------')
print('Задача 3. Моделирование трехмерного нормального вектора.')
print(' ')

# Количество реализаций
print('Количество реализаций n:')
n2 = 100
print(n2)

print('Вектор математических ожиданий a.')
a = [2, 0, 1]
print(a)


print(' ')
print('Ковариационная матрица C.')
C = [16, 2, 3,
     2, 6, 4,
     3, 4, 9]
print(C)

print(' ')
# создадим матрицу, заполненую нулями.
B = np.zeros(3,3)

B[0,0] = sqrt(C[0,0])

B[0,1] = C[0,0] / B[0,0]

B[1,1] = np.sqrt(C[1,1] - B[0,1]**2)

B[0,2] = C[0,2]/B[0,0]

B[1,2] = (C[1,2] - B[0,1] * B[0,2]) / B[1,1]

B[2,2] = np.sqrt(C[2,2] - (B[0,2]**2)-(B[1,2]**2))

print('Верхнетреугольная матрица B.')
print(B)

print(' ')
print('Найдем ksi.')

#  # Массив псевдослучайных чисел
# print('Массив псевдослучайных чисел альфа1:')
alpha1 = rand(100)
# print(alpha1)

# print('Массив псевдослучайных чисел альфа1:')
alpha2 = rand(100)
# print(alpha2)

# print('Массив псевдослучайных чисел альфа1:')
alpha3 = rand(100)
# print(alpha3)
n2 = 100

omega = np.zeros((n2, 3), dtype=float)

for i in range(n2):#i=1:n2
    omega[i,1] = 1-2*alpha1[i]
    gamma1 = 1-2*alpha2[i]
    gamma2 = 1-2*alpha3[i]
    D = (gamma1**2) + (gamma2**2)
    omega[i,2] = gamma1 * np.sqrt((1-omega[i,1]**2) / D)
    omega[i,3] = gamma2 * np.sqrt((1-omega[i,1]**2) / D)
    
    cnt = 1
    for j in range(3):  #j=1:3
        ksi[i,j] = omega[i,j]*B[j,cnt]+a[cnt]
        cnt = cnt+1
     
print(' ')
print('N-реализаций вектора ksi')
print(ksi)

