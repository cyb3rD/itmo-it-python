# -*- coding: utf-8 -*-
import disktools as dt, formattools as ft, time, os
'''
Вывод отчета по файловой системе
Требования:
1. Пройти все диски и все папки, полсчитать занятое место на дисках,
2. Подсчитать количество файлов каждого типа (расширения) и их часть 
    в занятом пространстве (построить таблицу по этим данным).
3. Для каждого диска - таблица с папками, сортируя по размеру от 
    большего к меньшему. Перечисляет самые частые 5 типов файлов. 
    Если есть еще, то отображает многоточие.
4. В начале отчета название отчета с временем начала анализа и 
    временем окончания. Также вывести время самого анализа
    в отформатированном виде.
5.  Пишет на экран отчет в табличной форме.
6.  Сохраняет этот же отчет в текстовый файл.
'''

# Файл с отчетом
fName = os.path.join(os.getcwd(),'report.txt')
resultFile = open(fName, 'w')

@ft.timer
def printReport():
    # Получаем список дисков
    disks = dt.checkDisks(dt.getDisks()[1])
    # Анализ каждого диска
    for disk in disks:
        print "Приступаем к анализу диска %s ..." % disk
        # Временная метка начала анализа диска
        startTime = time.time()
        # Выводим шапку отчета
        ft.reportHeader(resultFile, disk)
        # Вывод данных о каталогах диска
        ft.printDirInfo(resultFile, disk)
        # Вывод данных о расширениях
        ft.printExtInfo(resultFile, disk)
        #Вывод времени анализа
        ft.reportFooter(resultFile, disk, startTime)
        
    #Закрытие файла
    resultFile.close()
    print "\n Расположение файла с отчетом: %s" % fName

if __name__ == "__main__":
    printReport()