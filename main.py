# requests, pandas, numpy, matplotlib, pillow
import pandas
import numpy
import matplotlib.pyplot as plt
import requests
from PIL import Image

# Запросить данные с помощью библиотеки requests из API и вывести их в консоль.
url = 'https://www.google.com'
responce = requests.get(url)
if responce.status_code == 200:
    print(responce.text)
else:
    print('error:', responce.status_code)

# Считать данные из файла с помощью библиотеки pandas,
# выполнить простой анализ данных и вывести результаты.
# pip install openpyxl xlsxwriter xlrd - для работы exel
df = pandas.read_excel('data.xlsx')
print(df)
grop = df.sort_values(by='Age', ascending=False)
print(grop)

# Создать массив чисел с помощью библиотеки numpy,
# выполнить математические операции с массивом и вывести результаты.
num1 = [1, 2, 5, 6]
arr = numpy.array(num1)
print(arr * 3)
print(arr ** 2)

# Визуализировать данные с помощью библиотеки matplotlib.
x = numpy.linspace(0, 10, 100)
y1 = numpy.sin(x)
y2 = numpy.cos(x)

plt.plot(x, y1, 'r-', label='Sin')
plt.legend()
plt.title('Sin')
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x, y2, 'g-', label='Cos')
plt.legend()
plt.title('Cos')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Обработать изображение с помощью библиотеки pillow, например,
# изменить его размер, применить эффекты и сохранить в другой формат.
image = Image.open('Figure_1.jpeg')
print(image.format, image.size, image.mode)
image_res = image.rotate(90)
image_res = image_res.resize((300, 300))
image_res.save('myplotRes.png')
