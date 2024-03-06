import main


def verify_login(username, password):
    if username == 'admin' and password == 'admin':
        return True, "ADMIN"
    for student in main.student_list:
        if student.account.username == username and student.account.password == password:
            return True, "STUDENT"
    for lecture in main.lecture_list:
        if lecture.account.username == username and lecture.account.password == password:
            return True, "LECTURE"
    return False, None
