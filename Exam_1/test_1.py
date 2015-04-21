# -*- coding: utf-8 -*-
'''
Вывод информации о системе на экран:


Требования
1. Пройти все диски и все папки, полсчитать занятое место на дисках,
2. Подсчитать количество файлов каждого типа (расширения) и их часть 
    в занятом пространстве (построить таблицу по этим данным).
3. Для каждого диска - таблица с папками, сортируя по размеру от 
    большего к меньшему. Перечисляет самые частые 5 типов файлов. 
    Если есть еще, то отображает многоточие.
4. В начале отчета название отчета с временем начала анализа и 
    временем окончания. Также вывести время самого анализа
    в отформатированном виде.
5.	Пишет на экран отчет в табличной форме.
6.	Сохраняет этот же отчет в текстовый файл.

'''

import os, re

def getDisks ():
    '''
    Получение списка дисков системе
    '''
    listOfDisks = re.findall(r"[A-Z]+:.*$",os.popen("mountvol /").read(),re.MULTILINE)
    formattedList = []
    for disk in listOfDisks:
        formattedList.append(disk[:2])
    return formattedList, listOfDisks

disks = getDisks()[1] #список дисков

print disks

start_path = 'd:'
extDict = {} # extension: num of files

def getDirs (basedir="C:\\"):
    '''
    Получение списка каталогов для диска
    '''
    # список файлов в подкаталоге basedir
    # ToDo:
    # обработать исключение на windowsError 
    
    subnames = os.listdir(basedir)
    #список каталогов
    dirnames = []
    for name in subnames:
        if os.path.isdir(os.path.join(basedir, name)):
            dirnames.append(name)
            #print "[%s]" % name
    return dirnames


def getExtensions(fileName):
    '''
    Формирование словаря: {расширение:кол-во файлов}
    '''
    pass
    
def getSize(diskName):
    '''
    Подсчет занятого места
    '''
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(diskName):
        for f in filenames:
            # ToDo: формирование словаря с расширением и кол-вом файлов
            #расширение файла - последние 3 символа в имени
            extension = f[-3:] 
            # Сравниваем значение расширения в словаре (в виде ключа)
            if extDict.get(extension) == None:
                #Если ключа нет - новый ключ со значением 1
                #dict2 = {extension:1}
                extDict.update({extension:1})
            else:
                #если ключ есть, то инкремент его значение на +1
                extDict[extension] += 1
            fp = os.path.join(dirpath, f)
            # прибавление размера файла к общему счетчику
            total_size += os.path.getsize(fp)
    # Возвращаем объем занятого места на диске
    return total_size, extDict
'''
size = get_size(start_path)[0]
print "Размер каталога/диска: " + start_path  + str(size) + " байт"
print "словарь с данными по расширениям: "
#сортировка словаря
#список значений, их сортировка, получение ключей для первых 5ти значений
# sorted(extDict.items(), key=lambda (k, v): v, reverse=True)
print extDict['exe']
'''
'''
for d in disks:
    print getDirs(d)
'''
print getDirs('c:\\')