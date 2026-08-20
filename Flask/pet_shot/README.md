# 🐾 Pet Shop API (`pet_shot`)

API RESTful desarrollada en **Python (Flask)** y **SQLAlchemy** para la gestión de productos, inventario, usuarios con roles (`admin` y `client`), carritos de compra, ventas mediante comprobantes SINPE y facturación electrónica con UUID.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.12+
- **Framework**: Flask 3.1
- **Base de Datos Relacional**: PostgreSQL (SQLAlchemy ORM)
- **Caché en Memoria**: Redis (con fallback en memoria para desarrollo local)
- **Autenticación**: JWT con firma RSA (RS256)
- **Pruebas Unitarias**: Unittest

---

## 📂 Estructura del Proyecto

```text
pet_shot/
├── config.py                # Variables de entorno y configuración
├── database.py              # Configuración del motor SQLAlchemy
├── extension.py             # Instancia global del JwtManager (RS256)
├── jwtManager.py            # Manejo de generación y validación de tokens JWT
├── validateRoles.py         # Decorador middleware para control de acceso por rol
├── cacheManager.py          # Gestor de caché Redis con Fallback InMemoryCache
├── main.py                  # Punto de entrada de la aplicación y endpoints REST
├── entities/                # Modelos ORM (User, Product, Cart, CartItem, Invoice, InvoiceItem)
├── repositories/            # Capa de datos y persistencia (UserRepository, ProductRepository, etc.)
├── helpers/                 # Validaciones de entrada y reglas de negocio
├── docs/
│   └── TECHNICAL_DECISIONS.md # Diagrama ER y justificación de decisiones técnicas
├── tests/                   # Suite de pruebas unitarias
│   └── test_main.py
├── run_tests.py             # Script ejecutor automatizado de pruebas unitarias
└── requirements.txt         # Dependencias del proyecto
```

---

## ⚙️ Configuración e Instalación

### 1. Requisitos Previos

- Python 3.10+
- PostgreSQL activo
- Redis (Opcional, la app cuenta con fallback automático en memoria si Redis no está corriendo)

### 2. Variables de Entorno

Puedes modificar la configuración en `config.py` o exportar las variables de entorno en tu terminal:

```bash
export DB_NAME="pet_shop"
export DB_USER="postgres"
export DB_PASSWORD="tu_password"
export DB_HOST="localhost"

export REDIS_HOST="localhost"
export REDIS_PORT="6379"
```

### 3. Instalación de Dependencias

```bash
# Crear y activar entorno virtual
python3 -m venv env
source env/bin/activate  # En Linux/macOS
# env\Scripts\activate   # En Windows

# Instalar librerías requeridas
pip install -r requirements.txt
```

---

## 🚀 Ejecución del Servidor

Para iniciar el servidor de desarrollo Flask:

```bash
python main.py
```

El servidor estará escuchando en `http://localhost:4000`.

---

## 🧪 Ejecución de Unit Tests Automatizados

El proyecto cuenta con una suite de **32 pruebas unitarias** aisladas en [`tests/test_main.py`](file:///Users/ihugs/projects/Ejercicios_lyfter/Flask/pet_shot/tests/test_main.py) que cubren la lógica de los métodos declarados en [`main.py`](file:///Users/ihugs/projects/Ejercicios_lyfter/Flask/pet_shot/main.py) (incluyendo métodos auxiliares de sesión DB, tokens JWT, manejo de errores HTTP, vistas/endpoints con mocks y formateadores de datos de los repositorios).

Para ejecutar la suite completa de pruebas y generar el reporte automático en consola:

```bash
python run_tests.py
```

### Resumen de Clases de Prueba en `tests/test_main.py`:

| Clase de Prueba | Descripción | Cantidad |
| :--- | :--- | :---: |
| `TestMainHelperMethods` | Valida `handle_http_exception`, `generate_tokens`, `get_db` y `close_db`. | 4 |
| `TestUserMethods` | Valida `sigin`, `login`, `me`, `get_users`, `get_user_by_id`, `update_user` y `delete_user`. | 12 |
| `TestProductMethods` | Valida `get_products` (con/sin caché), `create_product` y `delete_product`. | 5 |
| `TestCartMethods` | Valida `get_carts`, `add_to_cart` y `remove_from_cart`. | 3 |
| `TestSalesAndInvoiceMethods` | Valida `create_sale` (con stock/factura y carrito vacío) y `refund_invoice` (éxito y 403 Forbidden). | 4 |
| `TestRepositoryMethods` | Valida los métodos auxiliares de formateo `format_cart` y `format_invoice` en los repositorios. | 4 |

### Ejemplo de Salida del Reporte:

```text
============================================================
 🚀 PET SHOT API AUTOMATED TEST SUITE RUNNER 
============================================================

============================================================
 📊 RESUMEN EJECUTIVO DE PRUEBAS UNITARIAS
============================================================
 Total de Pruebas Ejecutadas : 32
 Pruebas Exitosas            : 32 ✅
 Pruebas Fallidas            : 0 ❌
 Errores de Ejecución        : 0 ⚠️
 Tasa de Éxito               : 100.0%
 Tiempo Total de Ejecución   : 0.059 segundos
============================================================

🎉 ¡TODAS LAS PRUEBAS UNITARIAS PASARON EXITOSAMENTE! 🎉
```

---

## 📌 Resumen de Endpoints de la API

### Autenticación y Usuarios
- `POST /sigin`: Registro de usuario (retorna `user`, `access_token` y `refresh_token`).
- `POST /login`: Inicio de sesión (retorna `access_token` y `refresh_token`).
- `GET /me`: Consulta del perfil autenticado (`client` / `admin`).
- `GET /users`, `GET /users/<id>`, `PUT /users/<id>`, `DELETE /users/<id>`: CRUD de usuarios (Solo `admin`).

### Productos
- `GET /products`: Catálogo de productos (Cacheado 300s).
- `GET /products/<id>`: Detalle de producto (Cacheado 300s).
- `POST /products`, `PUT /products/<id>`, `DELETE /products/<id>`: Gestión de productos (Solo `admin`, Invalida caché).

### Carritos y Ventas
- `GET /carts`: Lista de carritos del usuario (activos e históricos).
- `GET /carts/active`: Obtener o crear carrito activo del cliente.
- `POST /carts/items`: Agregar/modificar producto en el carrito activo.
- `DELETE /carts/items/<product_id>`: Eliminar producto del carrito activo.
- `POST /sales`: Finalizar compra (requiere `billingAddress` y `paymentReference` SINPE). Genera Factura con ID UUID y descuenta stock.
- `GET /invoices`: Historial de facturas (Cacheado 600s).
- `GET /invoices/<invoice_id>`: Detalle de factura por UUID (Cacheado 600s).
- `POST /invoices/<invoice_id>/refund`: Procesar devolución de compra y restaurar stock.
