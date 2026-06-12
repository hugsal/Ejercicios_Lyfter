employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

departments = {}

for employee in employees:
    department = employee.get("department")
    target_department = departments.get(department)
    if target_department != None:
        target_department.append(employee)
    else:
        departments[department] = [employee]

print(departments)