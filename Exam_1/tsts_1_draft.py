# -*- coding: utf-8 -*-

# ToDo:
# Расчет времени - декраторами
# Использование, подключение модулей
# Обработка WindowsError при попытке чтения содержимого локального диска из списка
# Запись сведений в файл

import os, time
total_size = 0
diskName = 'd:\\'
extDict = {}
basedir = 'D:\\'

def timer (f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f (*args,**kwargs)
        print "Время выполнения анализа: %f" % (time.time()-t)
        return res
    return tmp
    


def getDirs (basedir):
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
            dirnames.append(basedir + name)
            #путь с именем диска
    return dirnames


def getSize(dirName):
    '''
    Подсчет занятого места
    '''
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dirName):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # прибавление размера файла к общему счетчику
            total_size += os.path.getsize(fp)
    # Возвращаем объем занятого места на диске
    return total_size


def getExts(diskName):
    '''
    Получение словаря {расширение: кол-во файлов}
    '''
    for dirpath, dirnames, filenames in os.walk(diskName):
        for f in filenames:
            extension = f[-3:] 
            # Сравниваем значение расширения в словаре (в виде ключа)
            if extDict.get(extension) == None:
                #Если ключа нет - новый ключ со значением 1
                extDict.update({extension:1})
            else:
                #если ключ есть, то инкремент его значение на +1
                extDict[extension] += 1
    # Возвращаем словарь с расширениями
    return extDict

def formatSize(num):    
    '''
    форматированный вывод размера
    '''
    if num > 1024 and num < 1024**2:
        return ((num/1024.0),'Кб')
    elif num < 1024**3:
        return ((num/1024.0**2), 'Мб')
    else:
        return ((num/1024.0**3), 'Гб')

#начало анализа
startTime = time.time()
        
myDirs = getDirs(basedir)
print "Диск: " + basedir + " : "

dirSize = formatSize(getSize(basedir))
print 'Всего занято: %4.3f %s' % (dirSize[0], dirSize[1])

# словарь {каталог: размер}
dataDict = dict.fromkeys(myDirs) 
for d in myDirs:
    dataDict[d] = getSize(d)

# сортировка словаря по значениям
dataList = list(dataDict.items())
dataList.sort(key = lambda item: item[1])

# вывод каталогов, отсортированных по размеру с форматированием
print "Каталоги, отсортированные по размеру: "
for element in dataList[::-1]:
    dirSize = formatSize(getSize(element[0]))
    print 'Каталог: %s Размер: %4.3f %s' % (element[0], dirSize[0], dirSize[1])

# вывод 5ти самых частых расширений
extDict = getExts(basedir)
extList = list(extDict.items())
extList.sort(key = lambda item: item[1])
print "\nСамые распространенные файлы:"
for i in range (5):
    print '*.%s : %d файлов' % extList[::-1][i]

#конец анализа
stopTime = time.time()
print "\n Время анализа: %3.3f сек." % (stopTime-startTime)  