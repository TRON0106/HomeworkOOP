from .MetaStudent import MetaStudent

class StudentBachelor(MetaStudent):
    def get_grant_value(self):
        return self._grant_process(3500, 4500, 5000)
