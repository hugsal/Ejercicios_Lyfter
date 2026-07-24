from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST


def create_rent(user_id, car_id):
    dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
    try:
        query = "INSERT INTO lyfter_car_rental.user_car_rent (fk_user_id, fk_car_id) VALUES (%s, %s)"

        dbManager.execute_query(query, user_id, car_id)
        print("Renta creada satisfactoriamente")
    except Exception as err:
        print("Error al crear nueva renta")
        print(err)
    finally:
        dbManager.close_connection


if __name__ == "__main__":
    user_id = input("ingresa el id del usuario: ")
    car_id = input("ingresa el id del carro: ")

    create_rent(user_id, car_id)
