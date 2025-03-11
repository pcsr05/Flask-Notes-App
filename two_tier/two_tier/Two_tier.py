import mysql.connector

# Function to connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Use your MySQL username
        password="password", # Use your MySQL password
        database="student_db"
    )

# Function to add a student
def add_student(name, grade):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, grade) VALUES (%s, %s)", (name, grade))
    conn.commit()
    conn.close()
    print("✅ Student added successfully!")

# Function to view students
def view_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()

    if not students:
        print("📭 No students found.")
    else:
        for student in students:
            print(f"🎓 ID: {student[0]} | Name: {student[1]} | Grade: {student[2]}")

# Function to update a student’s grade
def update_student(student_id, new_grade):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = %s WHERE id = %s", (new_grade, student_id))
    conn.commit()
    conn.close()
    print(f"🔄 Student ID {student_id} updated.")

# Function to delete a student
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    conn.close()
    print(f"🗑️ Student ID {student_id} deleted.")

# User Menu
while True:
    print("\n🎓 Student Management System")
    print("1️⃣ Add Student")
    print("2️⃣ View Students")
    print("3️⃣ Update Student Grade")
    print("4️⃣ Delete Student")
    print("5️⃣ Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        add_student(name, grade)
    elif choice == "2":
        view_students()
    elif choice == "3":
        student_id = input("Enter student ID to update: ")
        new_grade = input("Enter new grade: ")
        update_student(student_id, new_grade)
    elif choice == "4":
        student_id = input("Enter student ID to delete: ")
        delete_student(student_id)
    elif choice == "5":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again.")
