# -*- coding: utf-8 -*-
'''
 1. Функция - создать список студентов
 2. Функция - Ждать 10 сек 
 3. Класс с методом, вызывающим п.1 1000р
 Задекорировать  пп.1-3 расчетом времени
 Прменение декораторов, пример
'''
from datetime import datetime
import time
studList = []

#Функция - декоратор
def calculateTime(func):
	def printTime(*args, **kwargs):
	    print datetime.now()
	    # в декорируемую функцию передаются аргументы
	    func(*args, **kwargs)
	    print datetime.now()

	return printTime

# Создание студента - добавление в список
@calculateTime # применение декортаора
def createStudents():
    studList.append('student')
 
# подождать 10 сек
@calculateTime
def wait10sec():
    time.sleep(10)

class 	NewClass():
    @calculateTime
    def myMethod(self, num):
        for i in range(num):
 	        createStudents()

wait10sec()
createStudents()
print studList

NewClass().myMethod(3)
print studList