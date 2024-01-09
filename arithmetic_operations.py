def perform_arithmetic_operations(num1, num2):

    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2

    equal = num1 == num2
    not_equal = num1 != num2
    greater_than = num1 > num2
    less_than = num1 < num2
    greater_than_equal = num1 >= num2
    less_than_equal = num1 <= num2

    print("Arithmetic Operations:")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")

    print("\nRelational Operations:")
    print(f"{num1} == {num2}: {equal}")
    print(f"{num1} != {num2}: {not_equal}")
    print(f"{num1} > {num2}: {greater_than}")
    print(f"{num1} < {num2}: {less_than}")
    print(f"{num1} >= {num2}: {greater_than_equal}")
    print(f"{num1} <= {num2}: {less_than_equal}")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

perform_arithmetic_operations(number1, number2)
