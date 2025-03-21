# Наследственность
# Инкапсуляция
    #  public - публичный 
    #  protected - защищеный _
    # private - приватный __

class Animal():  # родительский класс
    def __init__(self, name, age, color, hp = 100, damage= 0):
        self.name = name
        self.__age = age
        self.color = color
        self.hp = hp
        self.damage = damage

    def set_damage(self):
        return self.damage
    
    def get_damage(self, value):
        self.hp -= value

    def info(self):
        return f"{self.name} {self.__age} {self.color}"
    
# # Создайте метод изменине возраста у кошки и собаки
#     def reAge(self, newAge):
#         if newAge < 0 or newAge > 20:
#             raise ValueError("Возраст только от 1 до 20")
#         else:
#             self.__age = newAge
    @property  # с помощью декоратора property мы можем получать значения
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value > 0 and value < 21:
            self.__age = value

class Cat(Animal):   # дочерний класс
    def sound(self):
        return "мяу мяу"
    
    def get_damage(self, value):
        super().get_damage(value)
        print(f'ах ты собака сутулая! У меня осталось hp: {self.hp}')
    
class Dog(Animal):   # дочерний класс
    def sound(self):
        return "гав гав"
    
    def get_damage(self, value):
        super().get_damage(value)  # это строка наследует все из медота родительского класса
        print(f'Блохастый кошак! У меня осталось hp: {self.hp}')
        
cat1 = Cat("Murzik", 2, 'orange', damage=20)
dog1 = Dog("Praim", 4, 'black', damage=30)
# cat1.age = 19 
# print(cat1.age)
print(cat1.info())
print(dog1.info())
cat1.get_damage(dog1.set_damage())
dog1.get_damage(cat1.set_damage())


# Задание 2
# Дополните нашу программу тем, чтобы добавить кошке и собаке такие данные как damage(урон) и hp(health point), чтобы они могли драться, создаем методы get_damage получение урона, в котором урон отнимает наш hp, и set_damage когда мы этот урон наносим. Если у животного будет меньше 0 hp  то он умер и больше нельзя  наносить урон.

# примечание ментора: здесть не нужны гетторы или сетторы. И проперти тоже не используем.




# Задача 3: Симулятор библиотеки 
# создать класс Book, с атрибутами:  title (название книги, строка), author (автор книги, строка), year (год издания, число), is_available (доступна ли книга для выдачи, булево, по умолчанию True).
#  Методы: 
#     borrow(): если книга доступна, отмечает её как взятую (is_available = False) и возвращает сообщение: "Вы взяли книгу <название>". Если недоступна, выводит: "Книга <название> сейчас недоступна.".
#  return_book(): отмечает книгу как доступную (is_available = True) и выводит: "Книга <название> возвращена.".
# создать класс Library, с атрибутами:
#  books (список объектов класса Book).
#  Методы:add_book(book): добавляет книгу в библиотеку.
#  remove_book(title): удаляет книгу по названию (если она есть в библиотеке).
#  list_available_books(): выводит список всех доступных книг с их названиями и авторами.
#  find_book(title): ищет книгу по названию и выводит информацию о ней (название, автор, год, доступность).

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f'Взяли книгу {self.title}'
        else:
            return f"Книга {self.title} недоступна"
        
    def return_book(self):
        self.is_available = True
        return f" Книга {self.title} возвращена"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга {book.title} добавлена в библиотеку')
        
        
book1 = Book()
book1.borrow()
print(book1.borrow)