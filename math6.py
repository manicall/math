import numpy as np
import matplotlib.pyplot as plt

x = 0.896
ix = [0.68, 0.73, 0.80, 0.88, 0.93, 0.99]
iy = [0.80866,  0.89492, 1.02964, 1.20966, 1.34087, 1.52368]
n = len(ix)
list_of_division = []
Di = []
#print("разности:")
for i in range(n):
    list_of_difference = [ix[i] - ix[j] for j in range(n)]  # разности
    if list_of_difference[i] == 0:
        list_of_difference[i] = x - ix[i]
    Di.append(np.prod(list_of_difference))
    list_of_division.append(iy[i]/Di[i])
    #print(list_of_difference,sep='\n')  # разности

print("Di:", [str(np.round(Di[i], 10)).ljust(12, " ") for i in range(n)])
print("iy[i]/Di[i]:", [np.round(iy[i]/Di[i], 5) for i in range(n)])
F = np.prod([x - ix[i] for i in range(n)]) * sum(list_of_division)
print("F:", F)
print()
fig = plt.figure()
plt.subplot(111)
plt.plot(ix, iy)
plt.scatter(x, F, s=15, color='red')
plt.show()
#================================================================

x = 0.2121
ix = [0.210, 0.215, 0.220, 0.225, 0.230, 0.235]
iy = [4.83170, 4.72261, 4.61855, 4.51919, 4.42422, 4.33337]

n = len(ix)
h = [ix[i+1] - ix[i] for i in range(n - 1)]
h = sum(h) / len(h)
t = (x - ix[0]) / h
mult = lambda t: np.prod([t - i for i in range(n)])
Ci = [(-1) ** (n - 1 - i) * np.math.factorial(i) * np.math.factorial(n - 1 - i) for i in range(n)]
i_t = [t - i for i in range(n)]
i_tCi = [i_t[i] * Ci[i] for i in range(n)]
list_of_division = [iy[i] / i_tCi[i] for i in range(n)]
F = mult(t)*sum(list_of_division)

_list =[["Xi", "Yi", "t-i", "Ci", "(t-i)*Ci", "Yi/(t-i)*Ci"]]
for i in range(n):
    _list.append([])
    _list.append([
        str(ix[i]),
        str(iy[i]),
        str(i_t[i]),
        str(Ci[i]),
        str(i_tCi[i]),
        str(list_of_division[i])
        ])
for row in _list:
    print()
    for col in row:
        print(col.ljust(20," "), end=" ")
print()
print("F:", F)
fig = plt.figure()
plt.subplot(111)
plt.plot(ix, iy)
plt.scatter(x, F, s=15, color='red')
plt.show()

