# импортирую библиотеку pandas как главного инструмента для решения поставленных задач
import pandas as pd
# импортирую библиотеку seaborn как главного инструмента для визуализации
import seaborn as sns
# импортирую библиотеку matplotlib
import matplotlib.pyplot as plt


# In[2]:


# открываем файл
df = pd.read_csv('/datasets/real_estate_data.csv')


# In[3]:


# начинаем изучать файлы
df.head(10)


# <div class="alert alert-info"> <b>Комментарий студента:</b> Первое, что бросается в глаза это необходимость указания в качестве разделителя знак табуляции \t, и сохранения результа </div>

# In[4]:


# добавляем функции read_csv() аргумент sep='\t' и сохраняем этот результат
df = pd.read_csv('/datasets/real_estate_data.csv', sep='\t')


# In[5]:


# посмотрим еще раз на первые 15 строк датафрейма
df.head(15)


# In[6]:


# посмотрим, для более полного первичного представления о датафрейме, последние его 15 строк
df.tail(15)


# <div class="alert alert-info"> <b>Комментарий студента:</b> В ходе первичного осмотра датафрейма наблюдаются следующие его недостатки:
# 
# *1. Объявления обезличены, отсутствует столбец, который позволяет идентифицировать каждое уникальное объявление. Требуется создать 'id';*
# 
# *2.  Наименования атрибутов представлены в хорошем стиле, 'змеинный регистр' соблюден;*
#     
# *3. Во многих столбцах встречаются NaN (отсутствующее в ячейке число), что свидетельствует об отсутствии данных. Значения None (нечисловой тип 'NoneType')  встречается в единичном случае (11 строка, столбец 'is_apartment'), что также свидетельствует об их наличии в датафрейме.*
# 
# пришло время получить общую информацию о данных в таблице df
df.info() 

# **Описание данных из условия проектной работы:**
# 
# - airports_nearest — расстояние до ближайшего аэропорта в метрах (м)
# - balcony — число балконов
# - ceiling_height — высота потолков (м)
# - cityCenters_nearest — расстояние до центра города (м)
# - days_exposition — сколько дней было размещено объявление (от публикации до снятия)
# - first_day_exposition — дата публикации
# - floor — этаж
# - floors_total — всего этажей в доме
# - is_apartment — апартаменты (обжект!)
# - kitchen_area — площадь кухни в квадратных метрах (м²)
# - last_price — цена на момент снятия с публикации
# - living_area — жилая площадь в квадратных метрах (м²)
# - locality_name — название населённого пункта
# - open_plan — свободная планировка (булев тип)
# - parks_around3000 — число парков в радиусе 3 км
# - parks_nearest — расстояние до ближайшего парка (м)
# - ponds_around3000 — число водоёмов в радиусе 3 км
# - ponds_nearest — расстояние до ближайшего водоёма (м)
# - rooms — число комнат
# - studio — квартира-студия (булев тип)
# - total_area — площадь квартиры в квадратных метрах (м²)
# - total_images — число фотографий квартиры в объявлении

# **Анализируя полученную информацию устанавливаем следующее описание датафрейма:**
# 
# 1. В столбце 'ceiling_height' из должных 23699 данных есть 14504 данных, в 'floors_total' из должных 23699 данных представлены 23613б, в living_area из должных 23699 данных указаны 21796 данных, is_apartment включает всего - 2775 данных, kitchen_area всего 21421, balcony всего 12180, аналогичная ситуация в столбцах locality_name, airports_nearest, cityCenters_nearest, parks_around3000, parks_nearest, ponds_around3000, parks_nearest, ponds_around3000,ponds_nearest, days_exposition.
# 2. в таблице двадцать два столбца (22) и 23699 строк. Тип данных в 3-х столбцах — object. Тип данных в 3-х столбцах - int64. В 14-ти столбцах тип данных - float64, тип булевых значений в 2-х столбцах (studio, open_plan). Особенное внимание обращают типы данных в следующих столбцах: 
#  - parks_around3000 - тип данных указан float64. Очевидно, что наиболее подходящий тип данных по данному значению int64.
#  - balcony - тип данных указан float64. Очевидно, что наиболее подходящий тип данных по данному значению int64.
#  - is_apartment - тип данных указан object. Очевидно, что наиболее подходящий тип булевых данных.
#  - floors_total - тип данных указан float64. Представляется, что наиболее подходящий тип данных int64.
#  - first_day_exposition - тип данных указан object. Представляется, что наиболее подходящий тип данных date.

# ### Вывод

# <div class="alert alert-info"> <b>Комментарий студента:</b> В ходе первичного осмотра датафрейма наблюдаются следующие его недостатки:
# 
# *1. Объявления обезличены, отсутствует столбец, который позволяет идентифицировать каждое уникальное объявление. Требуется создать 'id';*
# 
# *2.  Наименования атрибутов представлены в хорошем стиле, 'змеинный регистр' соблюден;*
#     
# *3. Во многих столбцах встречаются NaN (отсутствующее в ячейке число), что свидетельствует об отсутствии данных. Значения None (нечисловой тип 'NoneType')  встречается в единичном случае (11 строка, столбец 'is_apartment'), что также свидетельствует о возможности наличия полностью случайных, случайных, неслучайных значений в датафрейме;*
# 
# *4. В столбце 'ceiling_height' из должных 23699 данных есть 14504 данных, в 'floors_total' из должных 23699 данных представлены 236136, в living_area из должных 23699 данных указаны 21796 данных, is_apartment включает всего - 2775 данных, kitchen_area всего 21421, balcony всего 12180, аналогичная ситуация в столбцах locality_name, airports_nearest, cityCenters_nearest, parks_around3000, parks_nearest, ponds_around3000, parks_nearest, ponds_around3000,ponds_nearest, days_exposition. Необходимо поработать над пропущенными значениями в каждом отдельном случае.*
# 
# *5. Особенное внимание обращают типы данных в следующих столбцах:
# parks_around3000 - тип данных указан float64. Очевидно, что наиболее подходящий тип данных по данному значению int64.
# balcony - тип данных указан float64. Очевидно, что наиболее подходящий тип данных по данному значению int64.
# is_apartment - тип данных указан object. Очевидно, что наиболее подходящий тип булевых данных.
# floors_total - тип данных указан float64. Представляется, что наиболее подходящий тип данных int64.
# first_day_exposition - тип данных указан object. Представляется, что наиболее подходящий тип данных date.*
#     
# **Человеческий фактор, ошибки системы или процесса выгрузки «испортили» датафрейм, то есть сделали его непригодным для анализа. Вместе с тем датафрейм можно "вылечить" и сделать его пригодным для использования аналитических инструментов. Для обеспечения этого процесса необходимо приступить к следующему шагу - предобработке данных.** 
# 
# ## Предобработка данных

# In[8]:


# проведем подсчёт пропусков
(df.isna().sum())


# In[9]:


# расчитаем общее количество 'NaN'  в дата фрейме
print('NaN occurrences in DataFrame:')
df.isna().sum().sum()

# **Начнем с высоты потолков**

# In[10]:


# убедимся, что 'NaN' содержится в столбце датафрейма 'ceiling_height' (высота потолков)
df['ceiling_height'].isna().sum()


# In[11]:


# предлагается заменить значения 'NaN' в столбце датафрейма 'ceiling_height' (высота потолков)  на медиану
# среднее арифметическое значение mean может исказить значения существенно и сделать расчеты недостоверными
median_ceiling_height = df['ceiling_height'].median(skipna=True)


# In[12]:


df['ceiling_height'] = df.ceiling_height.fillna(median_ceiling_height)


# In[ ]:


# убедимся, что 'NaN' заменен на медиану в столбце датафрейма 'ceiling_height'
df['ceiling_height'].isna().sum()

# **Рассмотрим столбец с этажами в доме, если они конечно в доме есть.**

# In[14]:


# убедимся, что 'NaN' содержится в столбце датафрейма 'floors_total' (всего этажей в доме)
df['floors_total'].isna().sum()

# In[15]:

# посмотрим несколько строк где встречается NaN в столбце датафрейма 'floors_total' (всего этажей в доме)
df.query('floors_total == "NaN"').head()


# предлагается заменить значения 'NaN' в столбце датафрейма 'floors_total' на среднее арифметические значения.
mean_floors_total = df['floors_total'].mean(skipna=True)

# In[17]:


df['floors_total'] = df.floors_total.fillna(mean_floors_total)


# In[18]:


# убедимся, что 'NaN' не содержится в столбце датафрейма 'floors_total' (всего этажей в доме)
df['floors_total'].isna().sum()


# In[19]:


# подсчитаем на всякий случай количество строк где встрчаются пропущенные значения
print(len(df[df['floors_total'].isna()]))


# In[20]:


# осуществим изменение типа данных с float64 на наиболее подходящий тип данных int64.
df[['floors_total']] = df[['floors_total']].astype(int)


# In[21]:


# проверим смену типа данных в 'floors_total'
(df['floors_total']).dtypes


# **Рассмотрим столбец living_area (жилая площадь в квадратных метрах (м²).**

# <div class="alert alert-info"> <b>Комментарий студента:</b> Для исследования данных данный показатель имеет важное значение, процент пропусков по данному атрибуту составляет 8,03 % и требуется заменить их на наиболее приблеженные значения. Представляется, что в данном случае следует использовать медианные значения.  </div>

# In[22]:


# убедимся, что 'NaN' содержится в столбце датафрейма 'living_area' 
df['living_area'].isna().sum()


# In[23]:


# предлагается заменить значения 'NaN' в столбце датафрейма 'living_area' на медиану
median_living_area = df['living_area'].median(skipna=True)


# In[24]:


df['living_area'] = df.living_area.fillna(median_living_area)


# In[25]:


# убедимся, что 'NaN' заменен на медиану в столбце датафрейма 'living_area'
df['living_area'].isna().sum()

# **Рассмотрим столбец is_apartment.**

# In[26]:


# убедимся, что 'NaN' содержится в столбце датафрейма is_apartment
df['is_apartment'].isna().sum()


# <div class="alert alert-info"> <b>Комментарий студента:</b> Данный столбец  is_apartment содержит наибольшее количество пропущенных значений - 20924 или 88.29%. Как отмечалось ранее в столбце is_apartment встречаются категориальные значения. Например, 'False' </div>

# In[27]:


# рассмотрим уникальные значения в столбце 'is_apartment'
df['is_apartment'].value_counts()


# <div class="alert alert-info"> <b>Комментарий студента:</b> Количество True значительно ниже False, что соответствует природе возникновения аппартаментов как нового формата купли-продажи недвижимости. Мы не можем быть полностью уверены, что все значения NaN являются False, но следуя правилу большинства данных, попробуем все значения NaN привести к False.   </div>

# In[28]:


# заменяем значения NaN на False
df['is_apartment'] = df['is_apartment'].fillna(False)


# In[29]:


# рассмотрим еще раз уникальные значения в столбце 'is_apartment'
df['is_apartment'].value_counts()


# <div class="alert alert-info"> <b>Комментарий студента:</b> Сумма значений False и True свидетельствет, что столбец  is_apartment обработан.   </div>

# In[30]:


# убедимся, что 'NaN' больше не содержится в столбце датафрейма is_apartment
df['is_apartment'].isna().sum()


# In[31]:


# изменим тип данных int на более профильный тип для категориальных данных - bool
df[['is_apartment']] = df[['is_apartment']].astype(bool)


# In[32]:


# проверим смену типа данных в 'is_apartment'
(df['is_apartment']).dtypes

# **Рассмотрим столбец kitchen_area (площадь кухни в квадратных метрах (м²)**

# In[33]:


# убедимся, что 'NaN' содержится в столбце датафрейма kitchen_area 
df['kitchen_area'].isna().sum()


# <div class="alert alert-info"> <b>Комментарий студента:</b> Количество NaN подтверждается. По аналогии с 'living_area' проведем заполнение пропущенных значений на медианные значения. </div>

# In[34]:


# предлагается заменить значения 'NaN' в столбце датафрейма 'kitchen_area' на медиану
median_kitchen_area = df['kitchen_area'].median(skipna=True)


# In[35]:


df['kitchen_area'] = df.kitchen_area.fillna(median_kitchen_area)


# In[36]:


# убедимся, что 'NaN' заменен на медиану в столбце датафрейма 'kitchen_area'
df['kitchen_area'].isna().sum()


# <div class="alert alert-info"> <b>Комментарий студента:</b> Можем продолжить работу. </div>

# **Рассмотрим столбец balcony (число балконов)**

# <div class="alert alert-info"> <b>Комментарий студента:</b> Как отмечалось ранее при первичном рассмотрении датафрейма в столбце 'балконы'  тип данных указан float64, более логичным значением для данного показателя будет тип integer.</div>

# In[37]:


# убедимся, что 'NaN' содержится в столбце датафрейма 'balcony'
df['balcony'].isna().sum()


# In[38]:


# далее рассмотрим уникальные значения в столбце датафрейма 'balcony'
df['balcony'].value_counts()


# <div class="alert alert-info"> <b>Комментарий студента:</b> Представляется более логичным заменить пропущенные значения в количестве балконов на 0, то есть показатель их отсутствия. Обоснованием такого шага является экономический взгляд с той точки зрения, что необоснованное их обозначение может серьезно повлиять на показатель цены как возможного целевого показателя (атрибута) в этом фрейме данных. </div>

# In[39]:


# используем метод fillna и вставляем вместо NaN  нули
df['balcony'] = df['balcony'].fillna(0)


# In[40]:


# изменим тип данных float на более профильный тип для подобных категориальных данных - int
df[['balcony']] = df[['balcony']].astype(int)


# In[41]:


# далее рассмотрим повторно уникальные значения в столбце датафрейма 'balcony'
df['balcony'].value_counts()

# <div class="alert alert-info"> <b>Комментарий студента:</b> Можем даигаться дальше. </div>

# **Продолжим рассмотрение столбцов и следующий у нас locality_name (название населённого пункта).**

# <div class="alert alert-info"> <b>Комментарий студента:</b> Небольшая характеристика: данный показатель является категориальным значением,  наиболее подходящим типом данных является в данном случае object, присвоенный ему изначально. </div>

# In[42]:


# убедимся, что 'NaN' содержится в столбце датафрейма 'locality_name'
df['locality_name'].isna().sum()


# <div class="alert alert-info"> <b>Комментарий студента:</b> 49 случаев, в масштабах всего фрейма это всего 0,21 % , то есть весьма не критично. Вместе с тем название населённого пункта очень важный показатель, поскольку без его понимания с учетом специфики кейса в проекте (недвижимость), дальнейшее рассмотрение других данных в строке не представляется целесообразным для потенциального покупателя. При других обстоятельствах можно было бы попросить уточнить у авторов заполнить недостающие данные. В нашем случае это невозможно и в этой связи предлагается удалить отсутствующие значения целиком. </div>

# In[43]:


# удаляем 49 случаев с отсутствующими данными в названии населённого пункта
# указываем на значение TRUE, изменения сохраняются в новом объекте, который создается, и он не изменяет исходные данные.
# указываем axis = 0, чтобы работать с удалением строк! Критично важно!
df.dropna(subset=['locality_name'],inplace=True, axis=0)


# In[44]:


# убедимся, что 'NaN' не содержится в столбце датафрейма 'locality_name'
df['locality_name'].isna().sum()

# **Рассмотрим столбец 'airports_nearest' (расстояние до ближайшего аэропорта в метрах (м)**

# In[45]:


# убедимся, что 'NaN' содержится в столбце датафрейма airports_nearest
df['airports_nearest'].isna().sum()


# In[46]:


# проверим тип данных в 'airports_nearest'
(df['airports_nearest']).dtypes


# <div class="alert alert-info"> <b>Комментарий студента:</b> тип данных float подходит для измерения в метрах. В части выявленных пропущенных значений предлагается их заменить на среднее арифметическое. </div>

# In[47]:


# предлагается заменить значения 'NaN' в столбце датафрейма 'airports_nearest' на среднее арифметические значения.
mean_airports_nearest = df['airports_nearest'].mean(skipna=True)

# In[48]:


df['airports_nearest'] = df.airports_nearest.fillna(mean_airports_nearest)


# In[49]:


# убедимся, что 'NaN' не содержится в столбце датафрейма airports_nearest
df['airports_nearest'].isna().sum()


# **Рассмотрим следующий столбец cityCenters_nearest расстояние до центра города (м)**

# In[50]:


# убедимся, что 'NaN' содержится в столбце датафрейма cityCenters_nearest
df['cityCenters_nearest'].isna().sum()


# In[51]:


# проверим тип данных в 'airports_nearest'
(df['cityCenters_nearest']).dtypes


# <div class="alert alert-info"> <b>Комментарий студента:</b> тип данных float подходит для измерения в метрах. В части выявленных пропущенных значений предлагается аналогично предыдущему столбцу их заменить на среднее арифметическое. </div>

# In[52]:


# предлагается заменить значения 'NaN' в столбце датафрейма 'cityCenters_nearest' на среднее арифметические значения.
mean_cityCenters_nearest = df['cityCenters_nearest'].mean(skipna=True)

# In[53]:


df['cityCenters_nearest'] = df.cityCenters_nearest.fillna(mean_cityCenters_nearest)


# In[54]:


# убедимся, что 'NaN' не содержится в столбце датафрейма cityCenters_nearest
df['cityCenters_nearest'].isna().sum()


# In[55]:


# добавим столбец id_client
df['id_client'] = df.reset_index().index


# **Рассмотрим столбец parks_around3000 (число парков в радиусе 3 км)**

# <div class="alert alert-info"> <b>Комментарий студента:</b> В ходе первичного рассмтрения данных было установлено, что в parks_around3000 - тип данных указан float64. Очевидно, что наиболее подходящий тип данных по данному значению int64.  </div>

# In[56]:


# убедимся, что 'NaN' содержится в столбце датафрейма parks_around3000
df['parks_around3000'].isna().sum()


# In[57]:


# далее рассмотрим уникальные значения в столбце датафрейма 'parks_around3000'
df['parks_around3000'].value_counts()


# <div class="alert alert-info"> <b>Комментарий студента:</b> Рассмотрев уникальные значения предлагается принять меры аналогичные в случае со столбцом "балконы". </div>

# In[58]:


# используем метод fillna и вставляем вместо NaN  нули
df['parks_around3000'] = df['parks_around3000'].fillna(0)


# In[59]:


# изменим тип данных float на более профильный тип для подобных категориальных данных - int
df[['parks_around3000']] = df[['parks_around3000']].astype(int)


# In[60]:


# далее рассмотрим повторно уникальные значения в столбце датафрейма 'parks_around3000'
df['parks_around3000'].value_counts()

# **Рассмотрим столбец "parks_nearest" (расстояние до ближайшего парка (м)**

# In[61]:


# убедимся, что 'NaN' содержится в столбце датафрейма parks_nearest
df['parks_nearest'].isna().sum()


# In[62]:


# проверим тип данных в parks_nearest
(df['parks_nearest']).dtypes

# In[63]:


# предлагается заменить значения 'NaN' в столбце датафрейма 'parks_nearest' на медиану
median_parks_nearest = df['parks_nearest'].median(skipna=True)


# In[64]:


df['parks_nearest'] = df.parks_nearest.fillna(median_parks_nearest)


# In[65]:


# убедимся, что 'NaN' заменен на медиану в столбце датафрейма parks_nearest
df['parks_nearest'].isna().sum()


# **Рассмотрим столбец ponds_around3000 (число водоёмов в радиусе 3 км)**

# In[66]:


# убедимся, что 'NaN' содержится в столбце датафрейма ponds_around3000
df['ponds_around3000'].isna().sum()


# In[67]:


# проверим тип данных в  ponds_around3000
(df['ponds_around3000']).dtypes

# далее рассмотрим уникальные значения в столбце датафрейма
df['ponds_around3000'].value_counts()

# используем метод fillna и вставляем вместо NaN  нули
df['ponds_around3000'] = df['ponds_around3000'].fillna(0)


# In[70]:


# изменим тип данных float на более профильный тип для подобных категориальных данных - int
df[['ponds_around3000']] = df[['ponds_around3000']].astype(int)


# In[71]:


# далее повторно рассмотрим уникальные значения в столбце датафрейма 
df['ponds_around3000'].value_counts()


# **Рассмотрим ponds_nearest (расстояние до ближайшего водоёма (м))**

# In[72]:


# убедимся, что 'NaN' содержится в столбце датафрейма ponds_nearest
df['ponds_nearest'].isna().sum()


# In[73]:


# проверим тип данных в ponds_nearest
(df['ponds_nearest']).dtypes


# In[74]:


# предлагается заменить значения 'NaN' в столбце датафрейма ponds_nearest на медиану
median_ponds_nearest = df['ponds_nearest'].median(skipna=True)


# In[75]:


df['ponds_nearest'] = df.ponds_nearest.fillna(median_ponds_nearest)


# In[76]:


# убедимся, что 'NaN' заменен на медиану в столбце датафрейма ponds_nearest 
df['ponds_nearest'].isna().sum()


# **Рассмотрим последний столбец days_exposition сколько дней было размещено объявление (от публикации до снятия)**

# In[77]:


# убедимся, что 'NaN' содержится в столбце датафрейма days_exposition 
df['days_exposition'].isna().sum()


# In[78]:


# проверим тип данных в days_exposition
(df['days_exposition']).dtypes



# предлагается заменить значения 'NaN' в столбце датафрейма ponds_nearest на медиану
median_days_exposition = df['days_exposition'].median(skipna=True)


df['days_exposition'] = df.days_exposition.fillna(median_days_exposition)


# In[81]:


# убедимся, что 'NaN' заменен на медиану в столбце датафрейма ponds_nearest 
df['days_exposition'].isna().sum()


# In[82]:


# изменим тип данных float на  int
df[['days_exposition']] = df[['days_exposition']].astype(int)


# **Столбец 'first_day_exposition' переводим в тип данных date**

# In[83]:


#переведем столбец с датой в формат даты без времени, посольку время не указано
df['first_day_exposition'] = pd.to_datetime(df['first_day_exposition'], format = '%Y-%m-%d')


# In[84]:


# проверим тип данных в first_day_exposition
(df['first_day_exposition']).dtypes


# In[85]:


# пришло время посмотреть общую информацию о данных в таблице df с учетом проделанной работы по обработке данных
df.info() 


# **Для чистоты работы попробуем посмотреть наличие дубликатов во фрейме данных**

# In[86]:


# рассмотреим дата сет на предмет наличия явных дубликатов
(df.duplicated().sum())



# попробую удалить дубликаты, если они есть и потом сравнить.
df = df.drop_duplicates()
df.info()

# ## Расчёты и добавление результатов в таблицу

# **Рассчитаем и добавим в таблицу: цену квадратного метра**

# In[88]:


# предлагаемая формула:
df['price_per_square_meter'] = df['last_price'] / df['total_area']


# In[89]:


# посмотрим на результат
df.head()


# <div class="alert alert-info"> <b>Комментарий студента:</b> Тип float целесообразно заменить на int.</div>

# In[90]:


df['price_per_square_meter'] = df['price_per_square_meter'].astype(int)


# In[91]:


# посмотрим еще раз на результат
df.head()


# <div class="alert alert-info"> <b>Комментарий студента:</b> Можно работать дальше.</div>

# **Расчитаем и добавим в таблицу: день недели, месяц и год публикации объявления**

# In[92]:


#создадим столбец дня недели
df['weekday_exposition'] = df['first_day_exposition'].dt.weekday


# In[93]:


#создадим столбец месяца
df['month_exposition'] = df['first_day_exposition'].dt.month


# In[94]:


#создадим столбец года
df['year_exposition'] = df['first_day_exposition'].dt.year


# In[95]:


# посмотрим на результат
df.head()

# **Рассчитаем и добавим в таблицу: этаж квартиры; варианты — первый, последний, другой**

# In[96]:


# для наиболее быстрого и удобного расчета построим функцию
def floor_category(row):
    floors_total = row['floors_total']
    floor = row['floor']
    if floor == 1:
        return 'первый'
    elif floor == floors_total:
        return 'последний'
    elif 1 < floor < floors_total:
        return 'другой'

# используем функцию для категоризации этажей
df['floor_category'] = df.apply(floor_category, axis = 1)


# In[98]:


# посмотрим на результат
df.head()


# добавим столбец соотношения жилой площади к общей
# округлим методом round значения во фрейме данных
df['useful_area'] = (df['living_area'] / df['total_area']).round(2)


# In[100]:


# добавим столбец отношения площади кухни к общей
# округлим методом round значения во фрейме данных
df['kitchen_total_area'] = (df['kitchen_area'] / df['total_area']).round(2)


# In[101]:


# посмотрим на результат
df.head()

# ## Исследовательский анализ данных

# **Изучаем следующие параметры: площадь, цена, число комнат, высота потолков**

# In[102]:


# для начала посмотрим общие данные
df['total_area'].describe()


# In[103]:


# изучим c использованием гистограмм общую площадь
df.plot(y ='total_area', kind ='hist', bins = 100, grid=True, figsize = (5,3), range = (0,500))

# изучим цену
df.plot(y = 'last_price', kind = 'hist', bins = 100, grid=True, range = (0,15000000), figsize = (5,3))
df['last_price'].describe()

#изучим число комнат
#df.plot(y = 'rooms', kind = 'hist', bins = 30, grid=True, figsize = (5,3))
df['rooms'].value_counts().plot.bar()
df['rooms'].describe()

#изучим высоту потолков
df.plot(y = 'ceiling_height', kind = 'hist', bins = 30, range = (2,5), grid=True, figsize = (5,3))
df['ceiling_height'].describe()

#диаграмма размаха
plt.boxplot(df[df['days_exposition']!=0]['days_exposition'])
plt.ylim(1,1000)

df.plot(y = 'days_exposition', kind = 'hist', bins = 30, grid = True, range = (1,1600))
df.plot(y = 'days_exposition', kind = 'hist', bins = 100, grid = True, range = (1,200))

#среднее значение, медиана и межквартильный размах
df[df['days_exposition']!=0]['days_exposition'].describe()




# попробуем найти аномалии с помощью инструментов визуализация данных
plt.style.use('ggplot')


# In[109]:


# используем диаграмму размаха
df['days_exposition'].plot(kind='box')
plt.show()


# In[110]:


# устраним выявленные аномалии
days_df = df.query('days_exposition != 45 and days_exposition != 30 and days_exposition != 60 and days_exposition != 90 and days_exposition != 7 and days_exposition != 0')


# In[111]:


# диаграмма размаха
plt.boxplot(days_df['days_exposition'])
plt.ylim(1,1000)

#гистограммы
days_df.plot(y = 'days_exposition', kind = 'hist', bins = 30, grid = True, range = (1,1600))
days_df.plot(y = 'days_exposition', kind = 'hist', bins = 100, grid = True, range = (1,200))

#среднее значение, медиана и межквартильный размах
#good_data['days_exposition'].value_counts()
days_df['days_exposition'].describe()

# используем в работе метод сводных таблиц для проведения расчетов по условиям задания
# рассмотрим корреляцию цены квадратного метра от общей площади квартиры
pivot_table_total_area = df.pivot_table(index = 'total_area', values = 'price_per_square_meter', aggfunc = ['mean', 'count', 'median'])
pivot_table_total_area.columns = ['mean', 'count', 'median']
pivot_table_total_area.plot(y = 'median', style = 'o')

pivot_table_total_area.sort_values('median', ascending = False)

df['total_area'].corr(df['price_per_square_meter'])

# Изучим зависимость цены квадратного метра от числа комнат.

pivot_table_rooms = df.pivot_table(index = 'rooms', values = 'price_per_square_meter', aggfunc = ['mean', 'count', 'median'])
pivot_table_rooms.columns = ['mean', 'count', 'median']
pivot_table_rooms.query('count > 50').plot(y = 'median')

pivot_table_rooms.query('count > 50').sort_values('median', ascending = False)

df['rooms'].corr(df['price_per_square_meter'])

# рассмотрим зависимость цены квадратного метра от этажа (первого или последнего).
pivot_table_floor_category = df.query('floor_category != "другой"').pivot_table(index = 'floor_category', values = 'price_per_square_meter', aggfunc = ['mean', 'count', 'median'])
pivot_table_floor_category.columns = ['mean', 'count', 'median']
pivot_table_floor_category.plot(y = 'median')
pivot_table_floor_category

# зависимость цены квадратного метра от удалённости от центра.
df.plot(kind = 'scatter', y = 'price_per_square_meter', x = 'cityCenters_nearest', alpha = 0.3)

df['cityCenters_nearest'].corr(df['price_per_square_meter'])


# зависимость цены квадратного метра от даты размещения: дня недели.
pivot_table_weekday_exposition = df.pivot_table(index = 'weekday_exposition', values = 'price_per_square_meter', aggfunc = ['mean', 'count', 'median'])
pivot_table_weekday_exposition.columns = ['mean', 'count', 'median']
pivot_table_weekday_exposition.plot(y = 'median')

pivot_table_weekday_exposition.sort_values('median', ascending = False)


# определим зависимость цены квадратного метра от даты размещения: месяца.
pivot_table_month_exposition = df.pivot_table(index = 'month_exposition', values = 'price_per_square_meter', aggfunc = ['mean', 'count', 'median'])
pivot_table_month_exposition.columns = ['mean', 'count', 'median']
pivot_table_month_exposition.plot(y = 'median')

pivot_table_month_exposition.sort_values('median', ascending = False)


# рассмотрим зависимость цены квадратного метра от даты размещения: года.
pivot_table_year_exposition = df.pivot_table(index = 'year_exposition', values = 'price_per_square_meter', aggfunc = ['mean', 'count', 'median'])
pivot_table_year_exposition.columns = ['mean', 'count', 'median']
pivot_table_year_exposition.plot(y = 'median')

pivot_table_year_exposition.sort_values('median', ascending = False)


# <div class="alert alert-info"> <b>Комментарий студента: с 2014 до 2016 года цена падала, но далее начала увеличиваться. </b>
#     </div>

# **задание: "Какие факторы больше всего влияют на стоимость квартиры? Изучите, зависит ли цена от квадратного метра, числа комнат, этажа (первого или последнего), удалённости от центра. Также изучите зависимость от даты размещения: дня недели, месяца и года. "Выберите 10 населённых пунктов с наибольшим числом объявлений. Посчитайте среднюю цену квадратного метра в этих населённых пунктах. Выделите населённые пункты с самой высокой и низкой стоимостью жилья. Эти данные можно найти по имени в столбце '*locality_name'**

# In[119]:


locality_pivot_table = df.pivot_table(index = 'locality_name', values = 'price_per_square_meter', aggfunc=['count', 'mean'])
locality_pivot_table.columns = ['count', 'mean']
locality_pivot_table = locality_pivot_table.sort_values('count', ascending = False).head(10)
locality_pivot_table


# In[120]:


# определим самую высокую стоимость
locality_pivot_table[locality_pivot_table['mean']==locality_pivot_table['mean'].max()]


# In[121]:


# и самую низкую стоимость
locality_pivot_table[locality_pivot_table['mean']==locality_pivot_table['mean'].min()]


# <div class="alert alert-info"> <b>Комментарий студента: самая высокая стоимость жилья из 10 населённых пунктов с самым большим количеством объявлений в Санкт-Петербурге, тогда как самая низкая стоимость в Выборге. </b>
#     </div>

# **задание: "Изучите предложения квартир: для каждой квартиры есть информация о расстоянии до центра. Выделите квартиры в Санкт-Петербурге (*'locality_name'*). Ваша задача — выяснить, какая область входит в центр. Создайте столбец с расстоянием до центра в километрах: округлите до целых значений. После этого посчитайте среднюю цену для каждого километра. Постройте график: он должен показывать, как цена зависит от удалённости от центра. Определите границу, где график сильно меняется — это и будет центральная зона.**

# In[122]:


df['cityCenters_nearest_km'] = df['cityCenters_nearest']/1000
df['cityCenters_nearest_km'] = df['cityCenters_nearest_km'].fillna(999999)
df['cityCenters_nearest_km'] = df['cityCenters_nearest_km'].astype(int)
pivot_table_km = df.query('locality_name == "Санкт-Петербург" and cityCenters_nearest_km !=999999').pivot_table(index = 'cityCenters_nearest_km', values = 'price_per_square_meter', aggfunc = 'mean')
pivot_table_km.plot()
pivot_table_km


# <div class="alert alert-info"> <b>Комментарий студента: Все, что попадает в радиус трех км считается центром в Санкт-Петербурге. </b>
#     </div>

# **задание: "Выделите сегмент квартир в центре. Проанализируйте эту территорию и изучите следующие параметры: площадь, цена, число комнат, высота потолков. Также выделите факторы, которые влияют на стоимость квартиры (число комнат, этаж, удалённость от центра, дата размещения объявления). Сделайте выводы. Отличаются ли они от общих выводов по всему городу?"**

# In[123]:


# выделим квартиры в центре, беря за радиус 3 км
center_spb_data = df.query('cityCenters_nearest_km <= 3 and locality_name == "Санкт-Петербург"')


# In[124]:


# определим зависимость стоимости квадратного метра от количества комнат.
center_spb_rooms = center_spb_data.pivot_table(index = 'rooms', values = 'price_per_square_meter', aggfunc = ['mean', 'count', 'median'])
center_spb_rooms.columns = ['mean', 'count', 'median']
center_spb_rooms.query('count > 50').plot(y = 'median')

center_spb_rooms.query('count > 50').sort_values('median', ascending = False)

center_spb_data['rooms'].corr(center_spb_data['price_per_square_meter'])


# <div class="alert alert-info"> <b>Комментарий студента:  в центре Санкт_Петербурга чем меньше комнат тем дороже стоимость метра квадратного, в отличие от всей выборки, где стоимость уменьшается в зависимости от близости количества комнат к 3. Данный результат соответсвует действительности. </b>
#     </div>

# ## Общий вывод

# 1. датафрейм после "лечения" стал пригодным для использования аналитических инструментов.
# 2. Проведена предообработка данных, главная проблема заключалась в большом количестве пропущенных значений.
# 3. В ходе проведения исследования изучены параметры: площадь, цена, число комнат, высота потолков. Результаты изучения приятно удивили их соответстсвием реалиям рынка.
# 4. Из представленных данных следует, что наибольшее количество квартир в Санкт-Петербурге и в пригородах вокруг него, приходится на однокомнатные квартиры, незначительно уступают двухкомнатные квартиры.
# 5. В подовляющем большинстве исследуемых квартир высота потолков составляет от 2,5 м до 3 м.
# 6. Из-за наличия аномалий в данных сложно определиться когда продажи очень быстро проходили, а когда необычно долго.
# 7. Величина площади квартиры незначительно влияет на стоимость.
# 8. Обнаружена закономерность, что квадратные метры падают в цене приближаясь к трем комнатам.
# 9. обнаружена закономерность, что чем выше этаж тем дороже квадратный метр, как правило квартиры на первом этаже дешевле квартир на последнем этаже - в среднем на 10%.
# 10. Обнаружена закономерность, что чем ближе к центру, тем выше стоимость квадратного метра.
# 11. Обнаружена закономерность, что чем ближе ко вторнику выставлены объявления тем в среднем выше стоимость.Также заметно, что по субботам стоимость самая низкая.
# 12. самая высокая стоимость метра в апреле и августе. Самая низкая стоимость в мае и июне. На рынке недвижимости, как и во многих других сферах присутствует сезонность - в начале лета мы видим наименьшее предложение как по количеству, так и по стоимости недвижимости.
# 13. На рынке недвижимости СПБ с 2014 до 2016 года цена падала, но далее начала увеличиваться.
# 14. самая высокая стоимость жилья из 10 населённых пунктов с самым большим количеством объявлений в Санкт-Петербурге, тогда как самая низкая стоимость в Выборге.
# 15. Все, что попадает в радиус трех км считается центром в Санкт-Петербурге.
# 16. В центре Санкт_Петербурга чем меньше комнат тем дороже стоимость метра квадратного, в отличие от всей выборки, где стоимость уменьшается в зависимости от близости количества комнат к 3. Данный результат соответсвует действительности.




