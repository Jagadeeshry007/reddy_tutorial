import sys

students_data = {}


def enter_student_data():
    # Create one record
    student_record = {}
    name = input("Enter Student name: ")
    student_record["grade"] = int(input("Enter grade: "))
    student_record["science"] = int(input("Enter science mark: "))
    student_record["math"] = int(input("Enter math mark: "))
    student_record["average"] = (student_record["science"] + student_record["math"])/2
    students_data[name] = student_record
    print("Data entered successfully")
    print(f"Record - {students_data}")
    if(input("Add one more? [y/n]") == "y"):
        enter_student_data()
    else:
        return


if __name__ == "__main__":
    while True:
        option = input("Options: 1. Add data, 2. Remove data, Exit: 3: ")
        if option == "1":
            enter_student_data()
        elif option == "2":
            try:
                students_data.pop(input("Enter name of student record to be removed: "))
                print(f"Removed, Student record now - {students_data}")
            except KeyError:
                print("Entered student record does not exist")
            sys.exit()
        elif option == "3":
            print(f"existing student data is {students_data}")
            sys.exit()
