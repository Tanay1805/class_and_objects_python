def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        
        for k in range(i):
            print("* ", end="")
        
        print()
num_rows = 5

print_pyramid(num_rows)
