# -*- coding: utf-8 -*-
import random
# Базовый класс живтоного
class Animal(object):
	id = 0
	# Словарь для хранения продукции в виде {продукт: кол-во}
	products = {}
	# Цена животного
	priceOfAnimal = 0
	
	def __init__(self):
		pass
	# Сколько съедено
	def food(self):
		pass
	# Сколько произведено продукта
	def product(self):
		pass
	# Месяц спустя
	def monthLater(self):
		pass	
# Утка
class Duck(Animal):
	# инициализация словаря с видами продуктов
	def __init__(self):
		self.products = dict.fromkeys(('eggs', 'meat'))
		self.id += 1
	# для каждого продукта заполняется его кол-во "на складе"
	def monthLater(self):
		for p in self.products:
			self.products[p] = int(random.random()*100)

# Корова
class Cow(Animal):
	# инициализация словаря с видами продуктов
	def __init__(self):
		self.products = dict.fromkeys(('milk', 'meat'))
		self.id += 1
	# для каждого продукта заполняется его кол-во "на складе"
	def monthLater(self):
		for p in self.products:
			self.products[p] = int(random.random()*100)
	
# Свинья
class Pig(Animal):
	# инициализация словаря с видами продуктов
	def __init__(self):
		self.products = {'meat':None}
		self.id += 1
	# для каждого продукта заполняется его кол-во "на складе"
	def monthLater(self):
		for p in self.products:
			self.products[p] = int(random.random()*100)
	
# ФЕРМА
class FunFarm(object):
	# словарь для хранения животных
	animals = {}
	# название фермы
	nameOfFarm = ""
	# текущий день
	currentDay = 0
	def __init__(self, name="UnReal Farm", ducks=3, cows=4, pigs=5):
	       self.nameOfFarm = name
	       self.animals = dict.fromkeys(('Duck','Cow','Pig'))
	       # создать кол-во объектов и записать их в словарь
	       self.addAnimal('Duck', ducks)
	       self.addAnimal('Cow', cows)
	       self.addAnimal('Pig', pigs)

	def addAnimal(self, id, num):
		#добавление списка объектов животных в словарь
		listOfAnimals = []
		for i in range(num):
			if id == 'Duck':
				listOfAnimals.append(Duck())
			elif id == 'Cow':
				listOfAnimals.append(Cow())
			else:
				listOfAnimals.append(Pig())
		
		self.animals[id] = listOfAnimals

	def monthLater(self):
	    self.currentDay = 30
	    # Вызов метода для каждого созданного ранее объекта
	    for typeOfAnimal in myFarm.animals.keys():
		for obj in myFarm.animals[typeOfAnimal]:
			obj.monthLater()
			print obj.products

	def totalInfo(self):
		print u"Текущий день: " + str(self.currentDay)
		print u"Cводка: "
		# Кол-во животных | Вид продукции / кол-во | Стоимость животного

# Инициализация фермы
myFarm = FunFarm()
# Вывод информации о состоянии дел
myFarm.totalInfo()
# Прошел месяц
myFarm.monthLater()
# вывод информации о состоянии дел
myFarm.totalInfo()


print myFarm.animals


