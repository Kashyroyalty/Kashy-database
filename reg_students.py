from main import Student

try:
    user_name = input("Enter name \n")
    user_age = input("Enter age \n")
    user_idnum = input("Enter idnum \n")
    user_stream = input("Enter stream \n")
    user_gender = input("Enter gender \n")

    Student.create(name =user_name, age = user_age, idnum = user_idnum,
                    stream = user_stream, gender = user_gender)
    print("Student Created Successfully")

except:
       print("Failed to create student use a different idnum")