from flask import request
from validations import validate_data, validate_id, validate_task, validate_status
from database import save_file, read_file


def get_all_tasks(param):
    tasks = read_file()

    if param:
        validate_status(param)
        tasks = [task for task in tasks if task["status"] == param.title()]

    return {"tasks": tasks}, 200


def get_task_by_id(task_id):
    tasks = read_file()
    task = validate_task(tasks, task_id)

    return {"task": task}, 200


def normalize_status(status):
    return status.title()


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
    new_task["status"] = normalize_status(data["estado"])

    tasks.append(new_task)
    save_file(tasks)

    return {"task": new_task}, 201


def edit_task(task_id):
    tasks = read_file()
    validate_task(tasks, task_id)

    data = request.json
    validate_data(data)

    task_ids = [task["id"] for task in tasks]
    index = task_ids.index(int(task_id))
    tasks[index]["title"] = data["titulo"]
    tasks[index]["description"] = data["descripcion"]
    tasks[index]["status"] = normalize_status(data["estado"])

    save_file(tasks)

    return {"task": tasks[index]}, 200


def delete_task(task_id):
    tasks = read_file()
    task = validate_task(tasks, task_id)

    task_ids = [task["id"] for task in tasks]
    task_index = task_ids.index(int(task_id))
    tasks.pop(task_index)

    save_file(tasks)

    return {}, 200
