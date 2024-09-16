old_tuple = (1, 2, 3, 4, 5, 6)

list_from_old_tuple = list(old_tuple)
list_from_old_tuple_reverse = list_from_old_tuple[::-1]

list_from_old_tuple_reverse.remove(list_from_old_tuple_reverse[0])
list_from_old_tuple_reverse.remove(list_from_old_tuple_reverse[-1])

new_tuple = tuple(list_from_old_tuple_reverse)
print(new_tuple)  # (4, 3, 2)