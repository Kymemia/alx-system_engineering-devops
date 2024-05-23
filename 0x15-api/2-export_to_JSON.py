#!/usr/bin/python3

"""This is a python script that returns information
about his/her TODO list progress using a REST API"""

import json
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
    user_username = user_data["username"]
    user_tasks = []

    for todo in todos_data:
        task_title = todo["title"]
        task_completed = todo["completed"]
        user_tasks.append({"task": task_title, "completed": task_completed,
                           "username": user_username})

    user_data_json = {str(user_id): user_tasks}

    json_filename = f"{user_id}.json"
    with open(json_filename, "w") as json_file:
        json.dump(user_data_json, json_file)


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
