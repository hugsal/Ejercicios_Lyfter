from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST


def change_car_status(new_status, id):
    dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
    try:
        query = "UPDATE lyfter_car_rental.cars SET status = %s WHERE id = %s;"

        dbManager.execute_query(query, new_status, id)
        print("Carro editado satisfactoriamente")
    except Exception as err:
        print("Error al editar el status del carro")
        print(err)
    finally:
        dbManager.close_connection


if __name__ == "__main__":
    id = input("ingresa el id del carro: ")
    new_status = input("ingresa el status para el carro: ")

    change_car_status(new_status, id)
