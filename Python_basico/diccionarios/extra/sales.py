sales = [
	{
		"date": "27/02/23",
		"customer_email": "joe@gmail.com",
		"items": [
			{
				"name": "Lava Lamp",
				"upc": "ITEM-453",
				"unit_price": 65.76,
			},
			{
				"name": "Iron",
				"upc": "ITEM-324",
				"unit_price": 32.45,
			},
			{
				"name": "Basketball",
				"upc": "ITEM-432",
				"unit_price": 12.54,
			},
		],
	},
	{
		"date": "27/02/23",
		"customer_email": "david@gmail.com",
		"items": [
			{
				"name": "Lava Lamp",
				"upc": "ITEM-453",
				"unit_price": 65.76,
			},
			{
				"name": "Key Holder",
				"upc": "ITEM-23",
				"unit_price": 5.42,
			},
		],
	},
	{
		"date": "26/02/23",
		"customer_email": "amanda@gmail.com",
		"items": [
			{
				"name": "Key Holder",
				"upc": "ITEM-23",
				"unit_price": 3.42,
			},
			{
				"name": "Basketball",
				"upc": "ITEM-432",
				"unit_price": 17.54,
			},
		],
	},
]

sales_by_upc = {}

for record in sales:
    items = record.get("items")
    for item in items:
        upc = item.get("upc")
        price = item.get("unit_price")
        total_sale = sales_by_upc.get(upc)
        if total_sale != None:
            sales_by_upc[upc] = total_sale + price
        else:
            sales_by_upc[upc] = price

print(sales_by_upc)