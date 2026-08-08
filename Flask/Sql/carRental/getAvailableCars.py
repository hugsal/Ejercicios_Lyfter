from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST


def formatted_car(car):
    return {
        "id": car[0],
        "make": car[1],
        "model": car[2],
        "year": car[3],
        "status": car[4],
    }


def get_available_cars():
    dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
    try:
        query = "SELECT * FROM lyfter_car_rental.cars WHERE status = 'ready'"
        results = dbManager.execute_query(query)
        formatted_results = [formatted_car(result) for result in results]
        return formatted_results
    except Exception as err:
        print("Error al obtener informacion")
        print(err)
    finally:
        dbManager.close_connection()


if __name__ == "__main__":
    get_available_cars()
