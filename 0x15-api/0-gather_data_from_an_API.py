#!/usr/bin/python3

"""This is a python script that returns information
about his/her TODO list progress using a REST API"""


import requests
import sys


def fetch_user_data(user_id):
    """fetch user data"""
    response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}")
    response.raise_for_status()
    return response.json()


def fetch_todos():
    """fetch todos data"""
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    response.raise_for_status()
    return response.json()


def main(user_id):
    """displays TODO list progress"""
    user_data = fetch_user_data(user_id)
    todos_data = fetch_todos()

    user_name = user_data["name"]
    total_tasks = 0
    completed_tasks = 0
    completed_task_titles = []

    for todo in todos_data:
        if todo["userId"] == user_id:
            total_tasks += 1
            if todo["completed"]:
                completed_tasks += 1
                completed_task_titles.append(todo["title"])

    print(f"Employee {user_name} is done"
          f"with tasks({completed_tasks}/{total_tasks}):")
    for title in completed_task_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    main(employee_id)
