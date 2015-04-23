# -*- coding: utf-8 -*-

# ToDo:
# Расчет времени - декраторами
# Использование, подключение модулей
# Обработка WindowsError при попытке чтения содержимого локального диска из списка
# Запись сведений в файл

import os, time, re

# возможно для использования в качестве декоратора
def timer (f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f (*args,**kwargs)
        print "Время выполнения анализа: %f" % (time.time()-t)
        return res
    return tmp

def getDisks ():
    '''
    Получение списка дисков системе
    '''
    listOfDisks = re.findall(r"[A-Z]+:.*$",os.popen("mountvol /").read(),re.MULTILINE)
    formattedList = []
    for disk in listOfDisks:
        formattedList.append(disk[:2])
    return formattedList, listOfDisks

def checkDisks(disks):
    correctDiskList = []
    for d in disks:
        print "getDirs for disk %s" % d
        if getDirs(d) == []:
            pass
        else:
            print "Ok!"
            correctDiskList.append(d)
    return correctDiskList

def getDirs (basedir="C:\\"):
    '''
    Получение списка каталогов для диска
    '''
    # список файлов в подкаталоге basedir
    # обработка исключение на windowsError 
    subnames = []
    #список каталогов
    dirnames = []
    try:
        subnames = os.listdir(basedir)
    except OSError as e:
        print "Ошибка доступа к диску %s " % basedir
        print "Код ошибки: %s" %e.errno 
        return []
   
    for name in subnames:
        if os.path.isdir(os.path.join(basedir, name)):
            dirnames.append(name)
            #print "[%s]" % name
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
    extDict = {}
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

def printReport():
    
    #Формирование отчета 

    #список дисков
    disks = checkDisks(getDisks()[1])
    #print disks
    #анализ каталогов для каждого диска
    for disk in disks:
        #начало анализа
        startTime = time.time()
        #шапка отчета
        myDirs = getDirs(disk)
        print "Диск: " + disk + " : "

        dirSize = formatSize(getSize(disk))
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
            #begin test output
            print element
            dirSize = getSize(element[0])
            #end test output
            print 'Каталог: %s Размер: %f' % (element[0], dirSize)
            #dirSize = formatSize(getSize(element[0]))
            #print 'Каталог: %s Размер: %4.3f %s' % (element[0], dirSize[0], dirSize[1])

        # вывод 5ти самых частых расширений
        extDict = getExts(disk)
        extList = list(extDict.items())
        extList.sort(key = lambda item: item[1])
        print "\nСамые распространенные файлы:"
        for i in range (5):
            print '*.%s : %d файлов' % extList[::-1][i]
    
        #Вывод времени анализа
        stopTime = time.time()
        print "\n Время анализа диска %s: %3.3f сек." % (disk,(stopTime-startTime))


printReport()


    
#список дисков
#disks = getDisks()[1] 
#print disks
'''
disks = checkDisks(getDisks()[1])
print disks
 
for d in disks:
    #временная метка начала
    startTime = time.time()   
    print "Диск: " + d + " : "
    myDirs = getDirs(d)
    print myDirs
    #print getSize(d)
    dirSize = formatSize(getSize(d))
    print 'Всего занято: %4.3f %s' % (dirSize[0], dirSize[1])
    #Вывод времени анализа
    stopTime = time.time()
    print "\n Время анализа: %3.3f сек." % (stopTime-startTime)


#анализ каталогов для каждого диска
for d in disks:
    #шапка отчета
    myDirs = getDirs(d)
    print "Диск: " + d + " : "

    dirSize = formatSize(getSize(disk))
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
    
#Вывод времени анализа
stopTime = time.time()
print "\n Время анализа: %3.3f сек." % (stopTime-startTime)
'''