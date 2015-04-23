# -*- coding: utf-8 -*-
import disktools as dt, time
'''
Вспомогательные функциии:
timer(f) - декоратор для подсчета общего времени анализа всех дисков
sortDict(myDict) - сортировка словаря по значению
formatSize(num) - форматирование размера файла (Гб, Мб, Кб) 
reportHeader(resFile, disk) - вывод заголовка отчета
reportFooter(resFile, disk, startTime) - вывод времени анализ каждого диска
printDirInfo(resFile, disk) - вывод сведений о каталогах
printExtInfo(resFile, disk) - вывод сведений о расширениях
'''

def timer (f):
    '''
    подсчет времени (декоратор)
    '''
    def tmp(*args, **kwargs):
        t = time.time()
        res = f (*args,**kwargs)
        print "Общее время выполнения анализа: %3.3f сек." % (time.time()-t)
        return res
    return tmp
    
def sortDict(myDict):
    '''
    сортировка словаря по значению
    '''    
    dataList = list(myDict.items())
    dataList.sort(key = lambda item: item[1])
    return dataList
    
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
        
def reportHeader(resFile, disk):
    '''
    Заголовок отчета
    '''
    print '='*50
    print >> resFile, '='*50
    print 'Диск: ' + disk + ' : '
    print >> resFile, 'Диск: %s ' % disk
    #сведения о диске
    dirSize = formatSize(dt.getSize(disk))
    print >> resFile, '\nВсего занято: %4.3f %s' % (dirSize[0], dirSize[1])
    print 'Всего занято: %4.3f %s' % (dirSize[0], dirSize[1])
        
def reportFooter(resFile, disk, startTime):
    '''
    Вывод времени анализа каждого диска
    '''
    stopTime = time.time()
    print "\nВремя анализа диска %s: %3.3f сек." % (disk,(stopTime-startTime))
    print >> resFile, "\nВремя анализа диска %s: %3.3f сек." % (disk,(stopTime-startTime))
    
def printDirInfo(resFile, disk):
    '''
    Вывод сведений о каталогах
    '''
    # список каталогов
    myDirs = dt.getDirs(disk)
    # словарь {каталог: размер}
    dataDict = dict.fromkeys(myDirs) 
    for d in myDirs:
        dataDict[d] = dt.getSize(disk+d)
        
    #список отсортированных каталогов
    dataList = sortDict(dataDict)
        
    # вывод каталогов, отсортированных по размеру с форматированием
    print "Каталоги, отсортированные по размеру: "
    print >> resFile, "Каталоги, отсортированные по размеру: "
        
    for element in dataList[::-1]:
        sizeOfFolder = formatSize(element[1])# (Размер, ед.измерения)
            
        print '\%s Размер: %4.3f %s' % (element[0], \
                                            sizeOfFolder[0], sizeOfFolder[1])
        print >> resFile, '\%s Размер: %4.3f %s' % (element[0], \
                                            sizeOfFolder[0], sizeOfFolder[1])
    
def printExtInfo(resFile, disk):
    '''
    Вывод сведений о расширениях
    '''
    #отсортированный список расширений
    extList = sortDict(dt.getExts({},disk))
        
    # вывод 5ти самых частых расширений
    print "\nСамые распространенные файлы:"
    print >> resFile, "\nСамые распространенные файлы:"
    for i in range (5):
        print '*%s : %d файлов' % extList[::-1][i]
        print >> resFile, '*%s : %d файлов' % extList[::-1][i]