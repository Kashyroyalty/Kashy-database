from main import Student

our_students = Student.select()
for student in our_students:
    print(student.name, student.age, student.idnum, student.stream,student.gender)