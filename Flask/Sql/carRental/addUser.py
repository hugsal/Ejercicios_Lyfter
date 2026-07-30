from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST


def add_user(*args):
    dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
    try:
        query = "INSERT INTO lyfter_car_rental.users (full_name, email, user_name, user_password, born_date) VALUES (%s, %s, %s, %s, %s) RETURNING *;"

        new_user = dbManager.execute_query(query, *args)
        print("Usuario agregado satisfactoriamente")
        return new_user
    except Exception as err:
        print("Error al inserta usuario en la base de datos")
        print(err)
        return None
    finally:
        dbManager.close_connection()


if __name__ == "__main__":
    full_name = input("ingresa tu nombre completo: ")
    email = input("ingresa tu correo electronico: ")
    user_name = input("ingresa tu nombre de usuario: ")
    user_password = input("ingresa tu password: ")
    born_date = input("ingresa tu fecha de nacimineto (YYYY-MM-DD): ")

    add_user(full_name, email, user_name, user_password, born_date)
