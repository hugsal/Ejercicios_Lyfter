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
status VARCHAR(30),
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
    
INSERT INTO bill (bill_number, total_amount, status, fk_user_id)
VALUES (2712, 200, 'Procesada', 3);

INSERT INTO products_bill (quantity, total_amount, fk_product_id, fk_bill_id)
VALUES (1, 200, 2, 1);

UPDATE bill
    SET status = 'Procesada'
    WHERE id = 1;
    
    
DO $$
DECLARE	
    -- Definimos variables para almacenar datos durante la ejecución
    v_product_id INTEGER;
    v_record RECORD;
    v_bill_id INTEGER;
    
BEGIN
    -- 1. Validar Factura
    
    SELECT id INTO v_bill_id
    FROM bill
    WHERE bill_number = 2712;
    
    IF v_bill_id IS NULL THEN
      RAISE EXCEPTION 'Factura no encontrada. Abortando transacción.';
    END IF;
    
    -- 2. Obtener productos a devolver
    
	FOR v_record IN
    SELECT fk_product_id, quantity
    FROM products_bill
    WHERE id = v_bill_id
    
    LOOP
        RAISE NOTICE 'Procesando Producto ID: %, Cantidad a retornar: %', v_record.fk_product_id, v_record.quantity;
        
        -- Si el producto o la cantidad son nulos, saltamos para evitar errores en el WHERE
        IF v_record.fk_product_id IS NOT NULL AND v_record.quantity IS NOT NULL THEN
            UPDATE product
            SET stock_available = stock_available + v_record.quantity
            WHERE id = v_record.fk_product_id;
        END IF;
    END LOOP;
    
   -- 4. Cambiar status de factura
   
   	UPDATE bill
    SET status = 'Retornada'
    WHERE id = v_bill_id;
   	
    RAISE NOTICE 'Transacción finalizada.';
END $$;