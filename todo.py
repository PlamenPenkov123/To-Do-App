# todo.py
import psycopg2
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database connection configuration
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Create the 'todos' table if it doesn't already exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        task TEXT NOT NULL
    );
""")
conn.commit()

# GUI app
root = tk.Tk()
root.title("Todo List Application")

# UI elements
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

def refresh_todos():
    task_listbox.delete(0, tk.END)
    cursor.execute("SELECT id, task FROM todos;")
    for id, task in cursor.fetchall():
        task_listbox.insert(tk.END, f"{id}: {task}")


# Function to add a new task
def add_todo():
    tasks = task_entry.get().strip()
    if tasks:
        cursor.execute("INSERT INTO todos (task) VALUES (%s);", (tasks,))
        conn.commit()
        task_entry.delete(0, tk.END)
        refresh_todos()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove a task by ID
def remove_todo():
    selected = task_listbox.curselection()
    if selected:
        task_text = task_listbox.get(selected[0])
        task_id = task_text.split(':')[0]
        cursor.execute("DELETE FROM todos WHERE id = %s;", (task_id,))
        conn.commit()
        refresh_todos()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Main application loop
def main():
    refresh_todos()
    root.mainloop()

add_btn = tk.Button(root, text="Add Task", command=add_todo)
add_btn.pack()

delete_btn = tk.Button(root, text="Delete Selected Task", command=remove_todo)
delete_btn.pack(pady=5)

task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)
# Run the app
main()