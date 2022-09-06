#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""


if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    url_employee = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    url_todo = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    req_employee = requests.get(url_employee)
    EN = req_employee.json().get('name')
    req_todo = requests.get(url_todo)
    TOTAL_T = len(req_todo.json())
    TASKS = 0
    NUMT = 0
    lists = []
    while TASKS < TOTAL_T:
        if req_todo.json()[TASKS].get('completed') is True:
            lists.append(req_todo.json()[TASKS].get('title'))
            NUMT += 1
        TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(EN, NUMT, TOTAL_T))
    for t in lists:
        print("\t{} ".format(t))
