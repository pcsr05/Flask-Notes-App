import sqlite3

# Connect to SQLite database (or create it if it doesn’t exist)
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

# Create a table for notes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
''')

# Function to add a note
def add_note(title, content):
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    print("✅ Note added successfully!")

# Function to view all notes
def view_notes():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    
    if not notes:
        print("📭 No notes found.")
    else:
        for row in notes:
            print(f"📝 ID: {row[0]} | Title: {row[1]} | Content: {row[2]}")

# Function to delete a note
def delete_note(note_id):
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    print(f"🗑️ Note ID {note_id} deleted.")

# User Menu
while True:
    print("\n📒 Personal Note-Taking App")
    print("1️⃣ Add Note")
    print("2️⃣ View Notes")
    print("3️⃣ Delete Note")
    print("4️⃣ Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        add_note(title, content)
    elif choice == "2":
        view_notes()
    elif choice == "3":
        note_id = input("Enter note ID to delete: ")
        delete_note(note_id)
    elif choice == "4":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again.")

# Close connection
conn.close()
1