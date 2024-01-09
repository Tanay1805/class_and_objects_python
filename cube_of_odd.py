def create_odd_cube_dictionary(start, end):
    odd_cube_dict = {}

    for number in range(start, end + 1):
        if number % 2 != 0:
            odd_cube_dict[number] = number ** 3

    return odd_cube_dict

start_range = 1
end_range = int(input('Enter your range where should it end:'))

result_dict = create_odd_cube_dictionary(start_range, end_range)
print("Dictionary of cubes of odd numbers:", result_dict)
