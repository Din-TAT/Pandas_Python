#Задание
#Загрузите этот файл в датафрейм Pandas (с именем df). Однако, будьте осторожны - перед отправкой кода на проверку посмотрите на свой результат и убедитесь, что вы все загрузили корректно.
#
#Создайте (или переопределите) переменную df таким образом, чтобы она содержала столбцы с названиями:
#
#
#user_id (ранее - id)
#
#created_at (ранее - date_joined)
#
#login (ранее - username)

import pandas as pd

df = pd.read_csv('Проект 2/itresume-users-pandas.csv', sep=';', skiprows=1)

df.columns = ['user_id', 'login', 'created_at']
df = df[['user_id', 'created_at', 'login']]
print(df)