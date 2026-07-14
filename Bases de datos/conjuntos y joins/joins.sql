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
	('Luke Skywalker', 'darth.son@email.com');

INSERT INTO rent (state, fk_book_id, fk_customer_id)
VALUES 
	('Returned', 1, 2), 
	('Returned', 2, 2),
	('On time', 1, 1),
	('On time', 3, 1),
	('Overdue', 2, 2);
	
SELECT b.id, b.name as book, a.name as author
FROM book b
LEFT JOIN author a ON b.fk_author_id = a.id;

SELECT b.id, b.name AS book
FROM book b
LEFT JOIN author a ON b.fk_author_id = a.id
WHERE a.id IS NULL;

SELECT a.id, a.name as author
FROM book b
RIGHT JOIN author a ON b.fk_author_id = a.id
WHERE b.id IS NULL;

SELECT DISTINCT b.id, b.name
from book b 
INNER JOIN rent r ON b.id = r.fk_book_id;

SELECT DISTINCT b.id, b.name
from book b 
LEFT JOIN rent r ON b.id = r.fk_book_id
WHERE r.id IS NULL;

SELECT DISTINCT c.id, c.name
from customer c  
LEFT JOIN rent r ON c.id = r.fk_customer_id
WHERE r.id IS NULL;

SELECT DISTINCT b.id, b.name
from book b 
INNER JOIN rent r ON b.id = r.fk_book_id
WHERE r.state = 'Overdue';
