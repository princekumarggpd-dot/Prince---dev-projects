# Student Management System
students = {}
while True:
    print(''' 1. Enter Student
              2. Add Details
              3. View Student Info
              4. Remove Student
              5 . Exit ''')
    choice = int(input("Enter your choice : "))
    # 1. Enter student basic info
    if choice == 1:
        roll = int(input("Enter Roll Number:"))
        name = input("Enter Student Name: ")
        students.setdefault(roll,name)
        print("Student name added successfully !")
    elif choice == 2:
        roll = int(input("Enter Roll Number:"))
        if roll in students:
            age = int(input("Enter your Age: "))
            co = input("Enter your Course: ")
            students[roll]["Age"] = age
            students[roll]["Course"] = co
            print("Details of student added successfully !")
        else:
            print("Student not found")

    # 3. View student info
    elif choice == 3:
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student Information:")
            for key, value in students[roll].items():
                print(f"{key}: {value}")
        else:
            print("Student not found!")

    # 4. Remove student
    elif choice == 4:
        roll = input("Enter Roll Number: ")

        if roll in students:
            del students[roll]
            print("Student removed successfully!")
        else:
            print("Student not found!")

    # 5. Exit
    elif choice == 5:
        print("Exit sucessfully")
        break

    else:
        print("Invalid choice! Please enter 1-5")
    ch = input("want to continue (yes or no):").lower()
    if ch=="no":
        print("break successfully")
        break
         
     