# Яндек Практикум
Проектные работы по образовательной программе Yandex
## Data_Science проекты:
### Certificate: (https://drive.google.com/file/d/1F5NSOPRVl7gfwm2OIg9EMLTVJksBXcrW/view?usp=sharing)
*Этот репозиторий в основном предназначен для проектов, которые я выполнял в рамках Яндекс.Практикума*
*Онлайн-программа анализа данных помогала мне готовиться к карьере специалиста по обработке данных, помогая мне учиться очищать и систематизировать данные, выявлять закономерности и идеи, делать значимые выводы и четко сообщать о важных результатах. Я развиваю навыки работы с Python и его библиотеками анализа данных (Numpy, Pandas, Matplotlib) и SQL по мере создания портфолио проектов*

Совет: Для проектов data science с python я бы рекомендовал вам установить numpy, pandas, scipy, scikit learn, matplotlib, seaborn и другие базовые библиотеки.

## Часть 1 Введение в Data_Science
В этом разделе основное внимание уделяется предварительной обработке данных. Кроме того, были рассмотрены следующие вопросы: Работа с пропусками. Определение аномальных значений. Преобразование типов данных. Основные методы поиска дубликатов. Работа с несовершенными реальными наборами данных.

### Проект 1: research_borrowers
Описание проекта

*Заказчиком проекта является кредитный отдел банка. Задача заключается в том, что необходимо выявить закономерности и понять, влияет ли семейное положение и количество детей клиента на факт своевременного погашения кредита. Входные данные от банка — статистика платежеспособности клиентов.*

**Получены следующие результаты работы:** *с помощью лемматизации были установлены нужные категории для дальнейшего анализа и оценки гипотез; с использованием функций мы определили категории семьи, категории по уровню доходов. Создан словарь для обеспечения словестной категоризации; определили зависимость между семейным положением и возвратом кредита в срок; определили зависимость между количеством детей и возвратом кредита в срок; определили зависимость между уровнем дохода и возвратом кредита в срок; получены ответы на вопрос как разные цели кредита влияют на его возврат в срок.*

## Часть 2 Анализ данных
Визуализация данных с помощью гистограмм и ящиков с усами. Изучение фрагментов данных. Нахождение взаимосвязей различных параметров в данных. Объединение таблиц. Получение выводов из сгруппированных данных.

### Проект 2: market_value_estate
Описание проекта

*Заказчиком работы является организация, работающая в сфере реализации объектов недвижимости. В распоряжении данные сервиса Яндекс.Недвижимость — архив объявлений о продаже квартир в Санкт-Петербурге и соседних населённых пунктах за несколько лет. Нужно научиться определять рыночную стоимость объектов недвижимости.Необходимо  установить параметры. Это позволит построить автоматизированную систему: она отследит аномалии и мошенническую деятельность.*

**Получены следующие результаты работы:** 
- Обнаружена закономерность, что: величина площади квартиры незначительно влияет на стоимость.
- Обнаружена закономерность, что квадратные метры падают в цене приближаясь к трем комнатам.
- обнаружена закономерность, что чем выше этаж тем дороже квадратный метр, как правило квартиры на первом этаже дешевле квартир на последнем этаже - в среднем на 10%.
- Обнаружена закономерность, что чем ближе к центру, тем выше стоимость квадратного метра.
- Обнаружена закономерность, что чем ближе ко вторнику выставлены объявления тем в среднем выше стоимость.Также заметно, что по субботам стоимость самая низкая.
- самая высокая стоимость метра в апреле и августе. Самая низкая стоимость в мае и июне. На рынке недвижимости, как и во многих других сферах присутствует сезонность - - в начале лета мы видим наименьшее предложение как по количеству, так и по стоимости недвижимости.
- на рынке недвижимости СПБ с 2014 до 2016 года цена падала, но далее начала увеличиваться.
самая высокая стоимость жилья из 10 населённых пунктов с самым большим количеством объявлений в Санкт-Петербурге, тогда как самая низкая стоимость в Выборге.

## Часть 3 Статистический анализ данных
Изучение объектов и их взаимосвязей статистическими методами. Выборки и статистическая значимость. Выявление и лечение аномалий.

### Проект 3: determination_promising_tariff
Описание проекта

*Заказчиком работы выступает федеральный оператор мобильной связи компания «Мегалайн». Необходимо провести предварительный анализ тарифов на небольшой выборке клиентов. В нашем распоряжении данные 500 пользователей Megalyne: кто они, откуда, какой тариф они используют, сколько звонков и сообщений каждый отправил в 2018 году. Необходимо проанализировать поведение клиентов и сделать вывод, какой тариф лучше.*

**Получены следующие результаты работы:** 

- в тарифе ultra видим нормальное распределение, со смещением значений данных влево. Наиболее частые значения в минутах наблюдаются в отметке 550 минут, ближе к 700 мин. на графике идет спад. По условиям задачи в тариф ультра включено 3000 минут разговора . Выходит, что большинство пользователей тарифа ультра укладываются в отведенные 3000 мин или 50 час. разговора в месяц. Следовательно большинство пользователей укладываются в абоненсткую плату 1950 рублей;
- по условию тарифа smart 50 сообщений входит в пакет, большинство пользователей тарифа smart отправляют не более 10 сообщений, далее количество пользователей падает, количество сообщений растет. На графике виден хвост тех, кто отправляет больше 50 сообщений в месяц, следовательно данная часть потребителей тратят на сообщение 3 рубля. Например, те кто отправляет дополнительно 30 сообщений переплатят 90 рублей, 50 - 150 рублей, 90 это уже 270 рублей;
- при условии, что гипотеза средняя выручка пользователей тарифов «Ультра» и «Смарт» НЕ различаются - верна, мои предложения в части необходимости инветирования бюджета в рекламную компанию Ультра увеличиваются, поскольку лучше платить 1990 руб ежемесячно, чем переплачивать в три раза больше 550 рублей в Смарте, постоянно ограничивая себя;
- при условии, что гипотеза средняя выручка пользователей из Москвы отличается от выручки пользователей из других регионов - верна, я делаю вывод, что с большой вероятностью московский рынок мог бы стать хорошей экспериментальной площадкой для прокатки вопроса инвестирования бюджета в рекламную компанию тарифа "Ультра" с учетом ранее отмеченных преимуществ тарифа относительно его конкурента Смарт.

## Prefabricated_project_1: Analysis of the gaming products market
Описание проекта

*Прошел первый блок курсов. Пришло время проверить свои знания и решить аналитический кейс.Суть в том, что я позиционируюсь как специалист по обработке данных в интернет-магазине "Streamchik", который продает компьютерные игры по всему миру. Исторические данные о продажах игр, пользовательских и экспертных рейтингах, жанрах и платформах (например, Xbox или PlayStation) доступны из открытых источников. Необходимо выявить закономерности, определяющие успех игры. Это позволит вам делать ставки на потенциально популярный продукт и планировать рекламные кампании.*

**Получены следующие результаты работы:**

*В рамках проекта вывлены следующие закономерности:* 

1) Европейцы предпочитают производителей платформ из Японии, следовательно необходимо выбрать для продажи игры, которые подходят к игровым приставкам: wii, ps3, ps2, ds; 
2) При выборе игр наибольшее предпочтение потребители в Европе (Россия часть Европы) отдают таким жанрам как: action, sports, shooter, role-playning, racing; 
3) Важно помнить, что основными производителями игр явлются компании, которые представлены в Америке и Японии. Расчитывать на то, что американский потребитель или японский в массе обратится в интернет-магазин "Стримчик" не стоит, поскольку их по критерию территориальной принадлежности рынки насыщены собственными производителями. Очевидно, что итогавая цена (стоимость) игровых продуктов для потребителей США и Японии по данному фактору может оказаться ниже из-за отсутствия, например, издержек на транспортировку товаров; 
4) Игровые платформы на рынке по критерию продаж чередуются через каждые три года, важно ориентироваться на планировании продаж игр для платформ, поскольку потребность на игры, например, ps 3, 4 может в текущее время оказаться выше у потребителей, чем на игры платформы ps 2, как более устаревшей модели и явно уступающей по качеству всего продукта более совершенным моделям.


## Часть 4 Введение в машинное обучение
Можно ли избавиться от "человеческого фактора" и определить ценность объекта автоматически, применив машинное обучение? В этом разделе будет дан ответ на этот вопрос.

### Проект 4: ML_recommendation_model_tariffs
Описание проекта

*Оператор мобильной связи Megaline выяснил, что многие клиенты пользуются архивными тарифами. Они хотят создать систему, способную анализировать поведение клиентов и предлагать пользователям новый тариф: "Умный" или "Ультра".*

**Получены следующие результаты работы:**
В проекте реализована идея, лежащая в основании машинного обучения - подготовлена модель, которая обучается методами классификации и анализирует поведение клиентов, предлагая пользователям новый тариф: "Умный" или "Ультра". 


### Проект 5: Отток клиентов (customer_outflow)
Описание проекта

*Из «Бета-Банка» стали уходить клиенты. Каждый месяц. Немного, но заметно. Банковские маркетологи посчитали: сохранять текущих клиентов дешевле, чем привлекать новых.
В проекте нужно спрогнозировать, уйдёт клиент из банка в ближайшее время или нет. В работе предоставлены исторические данные о поведении клиентов и расторжении договоров с банком.*

**Получены следующие результаты работы:**
- была проделана значительная работа в рамках знакомства с данными и ее предообработки, в результате получен датафрейм, который позволил провести дальнейшее исследование с чистыми данными на входе (принцип GiGo);
- построенны модели классификации на несбалансированных дынных, f1 демонстрирвал доастаточно низкие показатели. Известно, что метрика f1 помогает нам оценить производительность алгоритма. Это помогает нам оценить производительность модели обучения машины с точки зрения бинарной классификации; Нам нужно было достичь высокого балла f1, которая указала бы, что модель хорошо разбирается с точки зрения обращения с задачей дисбаланса класса;
- дальше пошагово в работе проведена балансировка моделей и определена лучшая - случайный лес с использованием метода upsampled;
- после проведения тестирования лучшая модель показала результат f1 - меры : 0.6391129032258065;
- в работе получена ROC кривая, это вертикальная линия от (0,0) до (0,1), которая тянется до (1,1). Это означает, что полученная модель всегда может различить положительные и отрицательные случаи;
- для задачи бинарной классификации достигнуто разумное значение AUC > 0.5, со значением 0.8684049061392587.

## Часть 5 Машинное обучение в бизнесе
В этой части будут представлены проекты, которые показывают как машинное обучение помогает бизнесу, а именно как запускать новую функциональность сервиса, применяя машинное обучение. Выясним, как собирать данные и как продуктовые метрики связаны с метриками машинного обучения.

### Проект 6: Выбор локации для скважины (choosing_the_location)
Описание проекта

*Допустим, вы работаете в добывающей компании «ГлавРосГосНефть». Нужно решить, где бурить новую скважину.Вам предоставлены пробы нефти в трёх регионах: в каждом 10 000 месторождений, где измерили качество нефти и объём её запасов. Постройте модель машинного обучения, которая поможет определить регион, где добыча принесёт наибольшую прибыль. Проанализируйте возможную прибыль и риски техникой Bootstrap.*

**Получены следующие результаты работы:**

В добывающей компании «ГлавРосГосНефть» в должности data scientist мной было бы предложено стейкхолдерам бурить новую скважину в Регионе № 2, обоснованием своей позиции я бы привел следующие аргументы:
- еще на предварительном осмотре данных тепловая карта показала, что коэффицент корреляции признака f2 в регионе № 2 имел абсолютное значение с целевым показателем - product;
- величина RMSE показала лучшее минимальное значение в Регионе № 2;
- ключевые показатели такие как средняя выручка относительно других регионов, квантиль выручки, доверительный интревал и наименьшее значение риска убытка совершенно показали лучшие результаты в Регионе № 2 чем и определили его выбор.

### Проект 7: Восстановление золота из руды (recovery_of_gold)
Описание проекта

*Компания разрабатывает решения для эффективной работы промышленных предприятий. Модель должна предсказать коэффициент восстановления золота из золотосодержащей руды. Используются данные с параметрами добычи и очистки. Модель поможет оптимизировать производство, чтобы не запускать предприятие с убыточными характеристиками.*

**Получены следующие результаты работы:**

Используя данные с параметрами добычи и очистки разработана Модель CatBoostRegressor, которая демонстрирует лучший результат и предсказывает коэффициент восстановления золота из золотосодержащей руды.

### Проект 8: Определение возраста покупателей (determining_age_buyers)
Описание проекта

*Сетевой супермаркет «Хлеб-Соль» внедряет систему компьютерного зрения для обработки фотографий покупателей. Фотофиксация в прикассовой зоне поможет определять возраст клиентов.*

**Получены следующие результаты работы:**

Решена задача в работе, а именно подготовлена модель, которая помогает определить возраст клиента, чтобы в последующем анализировать покупки и предлагать товары, которые могут заинтересовать покупателей этой возрастной группы, либо контролировать добросовестность кассиров при продаже алкоголя. Даже допуская ошибку в среднем 7 лет возрастные группы определить данная модель поможет. Безусловно определение в последующем возрастных групп является предметом отдельной не менее значимой работы. При желании качество модели можно улучшать и довести MAE < 5, но здесь существуют риски переобучения, что было бы не совсем правильно в рамках данного исследования.

## Часть 6 Выпускной проект "Телеком: исследование оттока клиентов" (graduation_project)

Описание проекта

*Необходимо построить прототип модели машинного обучения в телеком компании для прогнозирования оттока клиентов*

**Получены следующие результаты работы:**

В работе представлены следующие модели машинного обучения: RandomForestClassifier, CatBoostClassifier, LGBMClassifier,  SGDClassifier, LogisticRegression,  DummyClassifier. Лучший результат ROC-AUC_test 0.8950 показала модель LGBMClassifier.
