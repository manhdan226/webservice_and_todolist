import requests as req

webservice_url = "http://127.0.0.1:2901/home"
res = req.get(webservice_url)
tasks_json = res.json()

def get_data_from_webservice():
    tasks_list = [[task_json["id"], task_json["task"], task_json["description"], task_json["assignee"], task_json["deadline"], task_json["progress"]] for task_json in tasks_json]
    tasks_list_sorted = sorted(tasks_list, key = lambda x: x[0])
    #print(tasks_list_sorted)
    return tasks_list_sorted

def get_data_by_id(id):
    data = [[task_json["id"], task_json["task"], task_json["description"], task_json["assignee"], task_json["deadline"], task_json["progress"]] for task_json in tasks_json if task_json["id"] == id]
    return data