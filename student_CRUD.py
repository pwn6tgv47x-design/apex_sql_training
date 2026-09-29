import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sec@123",
    database="studentdb"
)

cursor = db.cursor()

print("Successfully connected")



while True:
    print("===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!\n")


# Close connection
cursor.close()
db.close()





