year = int(input("Please Tell Your Year: "))

if year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
elif year % 100 == 0 and year % 400 == 0:
    print('Leap Year')
else:
    print('Not Leap Year')
