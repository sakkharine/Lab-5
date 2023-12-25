import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

df = pd.read_csv('test.csv', sep=",")
df = df.sample(n=1000, replace=False)

missing_values = df.isnull().sum()
print("Пропуски в данных:")
print(missing_values)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
df.boxplot(column='Rooms', by='DistrictId', ax=axes[0])
axes[0].set_yscale('log')
df['Rooms'].plot(kind='hist', ax=axes[1])
axes[0].set_title('Логарифмическая шкала')
axes[1].set_title('Гистограмма')
plt.show()

df['Rooms'].fillna(df['Rooms'].mean(), inplace=True)

room_counts = df['Rooms'].value_counts()
print("Количество комнат в выборке:")
print(room_counts)

pivot_table = df.pivot_table(index='DistrictId', columns='Rooms', aggfunc='size', fill_value=0)
print("Сводная таблица:")
print(pivot_table)

df.to_csv('surname.csv', sep=",", index=False)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['DistrictId'], df['Rooms'], df['Id'])
ax.set_xlabel('DistrictId')
ax.set_ylabel('Rooms')
ax.set_zlabel('Id')
ax.set_title('3D визуализация данных')

plt.show()
