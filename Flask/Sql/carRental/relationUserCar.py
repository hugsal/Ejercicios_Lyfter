from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST

dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
try:
    query = """CREATE TABLE IF NOT EXISTS lyfter_car_rental.user_car_rent (
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
rent_date DATE NOT NULL DEFAULT NOW(),
rent_status VARCHAR(30) NOT NULL DEFAULT 'on_time',
fk_user_id INT NOT NULL,
FOREIGN KEY(fk_user_id) REFERENCES lyfter_car_rental.users(id),
fk_car_id INT NOT NULL,
FOREIGN KEY(fk_car_id) REFERENCES lyfter_car_rental.cars(id)
);"""

    dbManager.execute_query(query)

    query = """INSERT INTO lyfter_car_rental.user_car_rent (rent_status, fk_user_id, fk_car_id)
    VALUES
('on_time', 63, 13),
('on_time', 5, 13),
('on_time', 7, 1),
('delayed', 8, 6),
('on_time', 32, 11),
('on_time', 8, 25),
('on_time', 26, 8),
('delayed', 64, 27),
('on_time', 60, 13),
('on_time', 11, 16),
('on_time', 29, 21),
('on_time', 51, 6),
('on_time', 20, 15),
('on_time', 33, 9),
('on_time', 6, 4),
('on_time', 33, 5),
('on_time', 65, 21),
('on_time', 20, 12),
('on_time', 22, 17),
('on_time', 26, 13),
('on_time', 22, 8),
('on_time', 7, 21),
('delayed', 4, 7),
('on_time', 9, 15),
('on_time', 16, 15);"""

    dbManager.execute_query(query)
    print("Relaciones agregados satisfactoriamente")
except Exception as err:
    print("Error al insertar relaciones en la base de datos")
    print(err)
finally:
    dbManager.close_connection()
