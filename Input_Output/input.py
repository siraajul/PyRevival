# Basic Input
name = str(input("What is your name ?"))
print('Hello' + name)

# Escape Sequence
print('My name is Sirajul &\nMy Age is 22')  # \n means 'next line'
print('My name is Sirajul &\tMy Age is 22')  # \t means 'tab'
print('My name is Sirajul &\bMy Age is 22')  # \b means 'backspace'

# Raw Strings
print(r"to end you line you have to use \n")  # to stop using escape sequence u have to use 'r' raw strings

# Formatted Strings
age = 27
name = "Sirajul"
print("My name is", name, "\nMy age is", age)  # regular way
print(f"My name is {name}\nMy age is {age-1}")  # this is formatted string
