import numpy as np
import matplotlib.pyplot as plt

x = 0.263
ix = [0.05, 0.1, 0.17, 0.25, 0.30, 0.36]
iy = [0.050042, 0.100335, 0.171657, 0.255342, 0.309336, 0.376403]
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
l = lambda x: x
plt.plot(ix, l(ix))
plt.plot(np.linspace(ix[0], ix[-1], 2), [F(x) for i in range(2)])
plt.show()


#================================================================




