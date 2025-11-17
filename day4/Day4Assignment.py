# Program to check if a number is even/odd and positive/negative/zero

# 1. Take integer input
num = int(input("Enter an integer: "))

# 2. Check if even or odd
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 3. Check if positive, negative, or zero
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print("The number is Zero")