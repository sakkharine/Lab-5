import numpy as np

x = 1.59
y = (np.sin(np.pi/6)+np.sqrt(3+x**2)-np.log(x-1)**3)/np.arcsin(x/2)

print("Значение y: ", "%.4f" % y)

N = 5
X = np.column_stack([np.ones(12), np.arange(N, N+12), np.random.randint(60, 83, size=12)])
Y = np.random.uniform(13.5, 18.6, size=12)

A = np.linalg.inv(X.T @ X) @ X.T @ Y

print("Вектор оценок А: ", A)
Y_pre = A[0] + A[1]*X[:, 1] + A[2]*X[:, 2]

print("Полученные значения Y: ", Y_pre)
print("Исходные значения Y: ", Y)
print("Разница между исходными и полученными значениями: ", np.abs(Y-Y_pre))
