#!/usr/bin/python3

"""This is a python script that returns information
about his/her TODO list progress using a REST API"""

import json
import requests
import sys


def fetch_users():
    """fetch users data"""
    response = requests.get(
            f"https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()
    return response.json()


def fetch_todos():
    """fetch todos data"""
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    response.raise_for_status()
    return response.json()


def main():
    """displays TODO list progress"""
    users_data = fetch_users()
    todos_data = fetch_todos()
    all_employees_data = {}

    for user in users_data:
        user_id = user["id"]
        username = user["username"]
        user_tasks = []

        for todo in todos_data:
            if todo["userId"] == user_id:
                task_info = {
                        "username": username,
                        "task": todo["title"],
                        "completed": todo["completed"]
                        }
                user_tasks.append(task_info)
        all_employees_data[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_data, json_file)


if __name__ == "__main__":
    main()
