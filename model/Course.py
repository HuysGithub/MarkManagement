class Course:
    def __init__(self, id, name, student_list=None, lecture_list=None):
        self.id = id
        self.name = name
        self.students = student_list if student_list is not None else []
        self.lectures = lecture_list if lecture_list is not None else []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def add_student(self, student):
        self.students.append(student.id)
        self.save_to_db()

    def add_lecture(self, lecture):
        self.lectures.append(lecture.id)
        self.save_to_db()

    def get_lectures(self):
        return self.lectures

    def get_students(self):
        return self.students
