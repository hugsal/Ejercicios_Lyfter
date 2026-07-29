from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST

dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
try:
    query = """CREATE TABLE IF NOT EXISTS lyfter_car_rental.cars (
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) UNIQUE NOT NULL,
year BIGINT NOT NULL,
status VARCHAR(30) NOT NULL DEFAULT 'ready'
);"""

    dbManager.execute_query(query)

    query = """INSERT INTO lyfter_car_rental.cars (make, model, year)
    VALUES
('Audi', 'RS 4', 2008),
('Dodge', 'Ram Wagon B350', 1993),
('Nissan', 'Leaf', 2011),
('Toyota', 'Camry Hybrid', 2009),
('Acura', 'MDX', 2010),
('Volkswagen', 'GLI', 2009),
('Ford', 'Ranger', 2002),
('Chevrolet', 'Express 3500', 2012),
('Buick', 'Rainier', 2006),
('Mercury', 'Cougar', 197),
('Hyundai', 'Santa Fe', 2010),
('Toyota', 'Camry', 1997),
('Buick', 'LaCrosse', 2011),
('Geo', 'Metro', 1996),
('Volvo', 'S60', 2012),
('Nissan', 'Pathfinder', 2001),
('Mazda', 'RX-8', 200),
('Mercury', 'Sable', 2005),
('Hyundai', 'Veracruz', 2010),
('Mitsubishi', 'Pajero', 1998),
('Chevrolet', 'S10', 1997),
('Eagle', 'Vision', 1996),
('Acura', 'RL', 2000),
('Volkswagen', 'Eos', 2007),
('Honda', 'Civic Si', 2003),
('Mazda', 'Miata MX-5', 2003),
('Nissan', 'Xterra', 2000),
('Bentley', 'Continental GTC', 2009),
('Kia', 'Spectra', 2004),
('Mercury', 'Mountaineer', 2010);"""

    dbManager.execute_query(query)
    print("Carros agregados satisfactoriamente")
except Exception as err:
    print("Error al insertar carros en la base de datos")
    print(err)
finally:
    dbManager.close_connection()
