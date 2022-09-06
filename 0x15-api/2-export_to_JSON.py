#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the JSON format."""


if __name__ == "__main__":
    import json
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
    filename = "{}.json".format(user_id)
    user = {}
    user_list = []
    with open(filename, "w", encoding="utf-8") as _file:
        for data in req_todo.json():
            dic = {"task": data['title'], "complet\
ed": data['completed'], "username": username}
            user_list.append(dic)
        user = {'{}'.format(str(user_id)): user_list}
        _file.write(json.dumps(user))
