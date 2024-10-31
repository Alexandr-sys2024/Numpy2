from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv

# Создание экземпляра браузера
driver = webdriver.Chrome()

    # Открытие страницы
url = 'https://www.divan.ru/category/pramye-divany'

# Открытие страницы
driver.get(url)


# Небольшая задержка для полной загрузки страницы
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "//span[contains(@class, 'ui-LD-ZU') and contains(@data-testid, 'price')]")

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()