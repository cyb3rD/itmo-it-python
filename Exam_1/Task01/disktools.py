# -*- coding: utf-8 -*-
import os,re
'''
Модуль с дополнительными функциями:
getDisks() - список дисков в системе
checkDisks(disks) - проверка дисков на доступность
getDirs (basedir="C:\\") - получение списка каталогов
getExts(extDict, diskName) - получение расширений и их кол-ва
getSize(dirName) - получение размера каталога
'''

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
        print "Проверка диска: %s" % d
        if getDirs(d) == []:
            print "Диск %s исключен из анализа." % d
        else:
            print "...Ok!"
            correctDiskList.append(d)
    return correctDiskList

def getDirs (basedir="C:\\"):
    '''
    Получение списка каталогов для диска
    '''
    #список каталогов
    subnames = []
    dirnames = []
    try:
        subnames = os.listdir(basedir)
    except OSError as e:
        print "Ошибка доступа к диску %s " % basedir
        print "Код ошибки: %s." %e.errno 
        return []
   
    for name in subnames:
        if os.path.isdir(os.path.join(basedir, name)):
            dirnames.append(name)
    return dirnames

def getExts(extDict, diskName):
    '''
    Получение словаря {расширение: кол-во файлов}
    '''
    for dirpath, dirnames, filenames in os.walk(diskName):
        for f in filenames:
            # Получаем расширение
            extension = os.path.splitext(f)[1] 
            # Сравниваем значение расширения в словаре (в виде ключа)
            if extDict.get(extension) == None:
                # Если ключа нет - новый ключ со значением 1
                extDict.update({extension:1})
            else:
                # Ключ есть: инкремент его значение на +1
                extDict[extension] += 1
    # Возвращаем словарь с расширениями
    return extDict


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

