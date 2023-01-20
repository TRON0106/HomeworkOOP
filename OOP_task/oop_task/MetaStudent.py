class MetaStudent:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def _grant_process(self, min, mid, top):
        if self.average_grade == 5:
            return top
        elif 4 < self.average_grade < 5:
            return mid
        elif 3 < self.average_grade <= 4:
            return min

    def update_average_grade(self, value):
        if 0 <= value <= 5:
            self.average_grade = value
        else:
            raise ValueError
