from data.file_path import FilePath
from data.load_data import SaveLoader

save_loader = SaveLoader()
student_list = save_loader.load_data(FilePath.STUDENT.value)
course_list = save_loader.load_data(FilePath.COURSE.value)
lecture_list = save_loader.load_data(FilePath.LECTURE.value)

for student in student_list:
    print(f"{student.name} - {student.id} - {student.dob}\n")
