CREATE DATABASE cars;

USE cars;

CREATE table make (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(15) NOT NULL
);


CREATE table color (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
color VARCHAR(15) NOT NULL
);

CREATE table year (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
year SMALLINT NOT NULL
);

CREATE table model (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(15) NOT NULL,
fk_make_id INT NOT NULL,
FOREIGN KEY(fk_make_id) REFERENCES make(id),
fk_color_id INT NOT NULL,
FOREIGN KEY(fk_color_id) REFERENCES color(id),
fk_year_id INT NOT NULL,
FOREIGN KEY(fk_year_id) REFERENCES year(id)
);

CREATE table user (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(30) NOT NULL,
phone_number BIGINT NOT NULL 
);

CREATE table insurance_policy (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(30) NOT NULL
);

CREATE table car(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
VIN VARCHAR(11) NOT NULL,
fk_model_id INT NOT NULL,
FOREIGN KEY(fk_model_id) REFERENCES model(id)
);

CREATE table cars_user (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
fk_car_id INT NOT NULL,
FOREIGN KEY(fk_car_id) REFERENCES car(id),
fk_user_id INT NOT NULL,
FOREIGN KEY(fk_user_id) REFERENCES user(id)
);


CREATE table insurance_company (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(30) NOT NULL,
fk_insurance_policy_id INT NOT NULL,
FOREIGN KEY(fk_insurance_policy_id) REFERENCES insurance_policy(id),
fk_car_id INT NOT NULL,
FOREIGN KEY(fk_car_id) REFERENCES car(id)
);

INSERT INTO make (name) VALUES ('Honda'), ('Chevrolet');
INSERT INTO color (color) VALUES ('Silver'), ('Blue'), ('Red');
INSERT INTO year (year) VALUES (2003), (2014), (2015);
INSERT INTO model (name, fk_make_id, fk_color_id, fk_year_id) 
VALUES 
	('Accord', 1, 1, 1),
	('CR-V', 1, 2, 2),
	('Volt', 2, 3, 3);

INSERT INTO user (name, phone_number) 
VALUES 
	('Alice', 1234567890), 
	('Bob', 9876543210),
	('Claire', 5551234567),
	('Dave', 1112223333);

INSERT INTO insurance_policy (name) 
VALUES 
	('Fire & Theft'),
	('Full Cover'),
	('Collision'),
	('Basic Legal');

INSERT INTO car (VIN, fk_model_id)
VALUES
	('1HGCM82633A', 1),
	('5J6RM4H79EL', 2),
	('1G1RA6EH1FU', 3);

INSERT INTO cars_user (fk_car_id, fk_user_id)
VALUES
	(1, 1),
	(1, 2),
	(2, 3),
	(3, 4)

INSERT INTO insurance_company (name, fk_insurance_policy_id, fk_car_id) 
VALUES 
	('ABC Insurance', 1, 1),
	('XYZ Insurance', 2, 1),
	('DEF Insurance', 3, 2),
	('GHI Insurance', 4, 3);

SELECT 
    c.VIN,
    mo.name AS model,
    ma.name AS make,
    co.color,
    y.year,
    u.name AS owner,
    u.phone_number,
    ic.name AS insurance_company,
    ip.name AS insurance_policy
FROM car c
INNER JOIN model mo ON c.fk_model_id = mo.id
INNER JOIN make ma ON mo.fk_make_id = ma.id
INNER JOIN color co ON mo.fk_color_id = co.id
INNER JOIN year y ON mo.fk_year_id = y.id 
LEFT JOIN cars_user cu ON c.id = cu.fk_car_id
LEFT JOIN user u ON cu.fk_user_id = u.id
LEFT JOIN insurance_company ic ON c.id = ic.fk_car_id
LEFT JOIN insurance_policy ip ON ic.fk_insurance_policy_id = ip.id;

SELECT 
    c.VIN,
    mo.name AS model,
    ma.name AS make,
    co.color,
    y.year,
    u.name AS owner,
    u.phone_number,
    GROUP_CONCAT(DISTINCT ic.name, ', ') AS insurance_company,
    GROUP_CONCAT(DISTINCT ip.name, ', ') AS insurance_policy
FROM car c
INNER JOIN model mo ON c.fk_model_id = mo.id
INNER JOIN make ma ON mo.fk_make_id = ma.id
INNER JOIN color co ON mo.fk_color_id = co.id
INNER JOIN year y ON mo.fk_year_id = y.id
LEFT JOIN cars_user cu ON c.id = cu.fk_car_id
LEFT JOIN user u ON cu.fk_user_id = u.id
LEFT JOIN insurance_company ic ON c.id = ic.fk_car_id
LEFT JOIN insurance_policy ip ON ic.fk_insurance_policy_id = ip.id
GROUP BY c.id, c.VIN, mo.name, ma.name, co.color, y.year, u.name, u.phone_number;