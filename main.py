from dao import StudentDAO
from dto import StudentDTO

student_dao = StudentDAO()

student1 = "Lary"
student2 = "Mike"
school = "School:Hindenburg"

stud1 = StudentDTO(school, student1)
stud2 = StudentDTO(school, student2)

student_dao.add_student(stud1)
student_dao.add_student(stud2)

# Delete student "Lary" from "School:Hindenburg"
# student_dao.delete_student(school, studentx)

student_names = student_dao.get_all_students("School:Hindenburg")
print(student_names)
