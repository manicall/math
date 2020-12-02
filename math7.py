from scipy import integrate
import sympy as smp
import numpy as np
'''
#a = 0.8
#b = 1.4
a = 0.7; b = 1.3
#y = '1 / sqrt(2 * x ** 2 + 3)'
y = '1 / sqrt(2 * x ** 2 + 0.3)'
d2y = smp.diff(y, 'x', 'x')
print(d2y)
f1 = lambda x: np.sqrt(2)*(3*x**2/(x**2 + 0.15) - 1) / (2*(x**2 + 0.15)**(3/2))
exp = lambda x: (8*x**2-0.6)/(2*x**2+0.3)**(5/2)
print('exp_max:', max(np.abs(exp(np.linspace(a,b,1000)))))
print('max:', max(np.abs(f1(np.linspace(a,b,1000)))))

print("проверка:",integrate.quad(smp.lambdify('x', y), a,b)[0],
      '(проверку осуществляет встроенная функция python, вычисляющая интеграл)')
'''



print('интеграл по формуле Симпсона')
n = 8
a = 0.4
b = 1.2
y = 'sqrt(x)*cos(x**2)'
#пример
#a = 1.2
#b = 1.6
#y = 'sin(2*x-2.1)/(x**2+1)'




f = smp.lambdify('x', y)

h = (b - a) / n
x = [a + i*h for i in range(n + 1)]
iy = [f(i) for i in x]

list1 = [f(x[0])]
for i in range(1, n):
    if i % 2 == 1:
        list1.append(4*f(x[i]))
    else:
        list1.append(2*f(x[i]))
list1.append(f(x[n]))

I = h/3 * sum(list1)

delt1_y = [np.round(iy[i + 1] - iy[i], 4) for i in range(len(iy)-1)]
delt2_y = [np.round(delt1_y[i + 1] - delt1_y[i], 4) for i in range(len(delt1_y)-1)]
delt3_y = [np.round(delt2_y[i + 1] - delt2_y[i], 4) for i in range(len(delt2_y)-1)]
delt4_y = [np.round(delt3_y[i + 1] - delt3_y[i], 4) for i in range(len(delt3_y)-1)]

print(delt1_y)
print(delt2_y)
print(delt3_y)
print(delt4_y)

R = (b - a) * max(np.abs(delt4_y)) / 180
detl_I = (b - a) * max(np.abs(delt4_y))

print('остаточный член формулы:', R)
print('Погрешность вычисления:', detl_I)

print('ответ:', I)
print("проверка:", integrate.quad(smp.lambdify('x', y), a,b)[0],
      '(проверку осуществляет встроенная функция python, вычисляющая интеграл)')