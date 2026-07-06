CREATE DATABASE ejercicios_sql;

USE ejercicios_sql;

CREATE table user (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(50) NOT NULL,
email VARCHAR(30) UNIQUE NOT NULL,
registration_date TEXT DEFAULT (DATETIME('now'))
);

CREATE table product (
id INTEGER PRIMARY KEY AUTOINCREMENT,
code SMALLINT UNIQUE,
name VARCHAR(50),
price FLOAT NOT NULL,
entry_date TEXT DEFAULT (DATETIME('now')),
brand VARCHAR(50) NOT NULL,
stock_available INT NOT NULL
);

CREATE table payment_method (
id INTEGER PRIMARY KEY AUTOINCREMENT,
method_type VARCHAR(15) NOT NULL,
bank_name VARCHAR(20) NULL
);

CREATE table invoice (
id INTEGER PRIMARY KEY AUTOINCREMENT,
invoice_number SMALLINT NOT NULL,
purchase_date TEXT DEFAULT (DATETIME('now')),
total_amount REAL NOT NULL,
fk_user_id INT NOT NULL REFERENCES user(id),
fk_payment_method_id INT NOT NULL REFERENCES payment_method(id)
);

CREATE table products_invoice (
id INTEGER PRIMARY KEY AUTOINCREMENT,
quantity INT NOT NULL,
total_amount FLOAT NOT NULL,
fk_product_id INT NOT NULL REFERENCES product(id),
fk_invoice_id INT NOT NULL REFERENCES invoice(id)
);

CREATE table review (
id INTEGER PRIMARY KEY AUTOINCREMENT,
comment VARCHAR(255) NOT NULL,
rating SMALLINT NOT NULL,
date TEXT DEFAULT (DATETIME('now')),
fk_user_id INT NOT NULL REFERENCES user(id),
fk_product_id INT NOT NULL REFERENCES product(id)
);

CREATE table shopping_cart(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fk_user_id INT NOT NULL REFERENCES user(id)
);

CREATE TABLE products_shopping_cart (
id INTEGER PRIMARY KEY AUTOINCREMENT,
quantity INT NOT NULL,
fk_product_id INT NOT NULL REFERENCES product(id),
fk_shopping_cart_id INT NOT NULL REFERENCES shopping_cart(id)
);

ALTER table invoice ADD buyer_phone_number INTEGER;
ALTER table invoice ADD employee_code INTEGER


INSERT INTO user (full_name, email) 
VALUES 
    ('Juan Perez', 'juanito@gmail.com'),
    ('María Magdalena', 'mariquita@hotmail.com'),
    ('Pedro Sola', 'sola.solin@gmail.com'),
    ('Ana Solis', 'anita@hotmail.com'),
    ('Dante Jimenez', 'jimenezdante@hotmail.com');


INSERT INTO product (code, name, price, brand, stock_available) 
VALUES 
    (65437, 'cuerda', 50500, 'mineral', 18),
    (18296, 'peluche', 20000, 'maquina', 20),
    (76219, 'botas', 200500, 'plastic', 75),
    (62109, 'patito de hule', 45000, 'cuak', 100),
    (22001, 'balon', 320000, 'nike', 25),
    (66589, 'pelota', 10000, 'adidas', 90),
    (22182, 'carro rc', 95000, 'rc', 60);

INSERT INTO payment_method (method_type, bank_name) 
VALUES 
    ('cash', NULL),
    ('tranfer', 'BBVA'),
    ('credit card', 'Banamex'),
    ('Pay Pal', NULL);

INSERT INTO review (comment, rating, fk_user_id, fk_product_id) 
VALUES 
    ('bad quality', 2, 1, 1),
    ('very nice', 5, 3, 2),
    ('very good battery', 5, 3, 7);

INSERT INTO products_shopping_cart (quantity, fk_product_id, fk_shopping_cart_id) 
VALUES 
    (2, 1, 1),
    (1, 3, 1),
    (1, 6, 1),
    (1, 5, 2),
    (2, 6, 2),
    (1, 1, 3),
    (2, 4, 3),
    (2, 5, 3),
    (3, 7, 3),
    (4, 3,3 );

INSERT INTO invoice (invoice_number, total_amount, fk_user_id, fk_payment_method_id, buyer_phone_number, employee_code) 
VALUES
    (34422, 90000, 2, 1, 4435672819, 2345),
    (34432, 228000, 4, 2, 4437893245, 3421),
    (34556, 643500, 3, 4, 4432221345, 6543),
    (34476, 537000, 2, 1, 4435672819, 2349);


INSERT INTO products_invoice (quantity, total_amount, fk_product_id, fk_invoice_id) 
VALUES 
    (2, 90000, 4, 1),
    (2, 101000, 1, 2),
    (1, 95000, 7, 2),
    (1, 32000, 5, 2),
    (1, 32000, 2, 3),
    (1, 10000, 6, 3),
    (3, 601500, 3, 3),
    (1, 200500, 3, 4),
    (3, 151500, 1, 4),
    (2, 90000, 4, 4),
    (1, 95000, 7, 4);

SELECT * FROM product;
SELECT * FROM product WHERE price > 50000;
SELECT * FROM products_invoice WHERE fk_product_id = 1;
SELECT 
    p.id, 
    p.name, 
    SUM(pi.quantity) AS total_unidades_compradas, 
    SUM(pi.total_amount) AS monto_total_comprado
FROM product p
JOIN products_invoice pi ON p.id = pi.fk_product_id
GROUP BY p.id, p.name;
SELECT * FROM invoice WHERE fk_user_id = 3;
SELECT * FROM invoice ORDER BY total_amount DESC;
SELECT * FROM invoice WHERE invoice_number = 34476;
