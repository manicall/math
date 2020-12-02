from scipy import integrate
import sympy as smp
import numpy as np

print('интеграл по формуле трапеций')
a = 0.8
b = 1.4
y = '1 / sqrt(2 * x ** 2 + 3)'
#пример
a = 0.7; b = 1.3
y = '1 / sqrt(2 * x ** 2 + 0.3)'
f = smp.lambdify('x', y)
d2y = smp.diff(y, 'x', 'x')
#d2y = smp.simplify(d2y)

d2f = smp.lambdify('x', d2y)
M2 = max(np.abs(d2f(np.linspace(a,b,1000))))

#print(d2y)
#l1 = lambda x: np.sqrt(2)*(x**2 - 0.075)
#l2 = lambda x: (x**2 + 0.15)**(5/2)
#M2 = l1(b)/l2(a)

n = round(np.sqrt((b - a) ** 3 * M2 / (12 * 0.0005))) + 1
h = (b - a) / n
x = [a + i*h for i in range(n + 1)]
iy = [f(x[i]) for i in range(n + 1)]
list1 = [iy[i] for i in range(1, n)]
list1.insert(0, (iy[0] + iy[-1]) / 2)
I = h*sum(list1)

print('max:', M2)
print('n:', n)
print('h:', h)
print('Ответ:', I)
print("проверка:", integrate.quad(smp.lambdify('x', y), a, b)[0],
      '(проверку осуществляет встроенная функция python, вычисляющая интеграл)')

print()
print('интеграл по формуле Симпсона')
n = 8
a = 0.4
b = 1.2
y = 'sqrt(x)*cos(x**2)'
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

I = h / 3 * sum(list1)

delt1_y = [np.round(iy[i + 1] - iy[i], 4) for i in range(len(iy)-1)]
delt2_y = [np.round(delt1_y[i + 1] - delt1_y[i], 4) for i in range(len(delt1_y)-1)]
delt3_y = [np.round(delt2_y[i + 1] - delt2_y[i], 4) for i in range(len(delt2_y)-1)]
delt4_y = [np.round(delt3_y[i + 1] - delt3_y[i], 4) for i in range(len(delt3_y)-1)]

R = (b - a) * max(np.abs(delt4_y)) / 180
detl_I = (b - a) * max(np.abs(delt4_y))

print('остаточный член формулы:', R)
print('Погрешность вычисления:', detl_I)

print('ответ:', I)
print("проверка:", integrate.quad(smp.lambdify('x', y), a,b)[0],
      '(проверку осуществляет встроенная функция python, вычисляющая интеграл)')