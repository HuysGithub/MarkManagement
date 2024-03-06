from .Course import Course


class Mark:
    def __init__(self, course: Course):
        self.course = course
        self.attendance = 0
        self.mid_term = 0
        self.final = 0
        self.finish_course = 0

    def add_attendance(self, attendance):
        self.attendance = attendance

    def add_mid_term(self, mid_term):
        self.mid_term = mid_term

    def add_final(self, final):
        self.final = final

    def calculate_finish_course(self):
        self.finish_course = self.attendance * 0.1 + self.mid_term * 0.4 + self.final * 0.5
