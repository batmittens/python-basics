# задание 1

numbers = [2,6,7,45,1,89,678,35]
for i in numbers:
    if i %5 == 0:
        print(i,'делится на 5')
        if i == 45:
            continue

        break
    else:
        print(i,"не делится на 5, продолжим поиск")

# задание 2
import random
cocktails = [["мартини","грейпфрутовый сок","жасмин","тоник","лосось"],
               ["клубника","какао","мята","марсала"],
               ["водка","томатный сок","лимонный сок","вустерширский соус","черный перец","сельдерей","лосось"],
               ["джин","вермут","ликер мараскино","апельсины","коктейльная вишня","лосось"],
               ["ром","авокадо","сахарный сироп","сливки","лимонный сок","лед"],
               ["красный вермут","тоник","апельсины","лосось"],
               ["только чай"]
        ]
for i in cocktails:
    for b in i:
     if b == 'лосось':
      i.remove(b)
print('Сегодня в вашем коктейле будет: ', random.choice(cocktails))