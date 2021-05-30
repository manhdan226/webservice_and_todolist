from boto3 import resource
from flask import (
    Flask,
    render_template,
    redirect,
    request
)
#from flask_restful import Api
from flask_cors import CORS

import requests as req

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources = {
    r"/*": {
        "origin": "*"
    }
})

def get_data_from_webservice():
    webservice_url = "http://127.0.0.1:3000/todo"
    res = req.get(webservice_url)
    tasks_json = res.json()
    tasks_list = [[task_json["id"], task_json["task"], task_json["description"], task_json["assignee"], task_json["deadline"], task_json["progress"]] for task_json in tasks_json]
    tasks_list_sorted = sorted(tasks_list, key = lambda x: int(x[0]))
    return tasks_list_sorted

def get_data_by_id(id):
    print("-------------------------> ",id)
    webservice_url = "http://127.0.0.1:3000/todo/"+id
    print(webservice_url)
    res = req.get(webservice_url)
    task_json = res.json()
    data = [task_json["id"], task_json["task"], task_json["description"], task_json["assignee"], task_json["deadline"], task_json["progress"]]
    return data

@app.route("/home")
def home():
    data = get_data_from_webservice()
    print(data)
    return render_template("index.html", data = data)

@app.route("/<id>")
def view(id):
    data = get_data_by_id(id)
    print(data)
    return render_template("view.html", data = data)

app.run(port=3001)