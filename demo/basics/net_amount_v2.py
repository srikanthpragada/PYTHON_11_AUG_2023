# Take qty and price and display net amount after
# a discount based on qty

price = int(input("Enter price :"))
qty = int(input("Enter qty :"))

amount = price * qty

if qty >= 3:
    discount = amount * 40 // 100
elif qty >= 2:
    discount = amount * 30 // 100
else:
    discount = amount * 10 // 100

net_amount = amount - discount

print(f"Amount     : {amount:8}")
print(f"- Discount : {discount:8}")
print(f"Net Amount : {net_amount:8}")
