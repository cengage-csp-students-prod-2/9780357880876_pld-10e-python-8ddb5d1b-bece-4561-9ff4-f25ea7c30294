# This program calculates profits and sales prices for a furniture company.

item_name = "TV Stand"
retail_price = 325.00
wholesale_price = 200.00
# Write your assignment statements here.
profit = retail_price - wholesale_price
sale_price = retail_price * 0.75
sale_profit = sale_price - wholesale_price
print(f"Item Name: {item_name}")
print(f"Retail Price: ${retail_price:.2f}")
print(f"Wholesale Price: ${wholesale_price:.2f}")
print(f"Profit: ${profit:.2f}")
print(f"Sale Price: ${sale_price:.2f}")
print(f"Sale Profit: ${sale_profit:.2f}")