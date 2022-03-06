"""
OOP Example
1) Получившаяся структура является примером следующих трех принципов ООП:
    1. Агрегация - класс EducationalInstitution содержит поле students_list,
    являющееся коллекцией объектов другого класса - Student, к тому же студенты
    могут существовать отдельно от учебного заведения (поэтому агрегация)
    2. Наследование - классы School и Gymnasium наследуются от EducationalInstitution
    3. Абстракция - в классе EducationalInstitution выделена только та характеристика (students_list),
    которая важна в контексте решаемой задачи
2) Получившийся код является примером принципа инкапсуляции - в классах School и Gymnasium
теперь появился метод (add), который вместе с полем образует одно целое
3) Получившийся код является примером принципа полиморфизма - оператор '+' возвращает
разный результат в зависимости от класса объекта, для которого он был вызвал
"""


class Student:
    pass


class EducationalInstitution:

    def __init__(self, students_list: list[Student]):
        self.students_list = students_list

    def __add__(self, other):
        return EducationalInstitution(self.students_list + other.students_list)


def add(ei1: EducationalInstitution,
        ei2: EducationalInstitution,
        cls=EducationalInstitution) -> EducationalInstitution:
    return cls(ei1.students_list + ei2.students_list)


class School(EducationalInstitution):

    def add(self, ei2: 'School') -> 'Gymnasium':
        if isinstance(ei2, School):
            return add(self, ei2, Gymnasium)

    def __add__(self, other):
        return School(self.students_list + other.students_list)


class Gymnasium(EducationalInstitution):

    def add(self, ei2: 'Gymnasium') -> 'Gymnasium':
        if isinstance(ei2, Gymnasium):
            return add(self, ei2, Gymnasium)

    def __add__(self, other):
        return Gymnasium(self.students_list + other.students_list)
