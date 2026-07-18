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
    -- 1. ENTRADAS: Definimos las "listas" de productos y cantidades a comprar
    v_products_ids INTEGER[] := ARRAY[1, 2, 3]; 
    v_quantities INTEGER[] := ARRAY[2, 1, 5];   
    v_user_id INTEGER := 2;
    v_bill_number INTEGER := 6548;
    
    i INTEGER;
    v_current_product_id INTEGER;
    v_current_qty INTEGER;
    v_available_stock INTEGER;
    v_product_price NUMERIC(10,2);
    v_user VARCHAR(50);
    v_bill_id INTEGER;
    v_total_bill_amount NUMERIC(10,2) := 0.00;
    
BEGIN
    -- STEP 1: Validar si el usuario existe
    SELECT full_name INTO v_user FROM users WHERE id = v_user_id;
    IF v_user IS NULL THEN
        RAISE EXCEPTION 'Usuario con ID % no existe. Abortando transacción.', v_user_id;
    END IF;

    -- STEP 2: Primer recorrido - Validar stock de TODO y calcular el total de la factura
    -- Recorremos el arreglo usando la longitud del mismo
    FOR i IN 1 .. array_length(v_products_ids, 1) LOOP
        v_current_product_id := v_products_ids[i];
        v_current_qty := v_quantities[i];
        
        -- Obtenemos el stock actual y el precio del producto
        SELECT stock_available, price INTO v_available_stock, v_product_price
        FROM product
        WHERE id = v_current_product_id;
        
        IF v_available_stock IS NULL THEN
            RAISE EXCEPTION 'El producto con ID % no existe. Abortando.', v_current_product_id;
        END IF;
        
        IF v_available_stock < v_current_qty THEN
            RAISE EXCEPTION 'Stock insuficiente para el producto ID %. Abortando.', 
                v_current_product_id;
        END IF;
        
        -- Acumulamos el monto total de la factura de forma dinámica
        v_total_bill_amount := v_total_bill_amount + (v_product_price * v_current_qty);
    END LOOP;

    -- STEP 3: Crear la factura
    INSERT INTO bill (bill_number, total_amount, fk_user_id)
    VALUES (v_bill_number, v_total_bill_amount, v_user_id)
    RETURNING id INTO v_bill_id;

    -- STEP 4: Actualizar stock e insertar la relacion
    FOR i IN 1 .. array_length(v_products_ids, 1) LOOP
        v_current_product_id := v_products_ids[i];
        v_current_qty := v_quantities[i];
        
        -- Calcular el subtotal de este producto en particular
        SELECT price INTO v_product_price FROM product WHERE id = v_current_product_id;

        -- Actualizar el stock
        UPDATE product
        SET stock_available = stock_available - v_current_qty
        WHERE id = v_current_product_id;

        -- Insertar el detalle del producto
        INSERT INTO products_bill (quantity, total_amount, fk_product_id, fk_bill_id)
        VALUES (v_current_qty, (v_product_price * v_current_qty), v_current_product_id, v_bill_id);
    END LOOP;

    RAISE NOTICE 'Transacción finalizada con éxito. Factura ID: %, Total: %', v_bill_id, v_total_bill_amount;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Transacción abortada debido a un error: %', SQLERRM;
        RAISE; 
END $$;