firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

if firstNumber > secondNumber:
    print(f"{firstNumber} is greater than {secondNumber}")
elif secondNumber > firstNumber:
    print(f"{secondNumber} is greater than {firstNumber}")
else:
    print("Sorry, the numbers are equal")
