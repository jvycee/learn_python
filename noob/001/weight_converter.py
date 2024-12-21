
weight = float(input("Enter your weight: "))
unit = input("Kilos or Pounds? (K or L): ").upper()


result = None
if unit == "K":
    result = weight * 2.205
    unit = "Lbs."
   
elif unit == "L":
    result = weight / 2.205
    unit = "Kgs."
try:
    if result is not None:
        print(f"Your weight is: {round(result, 1)} {unit}")
    
except ValueError:
    print("Please enter a valid number")