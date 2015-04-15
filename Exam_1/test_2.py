


1. Даны 2 класса:

    class Bowling:
        pass

    class Tennis(object):
        pass


Отметьте верные утверждения:

- классы не созданы
- класс Bowling является "новым" классом, Tennis - "старым"
- в приведенном коде присутствует операция наследования
- классы одинаковые

2. Разрешается ли такое поведение?

    class Machine:
        pass

    m = Machine()
    m.description = 'Car'

- Да
- Нет
- Иногда


3. Чем принципиально отличаются (если отличаются) записи класса? Перечислите важные плюсы
    и минусы:


    class Point:
        x = 10
        y = 10

    class Point:

        def __init__(self):
            self.x = 10
            self.y = 10

4. Что произойдет в следующем программном коде:

    class Polygon:

        points = []

        def __init__(self, *args):
            self.points += args

    a = Polygon(7, 2, 33)
    b = Polygon(41, 4, 15)


- Произойдет ошибка. Какая?
- Содержимое points класса Polygon будет таким же, как и объекта a
- атрибут points объекта после выполнения конструктора пересоздается по
    новому адресу в памяти
- содержимое points объекта b = [7, 2, 33, 41, 4, 15]
- содержимое points объектов a и b одинаково

5. Выберите работоспособный вариант создания класса:

    1)

    class M:
        
        def __str__(self):
            return 'object M'
    
    def _rep(s):
        return 'M'
    
    M.__repr__ = _rep
    
    2)

    class M:

        def __str__(self):
            return 'object M'

        def __repr__(self):
            return 'M'

- 1
- 2

6. Сопоставьте действия выводу на экран при работе в интерактивном
    режиме интерпретатора:

    >>> class M:
    ... def __str__(self):
    ...     return 'object M'
    ...

    >>> M               # 1

    >>> M()             # 2

    >>> print M()       # 3

    >>> def rep(s):
    ...     return 'M'
    ...
    
    >>> M.__repr__ = rep
    >>>
    >>> M()             # 4




a) object M

b) M

c) <__main__.M instance at 0x10f26aa28>

d) <class __main__.M at 0x10f24f808>

e) Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
AttributeError: 'M' object has no attribute '__repr__'


7. Отметьте верные утверждения:

    class Object:
        size = (0, 0)

    class Engineering:
        structure = []

    class Car(Tech, Engineering):

        def __init__(self, name='Some car'):
            self.name = name

    c = Car()


- класс Car отнаследован от Tech и от Engineering
- множественное наследование в Python запрещено
- если под structure подразумевается структура конкретного объекта, то присутствует ошибка. Какая?
- объект c содержит поля size и structure
- класс Car содержит атрибут name


8. Дан следующий класс:

    class Polygon:
        def __init__(self, *args):
            self.points = args
            
        def find(self, p):
            for i, x, y in enumerate(args):
                if p.x == x and p.y == y:
                    return i
            return -1


    pol = Polygon(Point(), Point(), Point())
    print pol.find(Point())


    1) Напишите класс Point:




    2) Что будет выведено на экран?


9. Выберите правильный синтаксис:

    1)
    
    class Time:

        @staticmethod
        def now(self):
            pass

    2)
    
    class Time:
        
        @staticmethod:
        def now():
            pass
    
    3)
    
    class Time:

        def now(self):
            pass
        
    4)

    class Time:

        def now():
            pass
        
    5)

    class Time:
        
        @staticmethod
        def now():
            pass

10. Для чего используется декоратор staticmethod?


11. Перечислите функции для анализа объекта и опишите, какая используется для чего?


12. Что проверяет функция isinstance?


13. Какие вспоминаются варианты взаимоотношения классов (шаблоны проектирования), удобные в python?


13. Напишите свой вариант переопределения любого оператора.


14. Напишите свой вариант полезного декоратора и вариант применения.


15. Для чего нужен self? Что это на самом деле? Можно ли использовать "this" вместо "self"?


