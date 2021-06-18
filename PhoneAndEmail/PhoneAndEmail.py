#! Python
# Программа для нахождения номеров телефона и адресов электронной почты в тексте буфера обмена.

# Подключение необходимых библиотек
import pyperclip
import re

# объявление Regex для поиска
PhoneRegex = re.compile(r'''(
(\+7|8)?
(\s|-|\.)?
(\()?
(\d{3,4})
(\))?
(\s|-|\.)?
(\d{3})?
(\s|-|\.)?
(\d{2,3})
(\s|-|\.)?
(\d{2,3})
)''', re.VERBOSE)
EmailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE) 

text = str(pyperclip.paste()) # чтение буфера обмена
Finds = [] # объявление массива для занесения туда результатов
index = []

# поиск телефонных номеров
for group in PhoneRegex.findall(text):
    index.append("Найденный НОМЕР ТЕЛЕФОНА: ")
    Phone = ""

    Phone += group[1]
    Phone += " (" + group[4] + ") "
    if(group[7] != ""):
        Phone += group[7] + " "
    Phone += '-'.join([group[9], group[11]])
    Phone += "\n"

    Finds.append(Phone)

# поиск адресов эл.почты
for group in EmailRegex.findall(text):
    index.append("Найденный АДРЕС ЭЛ.ПОЧТЫ: ")
    Email = ""

    Email += group[0] + "\n"

    Finds.append(Email)

if(len(Finds) > 0):
    pyperclip.copy('\n'.join(Finds)) # копирование результатов в буфер обмена

    #вывод результатов в консоль
    print("Скопировано в буфер:\n")
    for i in range(len(Finds)):
        print(index[i] + Finds[i])
else:
    print("Номера телефонов и адреса электронной почты не обнаружены!") # если ничего не обнаружено