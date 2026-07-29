from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST


def finish_rent(rent_id):
    dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
    try:
        query = "SELECT fk_car_id FROM lyfter_car_rental.user_car_rent WHERE id = %s"
        result = dbManager.execute_query(query, rent_id)
        if not result:
            return None
        car_id = result[0][0]

        update_car_query = (
            "UPDATE lyfter_car_rental.cars SET status = 'ready' WHERE id = %s"
        )
        dbManager.execute_query(update_car_query, car_id)

        update_rent_query = "UPDATE lyfter_car_rental.user_car_rent SET rent_status = 'finished' WHERE id = %s RETURNING *"
        rental = dbManager.execute_query(update_rent_query, rent_id)
        return rental
    except Exception as err:
        print("Error al finalizar renta")
        print(err)
    finally:
        dbManager.close_connection()


if __name__ == "__main__":
    rent_id = input("ingresa el id de la renta: ")

    finish_rent(rent_id)
