import os
import pickle

root_dir = os.path.dirname(os.path.realpath(__file__))


def save(slist: list, llist: list, clist: list):
    with open(os.path.join(root_dir, 'student.pkl'), "wb") as writer:
        pickle.dump(slist, writer)

    with open(os.path.join(root_dir, 'lecture.pkl'), "wb") as writer:
        pickle.dump(llist, writer)

    with open(os.path.join(root_dir, 'course.pkl'), "wb") as writer:
        pickle.dump(clist, writer)


def load():
    student_path = os.path.join(root_dir, 'student.pkl')
    lecture_path = os.path.join(root_dir, 'lecture.pkl')
    course_path = os.path.join(root_dir, 'course.pkl')
    slist, llist, clist = [], [], []
    if os.path.exists(student_path) and os.path.exists(lecture_path) and os.path.exists(course_path):
        if os.path.getsize(student_path) > 0:
            with open(os.path.join(root_dir, 'student.pkl'), "rb") as reader:
                slist = pickle.load(reader)

        if os.path.getsize(lecture_path) > 0:
            with open(os.path.join(root_dir, 'lecture.pkl'), "rb") as reader:
                llist = pickle.load(reader)

        if os.path.getsize(course_path) > 0:
            with open(os.path.join(root_dir, 'course.pkl'), "rb") as reader:
                clist = pickle.load(reader)

    return slist, llist, clist
