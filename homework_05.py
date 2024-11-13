def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    name : str = input("Hello! What's your name? ")
    print(f"Hi {name}, welcome to the number explorer!")
    
    numbers = []
    for i in range(1, 4):
        number: int = int(input(f"Enter your favorite number {i}: "))
        numbers.append(number)
    
    parity_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    
    print("\nHere’s what we found about your favorite numbers:")
    for num, parity in parity_info:
        print(f"{num} is {parity}.")
    
    print("\nLet's explore the squares of your favorite numbers:")
    for num in numbers:
        square = num ** 2
        print(f"The square of {num} is {square}.")
    
    total_sum = sum(numbers)
    print(f"\nThe sum of your favorite numbers is {total_sum}!")
    
    if is_prime(total_sum):
        print("Wow! The sum is a prime number!")
    else:
        print("The sum is not a prime number!")

    print(f"\nThanks for exploring numbers with me, {name}! Hope you had fun!")

print(main())
