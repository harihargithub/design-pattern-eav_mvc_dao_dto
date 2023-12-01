import mysql.connector
from dto import StudentDTO


class StudentDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1504mysqlrp7@#",
            database="design_pattern",
        )
        self.cursor = self.connection.cursor()

    def add_student(self, student_dto):
        add_student_query = (
            "INSERT INTO students " "(school, student_name) " "VALUES (%s, %s)"
        )
        self.cursor.execute(
            add_student_query, (student_dto.school, student_dto.student_name)
        )
        self.connection.commit()

    def get_all_students(self, school):
        get_students_query = "SELECT student_name FROM students WHERE school = %s"
        self.cursor.execute(get_students_query, (school,))
        students = [StudentDTO(school, row[0]) for row in self.cursor.fetchall()]
        return students

    def delete_student(self, school, student_name):
        delete_student_query = (
            "DELETE FROM students WHERE school = %s AND student_name = %s"
        )
        self.cursor.execute(delete_student_query, (school, student_name))
        self.connection.commit()
