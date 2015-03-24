# -*- coding: utf-8 -*-
'''
1. Найти в данной папке все файлы, в тексте которых содержится слово python,
 	и вывести на экран имена файлов.
2. Посчитать общее количество найденных слов и вывести на экран.
3. Записать в файл "result.txt" список найденных файлов 
	и число найденных слов python
'''
import os
sourceDir = "D:\\TestDir" # For example: os.getcwd()
resultFile = sourceDir + "\\result.txt"
dirList = os.listdir(sourceDir)
searchString = "python"
totalNumOfWords = 0
path = ""
files = ""

# Get list of files in directory sourceDir
for e in dirList:
    path = sourceDir + "\\" + e
    if os.path.isfile(path):
        files += path + " " 
fileList = files.split()

# Read each file (find and count searchString)
fw = open(resultFile,"w")
for f in fileList:
    numOfWordsInFile = 0
    fr = open(f)
    strFromFile = fr.read()
    numOfWordsInFile = strFromFile.count(searchString)
    fr.close()
    
    if numOfWordsInFile:
        output =  searchString + " FOUNDED " + str(numOfWordsInFile)\
        + " times in file: " + f
        print output
        fw.write(output+"\n")
        totalNumOfWords += numOfWordsInFile
    
if not totalNumOfWords:
    print searchString + " NOT FOUNDED in any file @ " + sourceDir
else:
    fw.write("Total " + searchString + " FOUNDED: " + str(totalNumOfWords))

fw.close()