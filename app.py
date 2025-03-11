import webbrowser
import threading
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Function to connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",  # Use 127.0.0.1 instead of "localhost"
        port=3306,         # Default MySQL port
        user="root",
        password="pcsr125",
        database="notes_db"
    )


@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    content = request.form['content']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        new_title = request.form['title']
        new_content = request.form['content']
        cursor.execute("UPDATE notes SET title=%s, content=%s WHERE id=%s", (new_title, new_content, id))
        conn.commit()
        conn.close()
        return redirect('/')

    cursor.execute("SELECT * FROM notes WHERE id=%s", (id,))
    note = cursor.fetchone()
    conn.close()
    return render_template('edit.html', note=note)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000")

    threading.Timer(1, open_browser).start()  # Open browser after 1 second
    app.run(debug=True)
    