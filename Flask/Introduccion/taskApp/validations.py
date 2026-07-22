from flask import abort


def validate_id(tasks, id):
    if not id:
        abort(400, "El identificador es obligatorio")

    if not isinstance(id, int):
        abort(400, "el id debe ser numerico")

    task = next((task for task in tasks if task["id"] == int(id)), None)
    if task:
        abort(400, "El identificador ya existe")


def validate_status(status):
    task_status = ("Por Hacer", "En Progreso", "Completada")

    normalized_status = status.title()
    if normalized_status not in task_status:
        abort(400, "El estado es invalido")


def validate_type(value, field):
    if isinstance(value, str):
        clean_value = value.strip()
        if not clean_value:
            abort(400, f"El campo {field} no puede estar vacío.")
    else:
        abort(400, f"El campo {field} debe ser texto.")


def validate_data(task):
    title = task.get("titulo", None)
    description = task.get("descripcion", None)
    status = task.get("estado", None)

    if not title:
        abort(400, "El titulo de la tarea es obligatorio")

    validate_type(title, "titulo")

    if not description:
        abort(400, "La descripcion de la tarea es obligatoria")

    validate_type(description, "descripcion")

    if status:
        validate_status(status)
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
