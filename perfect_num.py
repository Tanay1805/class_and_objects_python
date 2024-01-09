def is_perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num


number_to_check =int(input("Enter a number:"))
if is_perfect_number(number_to_check):
    print(f"{number_to_check} is a perfect number.")
else:
    print(f"{number_to_check} is not a perfect number.")
