#!/usr/bin/python3

"""This is a python script that returns information
about his/her TODO list progress using a REST API"""

import requests
import sys
import csv


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
    user_id = user_data["id"]

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID",
                             "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"
                             ])

        for todo in todos_data:
            if todo["userId"] == user_id:
                task_completed_status = "Completed" if todo["completed"] \
                                         else "Not Completed"
                task_title = todo["title"]
                csv_writer.writerow([user_id, user_name,
                                    task_completed_status, task_title])


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
