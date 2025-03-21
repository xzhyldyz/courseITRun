# Создать класс Student, который моделирует студента, его учебные достижения и готовность к работе. Студент имеет следующие характеристики:
# name, lastname, books(список): список книг, которые сдутент прочитал.
# knowledge (целое число): количество баллов знаний, которые накапливаются с течением времени.
# is_ready_to_work (булев тип): флаг, который указывает, готов ли студент к работе. Language (словарь): словарь, в котором ключ - это название языка прог
# Методы:
# add_points увеличивает количество знаний студента на заданное количество баллов. Если баллы превышают 1000, студент становиться готовым к работе.
# read_book добавляяет книгу в список прочитанных книг и увеличивает знания студента на 100 баллов за каждую прочитанную книгу.
# do_homework студент выполняет домашнее задание, увеличивает свои знания на 10 баллов.
# do_project студент выполняет проект, увеличивая свои знания на 50 баллов.
# learn_new_language студент изучает новый язык прог, увеличивая знания на количество баллов.
# info_about выводит инфо о студенте: его имя, фамилию, список прочитанных книг, количество знаний, готовность к работе и изученные языки.

# class  Student:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#         self.books = []
#         self.knowledge = 0
#         self.is_ready_to_work = False
#         self.languages = {}

#     def add_points(self, points):
#         self.knowledge += points
#         if self.knowledge >= 1000:
#             print('готов к работе')
#             self.is_ready_to_work = True 

#     def read_book(self, book):
#         self.books.append(book)
#         self.add_points(100)

#     def do_homework(self):
#         self.add_points(10)

#     def do_project(self):
#         self.add_points(50)
  
#     def learn_language(self, lang, points):
#         if points < 1 or points > 100:
#             raise ValueError
#         else:
#             self.languages[lang] = points
#             self.add_points(points)

#     def info_about(self):
#         return f"Меня зовут  {self.name} {self.lastname}\nЯ прочитал: {self.books}\nМои баллы:{self.knowledge}\nЯ знаю: {self.languages}\nГотовность к работе: {self.is_ready_to_work}"
    
# kuma = Student('Kuma','Baltozar')
# kuma.read_book('Основы веб разработки')
# kuma.read_book('Python 2023')
# kuma.read_book('Чистая архитектура')
# kuma.read_book('Основы JS')

# kuma.do_homework()
# kuma.do_homework()

# kuma.do_project
# kuma.do_project
# kuma.do_project

# kuma.learn_language('JS', 100)
# kuma.learn_language('Python', 100)
# kuma.learn_language('HTML', 50)
# kuma.learn_language('CSS', 50)
# kuma.learn_language('Bootstrap 4', 100)
# kuma.learn_language('Django', 100)
# kuma.learn_language('SQL', 100)

# print(kuma.info_about())





















