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
if numOfStuds:
    print "\n" + str(numOfStuds) + u" раз(а) найден искомый символ: " + search
else:
    print u"\nИскомый символ: " + search + u" не найден!"
# ========================
# Задание 5
# Найти группы студентов с одинаковыми именами и создать списки этих групп
# ========================
studList.sort()            # сортируем  исходный список
# список (элемент список вида [имя, фамилия])
newList = [stud.split() for stud in studList ] 
# список ВСЕХ имен студентов
nameList = [newList[i][0] for i in range(len(newList))]
# множество - список имен (без повторений)
nameSet = set(nameList)
# словарь {имя_студента: полные ФИО для одинаковых имен}
studDict = dict.fromkeys(nameSet) 

# ===================================
# Функция для вывода списка студентов:
# ==================================
def strDoubleStudents (listLen, nameList, isSet=True):
    # начальный индекс для перебора элементов
    n = 0                      
    # цикл по кол-ву имен в списке имен
    while n < listLen:
        # подсчет кол-ва имен
        counter = nameList.count(nameList[n])
        # если больше 1
        if counter > 1:
            # находим индекс первого вхождения имени (нач.позиция) в списке имен
            foundIndex = nameList.index(nameList[n]) 
            # в словарь для ключа имя_студента пишем список с полными ФИО 
            # из исходного списка
            studDict[nameList[n]] = studList[foundIndex:foundIndex+counter]
        # увеличиваем индекс на кол-во найденных элементов
        n += counter
    if not isSet:   
        print u"\nСловарь со списками студентов с одинаковыми именами:"
        # вывод словаря без ключей с пустыми значениями (None)
        return {s:studDict[s] for s in studDict if studDict[s] != None}   
    else:
        print u"\nСловарь со списками студентов с в виде множества:"
        # вывод словаря без ключей с значениями (None) и значение в виде множества
        return {s:set(studDict[s]) for s in studDict if studDict[s] != None}  

#==============================================
# Вывод списка студентов с одинаковыми именами
# в зависимости от значения параметра isSet:
# либо в виде списка, либо в виде множетсва
#==============================================
print strDoubleStudents(len(nameList), nameList)