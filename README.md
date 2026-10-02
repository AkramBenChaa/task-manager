# Task Manager

A lightweight command-line task manager built with Python.

This project is a simple CLI application for creating, viewing, and deleting tasks while keeping them stored locally between runs.

## Features

- Add new tasks
- View tasks with numbered indexing
- Delete tasks by number
- Persistent local storage using a text file
- Basic input and file error handling
- No external dependencies

## Project Structure

```text
task-manager/
├── task_manager.py
├── README.md
├── LICENSE
└── .gitignore
```

> `tasks.txt` is generated automatically when the application stores tasks and is intentionally ignored by Git.

## Requirements

- Python 3.x

## Run Locally

Clone the repository:

```bash
git clone https://github.com/AkramBenChaa/task-manager.git
cd task-manager
```

Run the application:

```bash
python task_manager.py
```

## Usage

After launching the application, choose an operation from the CLI menu:

1. Add a task
2. View tasks
3. Delete a task
4. Exit

## Storage

Tasks are stored locally in `tasks.txt`. The file is created and updated by the application and does not need to be created manually.

## Notes

This project was built as a Python practice project focused on:

- Functions
- Lists
- File handling
- Exception handling
- Loops and user input
- Basic CLI application structure

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
