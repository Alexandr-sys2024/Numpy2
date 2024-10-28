import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Данные об оценках студентов
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'John', 'Jack', 'Barbara', 'Monica', 'Kelly'],
    'Math': [5, 4, 5, 5, 3, 3, 3, 5, 3, 2],
    'Physics': [4, 4, 3, 5, 4, 3, 3, 5, 4, 1],
    'Biology': [4, 3, 4, 5, 5, 4, 4, 5, 4, 2],
    'Astronomy': [3, 5, 3, 5, 4, 5, 4, 4, 3, 3],
    'Chemistry': [4, 4, 5, 5, 4, 3, 5, 5, 4, 2]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Вывод DataFrame
print(df)
print(f"Средняя оценка - {df['Math'].mean()}")
print(f"Средняя оценка - {df['Physics'].mean()}")
print(f"Средняя оценка - {df['Biology'].mean()}")
print(f"Средняя оценка - {df['Astronomy'].mean()}")
print(f"Средняя оценка - {df['Chemistry'].mean()}")

print(f"Медианный оценка - {df['Math'].median()}")
print(f"Медианный оценка - {df['Physics'].median()}")
print(f"Медианный оценка - {df['Biology'].median()}")
print(f"Медианный оценка - {df['Astronomy'].median()}")
print(f"Медианный оценка - {df['Chemistry'].median()}")

df.boxplot(column='Math')
plt.show()

#stdMath = df['Math'].std()
#print(f"Стандартное отклонение Math - {stdMath}")

#stdPhysics = df['Physics'].std()
#print(f"Стандартное отклонение Physics - {stdPhysics}")

#stdBiology = df['Biology'].std()
#print(f"Стандартное отклонение Biology - {stdBiology}")

#stdAstronomy = df['Astronomy'].std()
#print(f"Стандартное отклонение Astronomy - {stdAstronomy}")

#stdChemistry = df['Chemistry'].std()
#print(f"Стандартное отклонение Chemistry - {stdChemistry}")



#print(df.describe())

Q1_math = df['Math'].quantile(0.25)
Q3_math = df['Math'].quantile(0.75)

IQR = Q3 - Q1

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['Math'] >= downside) & (df['Math'] <= upside)]

df_new.boxplot(column='Math')
plt.show()