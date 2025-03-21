# # #ООП- обьектно-ориентированное програмирование



# class Cat:
#     def __init__(self, name, age, color, paroda): # конструктор
#         self.name = name  #атрибуты класса
#         self.age = age  #атрибуты класса
#         self.color = color
#         self.paroda = paroda

#     def sound(self):
#         return 'мяу мяу'
    
#     def info(self):
#         return f'Имя: {self.name}, Возраст: {self.age}, {self.paroda} {self.color} Звук: {self.sound()}'
 
# cat = Cat('мурзик', 2, "черный", "Сиамская")
# cat2 = Cat('Moly', 1, "серая", "Британская")
# print(cat.age, cat.name, cat.sound())
# print(cat2.info())

 
# # #создать класс Car, с параметрами: ьренд, модель, год выпуска, владелец, владелец,
# # # is_going=False . Также у машины будет метод запуска машины


# class Car:
#     def __init__(self, brand, model, year, owner):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.owner = owner
#         self.is_going = False
#         self.speed = 0
    
#     def info(self):
#         return f'Бренд: {self.brand}, Модель: {self.model}, Год {self.year}, Владелец {self.owner}, Едет:{self.is_going}, со скоростью {self.speed} км\ч'
    
#     def start(self, newSpeedd):
#         self.is_going = True
#         self.speed = newSpeedd

#     # создать метод осьановки машины
#     # создать метод переименования модели и бренда

#     def stop(self):
#         self.is_going = False
#         self.speed = 0

#     def rename(self, name):
#         self.name = name


# car1 = Car('Mercedes-Benz','CLS II', 2020, 'Milena')
# car1.start(50)
# car1.stop()
# # car1.rename()
# print(car1.info())





class Purse:
    def __init__(self, valute, name="Неизвестный"):
        if valute not in ('KGS', 'USD'):
            raise ValueError('Только 2 валюты: KGS и USD')
        self.money = 0.00
        self.valute = valute
        self.name = name

# создать метод пополнение баланса
          # версия ассистента

    # def popolnenie (self):
    #     balance = input('Насколько  пополнить баланс')
    #     if balance > 0:
    #         self.money += balance
    #         print('ok')
    #         self.money + balance

            # версия ментора

    def up_balance(self, newM):
        self.money += newM
        return self.money

# создайте метод снятие суммы с кошелька
       # версия ассистента
#     def snyatie (self):
#         snyatie_summy = input('Сколько снять? ')
#         if snyatie_summy > 0:
#             self.money -= snyatie_summy
#             print('ok')
#             self.money - snyatie_summy

        # версия ментора
    def down_balance(self, newM):
        if self.money - newM < 0:
            raise ValueError(' У вас недостаточно средств')
        self.money = self.money - newM
        print('Успешный вывод')
        return self.money
    

    def info(self):
        return f'{self.name} у вас: {self.money} {self.valute}'

kuma = Purse('KGS', 'Kuma')
# print(kuma.money, kuma.valute, kuma.name)
kuma.up_balance(500)
kuma.down_balance(400)
print(kuma.info())





# class Cat:
# Домашка: Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. По умолчанию name = Ivan, ‍
# age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для‍
# получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения данных о номере группы ‍
# конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод ‍
# setGroupNumber позволяет изменить номер группы установленный по умолчанию. В программе необходимо создать пять ‍
# экземпляров класса Student, установить им разные имена, возраст и номер группы.

# class Student:
#     def __init__(self,name, groupNumber, age):
#         self.name = 'Ivan'
#         self.gN = '10A'
#         self.age = '18'

#     def getName(self):
#         return f'Имя студена {self.name}'
    
#     def getAge(self):
#         return f'Возраст студена {self.name}'
#     def getGroupNumber(self):
#         return f'Номер группы студена {self.name}'
    
#     def setNameAge(self, name, age):
#         self.name = name
#         self.age = age

#     def setGroupNumber(self,  groupNumber,):
#         pass

# Student1 = Student( 'Sara', '1A', 21)
# Student2 = Student( 'Adilet', '2A', 22)
# Student3 = Student( 'Sezim', '3A', 23)
# Student4 = Student( 'Mirlan', '4A', 24)
# Student5 = Student( 'Victor', '5A', 25)

# # print(Student1.name, Student1.age)
# print(Student1.setNameAge())






