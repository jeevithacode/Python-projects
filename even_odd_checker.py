number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

if number < 0:
    print("It's also a negative number")
elif number == 0:
    print("It's zero")
else:
    print("It's a positive number")
