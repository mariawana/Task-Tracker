https://roadmap.sh/projects/task-tracker

Task Tracker CLI

This project is a simple command line application where you can keep track of your tasks. You can add tasks, update them, delete them, and also change their status depending on what you're currently doing.

I made this to practice working with files, handling user input, and building a small CLI tool without using any external libraries.


Features

- Add a task
- Update a task
- Delete a task
- Mark a task as in-progress or done
- View all tasks
- Filter tasks by status


How to run

Make sure you have Python installed, then run:

python task_cli.py <command>


Commands

Add task:
python task_cli.py add "Buy groceries"

Update task:
python task_cli.py update 1 "Buy groceries and cook dinner"

Delete task:
python task_cli.py delete 1

Mark task:
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1

List tasks:
python task_cli.py list
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress


Notes

- Tasks are saved in a JSON file called tasks.json
- The file is created automatically if it doesn't exist
- Each task has an id, description, status, and timestamps

What I learned

- Reading and writing JSON files
- Handling command line arguments
- Basic CRUD operations
- Organizing simple logic in Python
