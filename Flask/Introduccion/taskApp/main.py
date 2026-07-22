from flask import Flask, request
from taskService import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    edit_task,
    delete_task,
)

app = Flask(__name__)


@app.route("/tasks", methods=["GET", "POST"])
def get_tasks():
    method = request.method
    query_param = request.args.get("estado", None)
    if method == "GET":
        return get_all_tasks(query_param)

    if method == "POST":
        return create_task()

    return {}, 403


@app.route("/tasks/<task_id>", methods=["GET", "PUT", "DELETE"])
def operations(task_id):
    method = request.method
    match method:
        case "GET":
            return get_task_by_id(task_id)
        case "PUT":
            return edit_task(task_id)
        case "DELETE":
            return delete_task(task_id)
        case _:
            return {}, 403


if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)
