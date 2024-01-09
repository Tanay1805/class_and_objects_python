def traverse_reverse_using_slicing(lst):
    reversed_list = lst[::-1]
    
    for item in reversed_list:
        print(item)

my_list = [1, 2, 3, 4, 5]
traverse_reverse_using_slicing(my_list)

def traverse_reverse_using_reverse(lst):
    reversed_list = list(lst)
    reversed_list.reverse()
    
    for item in reversed_list:
        print(item)


my_list = [1, 2, 3, 4, 5]
traverse_reverse_using_reverse(my_list)
