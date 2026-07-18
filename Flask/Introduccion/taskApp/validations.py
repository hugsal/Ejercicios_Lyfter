from flask import abort


def validate_id(tasks, id):
    if not id:
        abort(400, "El identificador es obligatorio")

    if not isinstance(id, int):
        abort(400, "el id debe ser numerico")

    task = next((task for task in tasks if task["id"] == int(id)), None)
    if task:
        abort(400, "El identificador ya existe")


def validate_data(task):
    task_status = ("Por Hacer", "En Progreso", "Completada")

    tittle = task.get("titulo", None).strip()
    description = task.get("descripcion", None).strip()
    status = task.get("estado", None).strip()

    if not tittle:
        abort(400, "El titulo de la tarea es obligatorio")

    if not description:
        abort(400, "La descripcion de la tarea es obligatoria")

    if status:
        normalized_status = status.title()
        if normalized_status not in task_status:
            abort(400, "El estado es invalido")
    else:
        abort(400, "El estado de la tarea es obligatorio")


def validate_task(tasks, id):
    try:
        id_number = int(id)
    except:
        abort(400, "el id debe ser numerico")

    task = next((task for task in tasks if task["id"] == id_number), None)

    if not task:
        abort(404, "tarea no encontrada")

    return task
