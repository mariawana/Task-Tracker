import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            data = json.load(file)
            return data
        except:
            return []


# save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# get next id
def get_next_id(tasks):
    if len(tasks) == 0:
        return 1

    max_id = tasks[0]["id"]
    for task in tasks:
        if task["id"] > max_id:
            max_id = task["id"]

    return max_id + 1


# find a task
def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


# add task
def add_task(description):
    tasks = load_tasks()

    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added successfully (ID:", new_task["id"], ")")


# update task
def update_task(task_id, description):
    tasks = load_tasks()
    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found")
        return

    task["description"] = description
    task["updatedAt"] = datetime.now().isoformat()

    save_tasks(tasks)
    print("Task updated")


# delete task
def delete_task(task_id):
    tasks = load_tasks()

    new_list = []
    found = False

    for task in tasks:
        if task["id"] == task_id:
            found = True
        else:
            new_list.append(task)

    if not found:
        print("Task not found")
        return

    save_tasks(new_list)
    print("Task deleted")


# mark task
def mark_task(task_id, status):
    tasks = load_tasks()
    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found")
        return

    task["status"] = status
    task["updatedAt"] = datetime.now().isoformat()

    save_tasks(tasks)
    print("Task updated to", status)


# list tasks
def list_tasks(status=None):
    tasks = load_tasks()

    if status is not None:
        filtered = []
        for task in tasks:
            if task["status"] == status:
                filtered.append(task)
        tasks = filtered

    if len(tasks) == 0:
        print("No tasks found")
        return

    for task in tasks:
        print(task["id"], "-", task["description"], "-", task["status"])


# main
def main():
    if len(sys.argv) < 2:
        print("No command given")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Missing description")
            return
        add_task(sys.argv[2])

    elif command == "update":
        if len(sys.argv) < 4:
            print("Missing arguments")
            return
        update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Missing id")
            return
        delete_task(int(sys.argv[2]))

    elif command == "mark-in-progress":
        mark_task(int(sys.argv[2]), "in-progress")

    elif command == "mark-done":
        mark_task(int(sys.argv[2]), "done")

    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()

    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
