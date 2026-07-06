CREATE DATABASE orders;

USE orders;

CREATE table user (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(30) NOT NULL,
phone BIGINT NOT NULL
);

CREATE table product (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(30) NOT NULL,
price INT NOT NuLL
);

CREATE table delivery(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
address VARCHAR(50) NOT NULL,
time TIME NOT NULL,
fk_user_id INT NOT NULL,
FOREIGN KEY (fk_user_id) REFERENCES user(id)
);

CREATE table items_delivery (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
quantity INT NOT NULL,
special_request VARCHAR(30),
fk_product_id INT NOT NULL,
FOREIGN KEY (fk_product_id) REFERENCES product(id),
fk_delivery_id INT NOT NULL,
FOREIGN KEY (fk_delivery_id) REFERENCES delivery(id)
);

INSERT INTO user (name, phone)
VALUES
	('Alice', 1234567890),
	('Bob', 9876543210),
	('Claire', 5551234567);
	
INSERT INTO product (name, price)
VALUES
	('Cheeseburger', 8),
	('Fries', 3),
	('Pizza', 12),
	('Salad', 6),
	('Water', 1);

INSERT INTO delivery (address, time, fk_user_id)
VALUES
	('123 Main St', '18:00:00', 1),
	('456 Elm St', '19:30:00', 2),
	('789 Oak St', '12:00:00', 3),
	('464 Georgia St', '17:00:00', 3);

INSERT INTO items_delivery (quantity, special_request, fk_product_id, fk_delivery_id)
VALUES
	(2, 'No onions', 1, 1),
	(1, 'Extra ketchup', 2, 1),
	(1, 'Extra cheese', 3, 2),
	(2, NULL, 2, 2),
	(1, 'No croutons', 4, 3),
	(1, NULL, 5, 4);

SELECT d.id, u.name, u.phone, id.quantity, p.name, p.price, id.special_request, d.address, d.time
FROM items_delivery id
INNER JOIN delivery d ON id.fk_delivery_id = d.id
INNER JOIN product p  ON fk_product_id = p.id
INNER JOIN user u ON d.fk_user_id = u.id;