#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the CSV format."""


if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    url_employee = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(user_id)
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(user_id)
    req_employee = requests.get(url_employee)
    req_todo = requests.get(url_todo)
    username = req_employee.json().get('username')
    filename = "{}.csv".format(user_id)
    with open(filename, "w", encoding="utf-8") as _file:
        for task in req_todo.json():
            txt = '"{}", "{}", "{}", "{}"\n'\
                .format((user_id), username, task['completed'], task['title'])
            _file.write(txt)
