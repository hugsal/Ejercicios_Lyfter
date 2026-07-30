from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST


def change_user_status(new_status, id):
    dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
    try:
        query = "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s;"

        dbManager.execute_query(query, new_status, id)
        print("Usuario editado satisfactoriamente")
    except Exception as err:
        print("Error al editar el status del usuario")
        print(err)
    finally:
        dbManager.close_connection()


if __name__ == "__main__":
    id = input("ingresa el id del usuario: ")
    new_status = input("ingresa el status para el ususario: ")

    change_user_status(new_status, id)
