# задание 1
import random

names1 = ''
names = ["пром", "агро", "торг", "урал", "север", "юг", "техно",
         "экспо", "метал", "нефть", "сельхоз", "фарм", "строй",
         "кредит", "алмаз", "-девелопмент", "развитие", "мос",
         "рос", "кубань", "сибирь", "восток", "нано", "софт",
         "микро", "онлайн", "инвест", "текстиль", "цемент"]
for x in range(6):
    names1 = names1 + random.choice(names)
print(names1)

# задание 2

def transliterate(string):
    slovar_lower = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'z', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': "'", 'ы': 'ii', 'ь': "'", 'э': 'e', 'ю': 'ju', 'я': 'ja'}
    slovar_upper = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'J', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Z', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ы': 'Ii', 'Э': 'E', 'Ю': 'Ju', 'Я': 'Ja'}

    text = ""

    for index, i in enumerate(string):
        if i in slovar_lower.keys():
            i = slovar_lower[i]
        elif i in slovar_upper.keys():
            i = slovar_upper[i]

        text += i

    return text
text2 = 'В наше время среди учёных нет точного ответа, является ли кошка полностью одомашненным животным, так как, ' \
        'например, собака в процессе одомашнивания изменила свою модель поведения, сумев развить довольно сильную ' \
        'привязанность и преданность к человеку и одновременно утратила множество способностей к охотничьему образу ' \
        'жизни и сигнальному общению, присущего его предкам — волкам. Кошка же по поведению почти не отличается от ' \
        'своего дикого предка, демонстрируя высокую независимость и повадки «одинокого хищника» Некоторые учёные ' \
        'считают, что кошка и вовсе не является одомашненным животным, а сама могла прийти к человеку, так как в ' \
        'селениях всегда в достатке водились синантропные животные или, проще говоря, многочисленные грызуны и' \
        ' птицы. ' \
        'Таким образом, кошка нашла для себя удобный источник пищи, закрепившись в «новой нише».' \
        ' Сосуществование человека и кошки было взаимовыгодным, так как человек избавлялся от грызунов, ' \
        'которые часто становились источником заболеваний и порчи хозяйства'
print(transliterate(text2))