# Take qty and price and display net amount after a discount of 10%

price = int(input("Enter price :"))
qty = int(input("Enter qty :"))

amount = price * qty
discount = amount * 10 // 100
net_amount = amount - discount

print(f"Amount     : {amount:8}")
print(f"- Discount : {discount:8}")
print(f"Net Amount : {net_amount:8}")
