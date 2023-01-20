from .MetaStudent import MetaStudent


class StudentAspirant(MetaStudent):
    def get_grant_value(self):
        return self._grant_process(1500, 2000, 3000)
