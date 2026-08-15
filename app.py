mylist = {}

def grade(num):
    if num >= 93:
        return 'A'
    elif num >= 80:
        return 'B'
    elif num >= 70:
        return 'C'
    elif num >= 60:
        return 'D'
    else:
        return 'F'


while True:
    print("\n1.Add grade")
    print("2.Display students")
    print("3.Search student")
    print("4.Remove student")
    print("5.Statistics")
    print("6.Exit")

    op = int(input("Enter your choice: "))

    if op == 1:
        name = input("Enter the name: ")
        num = int(input("Enter the grade: "))
        mylist[name] = num
        print("Grade added successfully!")

    elif op == 2:
        if len(mylist) == 0:
            print("No students found.")
        else:
            print("\nStudents:")
            for name, num in mylist.items():
                print(f"{name}: {num} ({grade(num)})")

    elif op == 3:
        name = input("Enter the name: ")
        if name in mylist:
            print(f"{name}: {mylist[name]} ({grade(mylist[name])})")
        else:
            print("Student not found")

    elif op == 4:
        name = input("Enter the name: ")

        if name in mylist:
            mylist.pop(name)
            print("Student removed successfully!")
        else:
            print("Student not found")

    elif op == 5:
        if len(mylist) == 0:
            print("No data available.")
        else:
            grades = list(mylist.values())

            max_grade = max(grades)
            min_grade = min(grades)
            average = sum(grades) / len(grades)

            print("MAX:", max_grade)
            print("MIN:", min_grade)
            print("Average:", round(average, 2))

    elif op == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")