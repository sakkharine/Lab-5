import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


a_min = -5
a_max = 12
delta_a = 2.5
x_value = 3.567


def f(x, a):
    return np.sin(x / 3) + 1.2 * a


a_values = np.arange(a_min, a_max, delta_a)
y_values = [f(x_value, a) for a in a_values]

print("Аргументы (x):", a_values)
print("Значения функции (f(x)):", y_values)

max_value = np.max(y_values)
min_value = np.min(y_values)
mean_value = np.mean(y_values)
num_elements = len(y_values)

if num_elements % 2 == 0:
    y_values_sorted = np.sort(y_values)[::-1]
else:
    y_values_sorted = np.sort(y_values)

plt.figure(figsize=(10, 6))

plt.plot(a_values, y_values, marker='o', linestyle='-', label='f(x) = sin(x/3) + 1.2a')
plt.xlabel('Значение a')
plt.ylabel('f(x)')
plt.title('Изменение значений функции f(x)')
plt.legend()
plt.grid(True)

plt.axhline(y=mean_value, color='r', linestyle='--', label=f'Среднее ({mean_value:.2f})', linewidth=2)
plt.legend()

plt.show()

print("Наибольшее значение функции:", max_value)
print("Наименьшее значение функции:", min_value)
print("Среднее значение функции:", mean_value)
print("Количество элементов в массиве:", num_elements)
print("Отсортированный массив значений функции:", y_values_sorted)
