'''Уровень 2
26. В двух заданных матрицах одинакового размером поменять строки, содержащие максимальное количество отрицательных эле- ментов. Нахождение количества отрицательных элементов заданной строки матрицы осуществлять в методе. Определение номера стро- ки, содержащей максимальное количество отрицательных элементов,
осуществлять в методе.'''
from random import *

a1 = [[randint(-10, 10) for i in range(5)] for i in range(5)]
a2 = [[randint(-10, 10) for i in range(5)] for i in range(5)]

def otr(x):
    s = -10**20
    l = 0
    for i in range(len(x)):
        k = 0
        for j in range(len(x[i])):
            if x[i][j] < 0:
                k += 1
        if k > s:
            s = k
            l = i
    return l
for i in range(len(a1)):
    print(a1[i])
print('----------')
s = a1[otr(a1)]
a1[otr(a1)] = a2[otr(a2)]
for i in range(len(a1)):
    print(a1[i])
print('===========')
for i in range(len(a2)):
    print(a2[i])
print('----------')
a2[otr(a2)] = s
for i in range(len(a2)):
    print(a2[i])
print('Программа выводит сначала первый массив, потом его измененную версию, после второй массив и его измененную версию')

