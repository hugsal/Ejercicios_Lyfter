CREATE table users (
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
full_name VARCHAR(50) NOT NULL,
email VARCHAR(30) UNIQUE NOT NULL
);

CREATE table product (
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
code SMALLINT UNIQUE,
name VARCHAR(50),
price FLOAT NOT NULL,
entry_date TIMESTAMP DEFAULT NOW(),
brand VARCHAR(50) NOT NULL,
stock_available INT NOT NULL
);

CREATE table bill (
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
bill_number SMALLINT NOT NULL,
purchase_date TIMESTAMP DEFAULT NOW(),
total_amount FLOAT NOT NULL,
fk_user_id INT NOT NULL,
FOREIGN KEY(fk_user_id) REFERENCES users(id)
);

CREATE table products_bill (
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
quantity INT NOT NULL,
total_amount FLOAT NOT NULL,
fk_product_id INT NOT NULL REFERENCES product(id),
fk_bill_id INT NOT NULL REFERENCES bill(id)
);

INSERT INTO users (full_name, email) 
VALUES 
    ('Juan Perez', 'juanito@gmail.com'),
    ('María Magdalena', 'mariquita@hotmail.com'),
    ('Pedro Sola', 'sola.solin@gmail.com'),
    ('Ana Solis', 'anita@hotmail.com'),
    ('Dante Jimenez', 'jimenezdante@hotmail.com');

INSERT INTO product (code, name, price, brand, stock_available) 
VALUES 
    (6543, 'cuerda', 50, 'mineral', 18),
    (1829, 'peluche', 200, 'maquina', 20),
    (7621, 'botas', 350, 'plastic', 75),
    (6210, 'patito de hule', 50, 'cuak', 100),
    (2200, 'balon', 500, 'nike', 25),
    (6658, 'pelota', 75, 'adidas', 90),
    (2218, 'carro rc', 950, 'rc', 60);
    
    
DO $$
DECLARE	
    -- Definimos variables para almacenar datos durante la ejecución
    v_available_stock INTEGER;
    v_user VARCHAR(50);
    v_bill_id INTEGER;
    
BEGIN
    -- 1. Validar el stock
    
    SELECT stock_available INTO v_available_stock
    FROM product
    WHERE id = 1;
    
    -- Si no hay stock suficiente, lanzamos un error y detenemos todo
    IF v_available_stock IS NULL OR v_available_stock < 1 THEN
      RAISE EXCEPTION 'Stock insuficiente. Abortando transacción.';
    END IF;
    
    -- 2. Validar user
    
    SELECT full_name INTO v_user
    FROM users
    WHERE id = 2;
    
	IF v_user IS NULL THEN
    	RAISE EXCEPTION 'Usuario no existe. Abortando transacción.';
    END IF;

    -- 3. Si hay stock y existe el usuario, procedemos a crear la factura
    INSERT INTO bill (bill_number, total_amount, fk_user_id)
    VALUES (6548, 50, 2);

    -- 3. Actualizamos el stock
    UPDATE product
    SET stock_available = stock_available - 1
    WHERE id = 1;

   	-- 4. Creamos la relacion, productos-factura
   	
   	SELECT id INTO v_bill_id
   	FROM bill
   	ORDER BY purchase_date DESC
   	LIMIT 1;
   	
   	INSERT INTO products_bill (quantity, total_amount, fk_product_id, fk_bill_id)
   	VALUES (1, 50, 1, v_bill_id);
   	
    RAISE NOTICE 'Transacción finalizada.';
END $$;