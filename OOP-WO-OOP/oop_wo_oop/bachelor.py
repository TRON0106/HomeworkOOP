from .student import create_student, _get_grant


def create_bachelor(name, group, average_grade):
    return create_student(name, group, average_grade) | {
        'degree': 'bachelor'
    }

def get_bachelor_grant(bachelor):
    if bachelor.get('degree') != 'bachelor':
        raise ValueError
    return _get_grant(bachelor['average_grade'], 1500, 2000, 3000)