import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(100)  # массив из 100 случайных чисел для оси x
y = np.random.rand(100)  # массив из 100 случайных чисел для оси y

# Создание диаграммы рассеяния
plt.scatter(x, y, c='blue', alpha=0.5, edgecolors='w', s=50)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')

# Отображение диаграммы
plt.show()