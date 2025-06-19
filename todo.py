# todo.py
import psycopg2
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

# Function to display the main menu
def show_menu():
    print("\nTodo List Menu:")
    print("1. View Todos")
    print("2. Add Todo")
    print("3. Remove Todo")
    print("4. Exit")
    print("Please choose an option (1-4): \n")

# Function to display all tasks
def show_todos():
    cursor.execute("SELECT id, task FROM todos;")
    tasks = cursor.fetchall()
    
    if not tasks:
        print("No todos found in the database.")
    else:
        print("\nCurrent Todos:")
        print("----------------")
        print("ID | Task")
        for id, task in tasks:
            print(f"{id}  | {task}")

# Function to add a new task
def add_todo():
    task = input("Enter a new task: ")
    cursor.execute("INSERT INTO todos (task) VALUES (%s);", (task,))
    conn.commit()
    print(f"Task \"{task}\" saved to the database.")

# Function to remove a task by ID
def remove_todo():
    show_todos()
    
    # Get the task ID to remove from the user
    task_id = input("Enter the ID of the task to remove: ")
    cursor.execute("DELETE FROM todos WHERE id = %s;", (task_id,))
    conn.commit()
    print(f"Task with ID {task_id} has been removed from the database.")

# Main application loop
def main():
    print("Welcome to the Todo List application!")

    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            show_todos()
        elif choice == '2':
            add_todo()
        elif choice == '3':
            remove_todo()
        elif choice == '4':
            print("Exiting the Todo List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

# Run the app
main()