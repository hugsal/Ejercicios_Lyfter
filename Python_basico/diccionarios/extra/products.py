products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

sales_by_category = {}

for product in products:
    category = product.get("category")
    price = product.get("price")
    sales = sales_by_category.get(category)
    if sales != None:
        sales_by_category[category] = sales + price
    else:
        sales_by_category[category] = price

print(sales_by_category)