from .StudentAspirant import StudentAspirant
from .StudentBachelor import StudentBachelor


def run():
    student1 = StudentAspirant('Vasya', '10', 4.5)
    student2 = StudentBachelor('Petya', '13', 5)
    print(student1.get_grant_value(), student2.get_grant_value())
    student1.update_average_grade(5)
    student2.update_average_grade(3.3)
    print(student1.get_grant_value(), student2.get_grant_value())


if __name__ == '__main__':
    run()
