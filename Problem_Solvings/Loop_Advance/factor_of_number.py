number = int(input("Enter a number: "))
print(f'All The Factors of {number} is:')
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
