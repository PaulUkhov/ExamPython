import random
import pandas as pd
# Для кодировки категориальных данных можно использовать метод pandas get_dummies # pd.get_dummies(df['Type 1'])

# Создание списка с двумя категориями
lst = ['robot'] * 10 + ['human'] * 10

# Перемешивание списка
random.shuffle(lst)

# Создание DataFrame с одним столбцом
data = pd.DataFrame({'whoAmI': lst}) 

data['robot'] = (data['whoAmI'] == 'robot').astype(int) #Преобразование в one hot таблицу в которой если true 1, а если false 0
data['human'] = (data['whoAmI'] == 'human').astype(int)

# Вывод первых нескольких строк DataFrame
print(data.head()) # head для быстрого просмотра
