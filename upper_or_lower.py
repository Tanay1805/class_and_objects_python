def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

string_test = input("Enter the string:")
upper, lower = count_upper_lower(string_test)
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")
