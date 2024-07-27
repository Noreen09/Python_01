# Question 1:

Anton : int = 21
Beth : int = Anton + 6
Chen : int = Beth + 20
Drew : int = Chen + Anton
Ethan : int = Chen

print(f"Anton is {Anton} \n Beth is {Beth} \n Chen is {Chen} \n Drew is {Drew} \n Ethan is {Ethan}")

# Question 2:

name:str = "Alice"
age:int = 30
city:str = "New York"

print(f"{name} is {age} years old and lives in {city}.")

# Question 3:

s: str = "hElLo WoRlD"

print(s.capitalize())
print(s.upper())
print(s.lower())

# Question 4:

s: str = "the quick brown fox jumps over the lazy dog"

print(f"the index of fox is {s.find("fox")}")

print(f"'the' appears {s.count("the")} times")


# Question 5:

s = "I love programming in Python"

print(s.replace("Python", "Java"))  

# Question 6:

s = "apple,banana,cherry,dates"

strings_list = s.split(",")

print(strings_list)

joined_string = " ".join(strings_list)

print(joined_string)

# Question 7:

s = "   Python is fun!   "

trim = s.strip()

left = trim.ljust(20, '*')

right = trim.rjust(20, '*')

print(trim)
print(left)
print(right)

# Question 8 :

num = 45
print(f"Binary representation: {bin(num)}")

# Question 9 :

base = 3
exponent = 4

print(f"Power result: {base ** exponent}")

# Question 10 :

value = 12.34567

print(f"Rounded to nearest integer: {round(value)} \n Rounded to two decimal places: {round(value, 2)}")


