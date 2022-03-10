"""
OOP Example
1) Получившаяся структура является примером следующих трех принципов ООП:
    1. Агрегация - класс EducationalInstitution содержит поле students_list,
    являющееся коллекцией объектов другого класса - Student, к тому же студенты
    могут существовать отдельно от учебного заведения (поэтому агрегация)
    2. Наследование - классы School и Gymnasium наследуются от EducationalInstitution
    3. Абстракция - в классе EducationalInstitution выделена только та характеристика (students_list),
    которая важна в контексте решаемой задачи
2) Получившийся код является примером принципа полиморфизма - функция add работает по разному
в зависимости от класса объектов, для которых вызывается
3) Получившийся код является примером принципа инкапсуляции - метод __add__ включен в классы
и классы полностью контролируют своё поведение
"""


class Student:
    pass


class EducationalInstitution:

    def __init__(self, students_list: list[Student]):
        self.students_list = students_list

    def __add__(self, other):
        return EducationalInstitution(self.students_list + other.students_list)


def add(ei1: EducationalInstitution, ei2: EducationalInstitution) -> EducationalInstitution:
    if isinstance(ei1, School) and isinstance(ei2, School):
        return Gymnasium(ei1.students_list + ei2.students_list)
    if isinstance(ei1, Gymnasium) and isinstance(ei2, Gymnasium):
        return Gymnasium(ei1.students_list + ei2.students_list)
    return EducationalInstitution(ei1.students_list + ei2.students_list)


class School(EducationalInstitution):

    def __add__(self, other):
        if isinstance(other, School):
            return Gymnasium(self.students_list + other.students_list)


class Gymnasium(EducationalInstitution):

    def __add__(self, other):
        if isinstance(other, Gymnasium):
            return Gymnasium(self.students_list + other.students_list)
