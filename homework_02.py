# Question 1

num1 : int = input("Please enter the first number: ")
num2 : int  = input("Please enter the second number: ")

sum : int = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

# Question 2

fav_animal : str = input("What's your favorite animal? ")
print(f"My favorite animal is also {fav_animal}!")

# Question 3

fahrenheit : float = input("Enter temperature in Fahrenheit: ")

celsius : float = (fahrenheit - 32) * 5.0 / 9.0
print(f"Temperature: {fahrenheit}F = {celsius}C")

# Question 4

side1 : float = input("What is the length of side 1? ")
side2 : float = input("What is the length of side 2? ")
side3 : float = input("What is the length of side 3? ")

perimeter : float = side1 + side2 + side3
print(f"The perimeter of the triangle is {perimeter}")

# Question 5 

number : float = float(input("Type a number to see its square: "))
square : float = number * number

print(f"{number} squared is {square}")

# Question 6

numbers : list[int] = [1, 2, 3, 4, 5]
numbers.remove(3)

print(numbers)

# Question 7

list1 : list[int] = [1, 2, 3]
list2 : list[int] = [4, 5, 6]

list1.extend(list2)
print(list1)

# Question 8

items : list[int] = [10, 20, 30, 40]

rem_val : int = items.pop()

print(f"Modified list: {items}")
print(f"Removed value: {rem_val}")

# Question 9

colors : list[str] = ['red', 'blue', 'green', 'yellow']
index : str = colors.index('green')

print(f"The index of 'green' is {index}")

# Question 10

def element(lst):
    print(lst[-1])

list = [1, 2, 3, 4, 5]
element(list)


# Question 11
list = []
while True:
    value = input("Enter a value: ")
    if value == "":
        break
    list.append(value)

print(f"Here's the list: {list}")



