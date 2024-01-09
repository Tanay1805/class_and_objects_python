list1 = [1, 2, 3]
list2 = [4, 5, 6]
result_list = list1 + list2
print("Extended list using + operator:", result_list)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)
print("Extended list using append():", list1)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("Extended list using extend():", list1)
