item = input("What item would you like to buy?:")
price = float(input("What is the price?: "))
quantity = int(input("How many?: "))

total = price * quantity

print(f"The total price for {quantity} {item} is ${total:.2f}")