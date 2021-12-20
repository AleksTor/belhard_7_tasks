"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: str
    average_score: float

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    '''equal - равно'''
    def __eq__(self, other):
        return self.average_score == other.average_score

    '''not equal - не равно'''
    def __ne__(self, other):
        return self.average_score != other.average_score

    '''less than - меньше чем'''
    def __lt__(self, other):
        return self.average_score < other.average_score

    '''greater than - больше чем'''
    def __gt__(self, other):
        return self.average_score > other.average_score

    '''less equal - меньше или равно'''
    def __le__(self, other):
        return self.average_score <= other.average_score

    '''greater equal - больше или равно'''
    def __ge__(self, other):
        return self.average_score >= other.average_score

    '''repr - ссылка на экземпляр, вызывается для получения формального предсавления объекта
    вовзращает значние str'''
    def __repr__(self):
        return f"\n Имя: {self.name} \n Фамилия: {self.surname} \n Группа: {self.group} "\
            f"Средний балл: {self.average_score}"


some_list = [
    Student("Петрошевич", "Петр", "гр.1", 9.99),
    Student("Сидоркевич", "Сергей", "гр.2", 8.88),
    Student("Алексашкин", "Александр", "гр.1", 4.44),
    Student("Фунтова", "Елизовета", "гр.2", 3.33),
    Student("Баксова", "Моника", "гр.1", 2.22)
]

'''Функция sorted возвращает сортированный список'''
print(sorted(some_list))
print(sorted(some_list, reverse=True))
''' создаем новый список, в котором будут только те, у кого балл выше 5'''
new_list = [student for student in some_list if student.average_score > 5]
print(new_list)
