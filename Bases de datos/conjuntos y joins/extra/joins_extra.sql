CREATE database library;

USE library;

CREATE table author (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR (50) NOT NULL
);

CREATE table book (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR (50) NOT NULL,
fk_author_id INT,
FOREIGN KEY(fk_author_id) REFERENCES author(id)
);

CREATE table customer (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR (50) NOT NULL,
email VARCHAR(60) NOT NULL
);

CREATE table rent (
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
state VARCHAR(20),
fk_book_id INT NOT NULL,
FOREIGN KEY(fk_book_id) REFERENCES book(id),
fk_customer_id INT NOT NULL,
FOREIGN KEY(fk_customer_id) REFERENCES customer(id)
);

INSERT INTO author (name)
VALUES 
	('Miguel de Cervantes'),
	('Dante Alighieri'),
	('Takehiko Inoue'),
	('Akira Toriyama'),
	('Walt Disney');

INSERT INTO book (name, fk_author_id)
VALUES 
	('Don Quijote', 1),
	('La Divina Comedia', 2),
	('Vagabond 1-3', 3),
	('Dragon Ball 1', 4),
	('The Book of the 5 Rings', NULL);

INSERT INTO customer (name, email)
VALUES
	('John Doe', 'j.doe@email.com'),
	('Jane Doe', 'jane@doe.com'),
	('Luke Skywalker', 'darth.son@email.com'),
	('Obi Wan', 'obiwan@email.com');
	
INSERT INTO rent (state, fk_book_id, fk_customer_id)
VALUES 
	('Returned', 1, 2), 
	('Returned', 2, 2),
	('On time', 1, 1),
	('On time', 3, 1),
	('Overdue', 2, 2),
	('Returned', 4, 3), 
	('On time', 5, 1),
	('Overdue', 2, 2),
	('Returned', 3, 4), 
	('Returned', 5, 4);
	
SELECT c.id, c.name, COUNT(*) as total_rents
FROM rent r
INNER JOIN book b ON r.fk_book_id = b.id
INNER JOIN customer c ON r.fk_customer_id =c.id
GROUP BY c.id, c.name
ORDER BY total_rents DESC
LIMIT 3

SELECT c.name, b.name, a.name, r.state 
FROM rent r
INNER JOIN book b ON r.fk_book_id = b.id
LEFT JOIN author a ON b.fk_author_id = a.id
INNER JOIN customer c ON r.fk_customer_id =c.id
