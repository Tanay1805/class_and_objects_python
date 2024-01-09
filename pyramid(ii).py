def print_number_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print(i, end=" ")
        print()


num_rows = 5

print_number_triangle(num_rows)
