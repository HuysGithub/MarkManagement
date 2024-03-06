from model.Student import Student
from model.Course import Course
from model.Lecture import Lecture


class AdminBackend:
    def __init__(self):
        pass

    def add_student(self, student: Student, student_list: list):
        student_list.append(student)
        return student_list

    def remove_student(student: Student, student_list: list):
        student_list.remove(student)
        return student_list

    def add_course(course: Course, course_list: list):
        course_list.append(course)
        return course_list

    def remove_course(course: Course, course_list: list):
        course_list.remove(course)
        return course_list

    def add_lecture(lecture: Lecture, lecture_list: list):
        lecture_list.append(lecture)
        return lecture_list

    def remove_lecture(lecture: Lecture, lecture_list: list):
        lecture_list.remove(lecture)
        return lecture_list
