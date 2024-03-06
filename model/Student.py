import main
from model.Account import Account
from model.Mark import Mark


class Student:
    def __init__(self, id, name, dob, mark: list[Mark] = None, account: Account = None):
        self.id = id
        self.name = name
        self.dob = dob
        self.mark = mark
        self.account = account if account is not None else Account(self.id)
        main.student_list.append(self)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        self.dob = dob
