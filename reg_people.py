from main import People

try:
    user_name = input("Enter name \n")
    user_phonenumber = input("Enter phonenumber \n")
    user_email = input("Enter email \n")
    user_county = input("Enter county \n")
    user_gender = input("Enter gender \n")
    user_religion = input("Enter religion \n")
    user_password = input("Enter password \n")


    People.create(name = user_name, phonenumber = user_phonenumber, email =user_email,
                  county = user_county, gender = user_gender, religion = user_religion,
                  password = user_password)

    print("Person successfully registered")

except:
    print("Failed to register person")

