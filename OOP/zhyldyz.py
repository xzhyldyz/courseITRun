# class Phone:
#     def __init__(self, brand, memory, color):
#         self.brand = brand
#         self.memory = memory
#         self.color = color

#     def description(self):
#         # print("Бренд этого телефона - " + self.brand + ". Имеет " + str(self.memory) +  " ГБ памяти и цвет "+ self.color)
#         return f'Бренд этого телефона -: {self.brand} '

# Phone1 = Phone( "Айфон", 35, "белый" )


# Phone1.description() #вызов функции
# print(Phone1.brand)  # вызов свойства

# class Dog:
#     def __init__(self, name, age, color, weight):
#         self.n = name
#         self.a = age
#         self.c = color
#         self.w = weight

#     def sound(self):
#         return( "гав гав")
    

# dog = Dog( 'Жолборс', 3, 'Серый', ' 20кг')



# class Converse(sel)




# class Animal:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color

#     def info(self):
#         return f'{self.name} {self.age} {self.color}'
    
#     def change_age(self, age):
#         if self.age < 0 or self.age >20:
#             print('Мертвая собака')
#         self.age += 5
         
#     def reAge(self, NewAge):
#         if NewAge < 0 or NewAge > 20:
#             raise ValueError (' djvfbvvjbv')
#         else:
#             print()

    
        


# class Cat(Animal):
#     def sound(self):
#         return 'мяу мяу'
    
# class Dog(Animal):
#     def sound(self):
#         return 'гав гав'
    
# cat1 = Cat('Murzik', 2, 'orange')
# dog1 = Dog('Praim', 4, 'black')
# cat1.age = 10
# print(cat1.info())
# print(dog1.info())


#дополните нашу программу тем, чтобы добавить кошке и собаке такие данные  как damage(урон) и hp(health point)
#чтобы они могли драться, создаем методы get_damage  получение урона, в котором урон отнимает наш hp, 
# и  set_damage  




# x = 100
# x = x + 5
# x += 5



# a = 1,5,4
# print(a[1::])


# music = ['chandelier', 'Hello', 'Flower', 'Animal', 'La-la-la', 'lonely', 'Ocean eyes', 'Women', 'Traum','Believer']
# music[4:] = music[8:]
# print(music)


contact = ['Жылдыз', 'Кемел', 'Сезим', 'Мелена', 'Айлин']
inputNumber = int(input('Выберите действие: \n1 - искать контакт\n2 - добавлять контакт\n3 -удалить контакт\n'))
if inputNumber == 1:
    name = input('Ведите имя контакта: ').capitalize()
    if name in contact:
        print(name)
    else:
        print(' Такого контакта не существует.')
elif inputNumber == 2:
    name = input('Ведите имя контакта чтобы добавить: ').capitalize()
    if name in contact:
        print('Такой кантакт уже существует.')
    else:
        contact.append(name)
        print(contact)
elif inputNumber == 3:
    name = input('Ведите имя контакта чтобы удалить: ').capitalize()
    if name in contact:
        contact.remove(name)
        print(contact)
    else:
        print('Такого контакта и так не существует')

    








