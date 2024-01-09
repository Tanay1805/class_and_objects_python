def calculate_factorial(number):
    factorial_result = 1


    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        for i in range(1, number + 1):
            factorial_result *= i

        print(f"The factorial of {number} is: {factorial_result}")

num_to_calculate_factorial = int(input("Enter a non-negative integer: "))
calculate_factorial(num_to_calculate_factorial)

