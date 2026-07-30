from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST


def add_car(*args):
    dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
    try:
        query = "INSERT INTO lyfter_car_rental.cars (make, model, year) VALUES (%s, %s, %s) RETURNING *;"

        new_car = dbManager.execute_query(query, *args)
        print("Carro agregado satisfactoriamente")
        return new_car
    except Exception as err:
        print("Error al inserta carro en la base de datos")
        print(err)
        return None
    finally:
        dbManager.close_connection()


if __name__ == "__main__":
    make = input("ingresa la marca del vehiculo: ")
    model = input("ingresa el modelo del vehiculo: ")
    year = input("ingresa el año del vehivulo: ")

    add_car(make, model, year)
