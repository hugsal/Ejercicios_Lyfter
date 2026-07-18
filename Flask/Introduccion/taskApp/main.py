from flask import Flask, request
from validations import validate_task, validate_id, validate_data
from database import read_file, save_file

app = Flask(__name__)

router = {
    "get_tasks": "/tasks",
    "get_task": "/task/<task_id>",
    "post_task": "/create-task",
    "put_task": "/edit-task/<task_id>",
    "delete_task": "/delete-task/<task_id>",
}


@app.route(router.get("get_tasks"))
def get_tasks():
    tasks = read_file()
    return {"tasks": tasks}, 200


@app.route(router.get("get_task"))
def get_task(task_id):
    tasks = read_file()
    task = validate_task(tasks, task_id)

    return {"task": task}, 200


@app.route(router.get("post_task"), methods=["POST"])
def create_task():
    data = request.json
    tasks = read_file()

    id = data.get("identificador", None)
    validate_id(tasks, id)
    validate_data(data)

    new_task = {}

    new_task["id"] = data["identificador"]
    new_task["title"] = data["titulo"]
    new_task["description"] = data["descripcion"]
    new_task["status"] = data["estado"].title()

    tasks.append(new_task)
    save_file(tasks)

    return {"task": new_task}, 201


@app.route(router.get("put_task"), methods=["PUT"])
def edit_task(task_id):
    tasks = read_file()
    validate_task(tasks, task_id)

    data = request.json
    validate_data(data)

    task_ids = [task["id"] for task in tasks]
    index = task_ids.index(int(task_id))
    tasks[index]["title"] = data["titulo"]
    tasks[index]["description"] = data["descripcion"]
    tasks[index]["status"] = data["estado"]

    save_file(tasks)

    return {"task": tasks[index]}, 200


@app.route(router.get("delete_task"), methods=["DELETE"])
def delete_task(task_id):
    tasks = read_file()
    task = validate_task(tasks, task_id)

    task_ids = [task["id"] for task in tasks]
    task_index = task_ids.index(int(task_id))
    tasks.pop(task_index)

    save_file(tasks)

    return {}, 200


if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)
