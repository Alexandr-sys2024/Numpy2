import pandas as pd

# Замените 'path_to_your_file.csv' на путь к вашему файлу
file_path = 'cleaned_prices.csv'

# Загружаем данные из CSV файла
df = pd.read_csv(file_path)

# Предположим, что столбец с ценами называется 'price'. Измените при необходимости.
if 'Price' in df.columns:
    average_price = df['Price'].mean()
    print(f'Средняя цена: {average_price}')
else:
    print("Столбец с ценами Price' не найден. Проверьте название столбца.")