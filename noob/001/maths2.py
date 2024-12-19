import math

#circumfrence of a circle

try:
    radius = float(input("What is the radius of the circle?: "))
    if radius <= 0:
        print("Radius must be a positive number")
    elif radius > 1000: 
        print("Too big!")
    elif radius < 0.01: 
        print("Too small!")
    else:
        circumference = 2 * math.pi * radius
        print(f"The value is {circumference:.2f}in ")
except ValueError:
    print("Please enter a valid number")