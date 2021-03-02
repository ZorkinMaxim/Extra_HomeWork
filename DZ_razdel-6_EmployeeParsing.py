# Создать класс Employee, который принимает имя, фамилию и зарплату в качестве аргументов при конструировании.
# Класс должен поддерживать:
# атрибут first_name, возвращающий имя
# атрибут last_name, возвращающий фамилию
# атрибут salary, возвращающий зарплату
# функцию from_string, которая принимает имя, фамилию и зарплату в формате 'first_name-last_name-salary',
# парсит строку и возвращает экземпляр Employee.

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, str_to_parse):
        first_name, last_name, salary = str_to_parse.split('-')
        return cls(first_name, last_name, int(salary))


emp = Employee.from_string('John-Smith-55000')
print(emp.first_name)
print(emp.last_name)
print(emp.salary)

emp2 = Employee('Mary', 'Sue', '60000')
print(emp2.first_name)
print(emp2.last_name)
print(emp2.salary)

