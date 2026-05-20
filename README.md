# 📝 Task Manager (CLI in Python)

A simple command-line task manager built in Python.  
This project allows you to create, list, edit, delete, and mark tasks as completed directly in the terminal

---

## 🚀 Features

- Create new tasks
- List all tasks with status (✔ completed / ✗ pending)
- Edit existing tasks
- Delete tasks
- Mark tasks as completed or pending (toggle)
- Simple and interactive menu system

---

## 🧠 How it works

All tasks are stored in a Python list of dictionaries:

```python
{
    "titulo": "Task name",
    "Concluído": False
}
