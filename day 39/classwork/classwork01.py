price = int(input("enter product price: "))
discount = int(input("enter product discount: "))
discount_price = price * discount / 100
new_price = price - discount_price
print(new_price)