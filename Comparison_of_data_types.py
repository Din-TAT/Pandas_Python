#Задание
#Загрузите этот файл в датафрейм Pandas (с именем df). Однако, будьте осторожны - перед отправкой кода на проверку посмотрите на свой результат и убедитесь, что вы все загрузили корректно.
#
#Создайте переменную are_types_equal, в которую запишите результат сравнения типа данных у столбцов username и date_joined.

import pandas as pd

df = pd.read_csv('Проект 2/itresume-users-pandas.csv',sep=';',skiprows=1)
are_types_equal = df['username'].dtype == df['date_joined'].dtype
print(are_types_equal)