a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Complete list:", a)
print("4th element of list:", a[3])
print("List from 0th to 4th index:", a[:5])
print("List -7th to 3rd element:", a[-7:4])

a.append(110)
print("List after appending 110:", a)

a.sort()
print("List after sorting:", a)

popped_element = a.pop()
print("Popped element:", popped_element)
print("List after popping:", a)

specified_element = 50
a.remove(specified_element)
print(f"List after removing {specified_element}:", a)

index_to_insert = 2
element_to_insert = 15
a.insert(index_to_insert, element_to_insert)
print(f"List after inserting {element_to_insert} at index {index_to_insert}:", a)

element_to_count = 30
count = a.count(element_to_count)
print(f"Occurrences of {element_to_count} in the list:", count)

extension_list = [120, 130, 140]
a.extend(extension_list)
print("List after extending with another list:", a)

a.reverse()
print("Reversed list:", a)
