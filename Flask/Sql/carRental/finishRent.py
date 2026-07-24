from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST


def finish_rent(rent_id):
    dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
    try:
        query = "SELECT fk_car_id FROM lyfter_car_rental.user_car_rent WHERE id = %s"
        result = dbManager.execute_query(query, rent_id)
        car_id = result[0][0]

        query = "UPDATE lyfter_car_rental.cars SET status = %s WHERE id = %s"
        new_status = "ready"
        dbManager.execute_query(query, new_status, car_id)

        query = (
            "UPDATE lyfter_car_rental.user_car_rent SET rent_status = %s WHERE id = %s"
        )
        new_status = "finished"
        dbManager.execute_query(query, new_status, rent_id)
    except Exception as err:
        print("Error al finalizar renta")
        print(err)
    finally:
        dbManager.close_connection


if __name__ == "__main__":
    rent_id = input("ingresa el id de la renta: ")

    finish_rent(rent_id)
