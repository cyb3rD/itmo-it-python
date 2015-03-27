# -*- coding: utf-8 -*-
# Init
studList = ["Bill Gates", "Jack", "John Cameron", "John Woo", \
            "James Goodwin", "Denzel Washington", "Jack Nicolson", "Arnold", "Jack"]
search = 'r'
# =======================
# Задание 1-2
# студент по индексу
# ========================
index = input(u'Введите индекс: ')
if index > len(studList) or index < 0:
    print u"Некорректный индекс!"
else:    
    print u"Элемент под номером " + str(index) + ": " + studList[index-1]
# ========================
# Задание 3
# список студентов
# ========================
start  = input(u'Введите начальный индекс: ')
end = input(u'Введите конечный индекс: ')
print studList[start-1:end]
# ========================
# Задание 4
# кол-во искомого символа в списке
# ========================
numOfStuds = 0

for stud in studList:
    if search in stud:
        numOfStuds += 1
print "\n" + str(numOfStuds) + u" раз(а) найден искомый символ: " + search
# ========================
# Задание 5
# Найти группы студентов с одинаковыми именами и создать списки этих групп
# ========================

studList.sort()            # сортируем  исходный список
# список, где каждый элемент список вида [имя, фамилия]
newList = [stud.split() for stud in studList ] 
# список имен студентов
nameList = [newList[i][0] for i in range(len(newList))]
tmpList = []                # список для хранения студентов с одинаковыми именами
equalList = []              # список для хранения групп студентов с одинаковыми именами
nameListLen = len(nameList) # кол-во элементов в списке имен
n = 0                       # начальный индекс для перебора элементов
counter = 0

while n < nameListLen:
    # подсчет кол-ва имен
    counter = nameList.count(nameList[n])
    # если больше 1
    if counter > 1:
        # индекс первого вхождения имени (нач.позиция)
        foundIndex = nameList.index(nameList[n]) 
        # во временный список пишем студентов с одинаковыми фамилиями
        tmpList.append(studList[foundIndex:foundIndex+counter])
        # в итоговый список в качестве элемента дописываем
        # список студентов с одинаковыми фамилиями
        equalList.append(tmpList)
    # увеличиваем индекс и обнуляем временный список
    n += counter
    tmpList = []
        
print "\n" + u"Списки студентов с одинаковыми именами:"
print equalList
