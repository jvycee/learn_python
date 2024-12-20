weight = float(input("Enter your weight: "))
unit = input("Kilos or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    print(weight)
elif unit == "L":
    weight = weight / 2.205
    print(weight)
else:
    print("Try again")
    
