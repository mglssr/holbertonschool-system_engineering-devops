#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the JSON format."""


if __name__ == "__main__":
    import json
    import requests

    url_employee = "https://jsonplaceholder.typicode.com/users"
    req_employee = requests.get(url_employee)
    filename = "todo_all_employees.json"
    users = {}
    user_list = []
    for empl in req_employee.json():
        username = empl.get('username')
        user_id = empl.get('id')
        url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}"\
                   .format(user_id)
        req_todo = requests.get(url_todo)
        user_list = []
        for data in req_todo.json():
            dic = {"task": data['title'], "comple\
ted": data['completed'], "username": username}
            user_list.append(dic)
        users[user_id] = user_list
    with open(filename, "w", encoding="utf-8") as _file:
        _file.write(json.dumps(users))
