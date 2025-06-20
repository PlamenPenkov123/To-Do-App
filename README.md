# To Do App

A simple command-line To Do application written in Python.

## Features

- Add, view, and remove tasks
- Persistent storage

## Getting Started

### Prerequisites

- Python 3.x installed
- Tkinter installed
- PostgreSQL database

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/PlamenPenkov123/To-Do-App.git
    cd To-Do-App
    ```

    If you do not have a database and user, you can create them with the following commands (replace `your_db_name`, `your_db_user`, and `your_db_password` with your own values):
    
    ```bash
    # Access the PostgreSQL prompt
    psql -U postgres

    # In the PostgreSQL prompt, run:
    CREATE DATABASE your_db_name;
    CREATE USER your_db_user WITH PASSWORD 'your_db_password';
    GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
    GRANT ALL ON SCHEMA public TO your_db_user;
    ```

    Exit the prompt with `\q`.
    
    Create a `.env` file in the project root with your database credentials:
    ```
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Linux/macOS:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the app:
```bash
python3 todo.py
```
