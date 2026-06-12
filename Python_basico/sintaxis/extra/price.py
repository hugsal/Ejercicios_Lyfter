price = int(input("Enter the price of the item:"))
discount = 0
final_price = 0
if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.1

final_price = price - discount

print("The final price is: ", final_price)