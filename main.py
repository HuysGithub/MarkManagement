from data import data
from gui import loginGUI
from gui import adminGUI
from model.Student import Student

student_list, lecture_list, course_list = data.load()


def main():
    # student = Student("BA12-089","Nguyen Quoc Huy", "16-08-2003")
    # student_list.append(student)
    login_window = loginGUI.LoginWindow()

    if login_window.is_logged_in:
        if login_window.login_mode == "STUDENT":
            admin_window = adminGUI.AdminGui()

    data.save(student_list, lecture_list, course_list)


if __name__ == "__main__":
    main()
