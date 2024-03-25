number = int(input("Enter a number: "))
reversed_number = 0
copy = number
while number > 0:
    z = number % 10
    reversed_number = reversed_number * 10 + z
    number = number // 10
if copy == reversed_number:
    print("Palindrome")
else:
    print("Not Palindrome")
