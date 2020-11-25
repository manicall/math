import numpy as np
import matplotlib.pyplot as plt

x = 0.896
ix = [0.68, 0.73, 0.80, 0.88, 0.93, 0.99]
iy = [0.80866, 0.89492, 1.02964, 1.20966, 1.34087, 1.52368]
n = len(ix)
list_of_division = []
for i in range(n):
    list_of_difference = [ix[i] - ix[j] for j in range(n)]  # разности
    if list_of_difference[i] == 0:
        list_of_difference[i] = x - ix[i]
    Di = (np.prod(list_of_difference))
    list_of_division.append(iy[i]/Di)
    print("Di:", str(np.round(Di, 10)).ljust(12, " "), "iy[i]/Di[i]:", np.round(iy[i]/Di, 5))

print(list_of_division)

F = lambda x: np.prod([x - ix[i] for i in range(n)]) * sum(list_of_division)  #
print(F(x))

fig = plt.figure()
plt.subplot(111)
plt.plot(ix, iy)
plt.plot(np.linspace(ix[0], ix[-1], 2), [F(x) for i in range(2)])



#================================================================

x = 0.1157
ix = [0.101,
0.106,
0.111,
0.116,
0.121,
0.126]
iy = [1.26183,
1.27644,
1.29122,
1.30617,
1.32130,
1.32660]

n = len(ix)

h = [ix[i+1] - ix[i] for i in range(n - 1)]
h = sum(h) / len(h)
t = (x - ix[0]) / h
mult = lambda t: np.prod([t - i for i in range(n)])

Ci = [(-1) ** (n - 1 - i) * np.math.factorial(i) * np.math.factorial(n - 1 - i) for i in range(n)]
print(Ci)

i_tCi = [(t - i) * Ci[i] for i in range(n)]
print(i_tCi)

how_should_i_name_this_variable = [iy[i]/i_tCi[i] for i in range(n)]
print(how_should_i_name_this_variable)

F = lambda x: mult(t)*sum(how_should_i_name_this_variable)
print(F(x))


plt.show()

fig = plt.figure()
plt.subplot(111)
plt.plot(ix, iy)
plt.plot(np.linspace(ix[0], ix[-1], 2), [F(x) for i in range(2)])

plt.show()