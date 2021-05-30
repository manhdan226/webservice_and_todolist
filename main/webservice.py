from flask import Flask, request, jsonify
from flask_cors import CORS
import query_db as db

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources = {
    r"/*": {
        "origin": "*"
    }
})

@app.route("/todo")
def get_all_task():
    return jsonify(db.get_all_task())

@app.route("/todo", methods = ["POST"])
def create_task():
    return jsonify(db.create_task(request.get_json()))

@app.route("/todo/<string:id>")
def get_task_by_id(id):
    return jsonify(db.get_task_by_id(id))

@app.route("/todo/<string:id>", methods = ["PUT"])
def update_task(id):
    try:
        return jsonify(db.update_task(request.get_json(),id))
    except:
        return "Can't put"

@app.route("/todo/<string:id>", methods = ["DELETE"])
def delete_task(id):
    return jsonify(db.delete_task(id))

app.run(port=3000)