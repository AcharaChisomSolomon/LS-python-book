def print_range(num):
    if num < 0:
        print(f'{num} is less than 0')
    elif num <= 50:
        print(f'{num} is between 0 and 50')
    elif num <= 100:
        print(f'{num} is between 51 and 100')
    else:
        print(f'{num} is greater than 100')

print_range(0)
print_range(25)
print_range(50)
print_range(75)
print_range(100)
print_range(125)
print_range(-25)