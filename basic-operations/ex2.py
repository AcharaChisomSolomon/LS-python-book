number = 4936

# extract each digit and print the out showing the ones, tens, hundreds and thousands place
# e.g. 4936
# ones: 6
# tens: 3
# hundreds: 9
# thousands: 4

ones = number % 10
tens = (number % 100) // 10
hundreds = (number % 1000) // 100
thousands = number // 1000

print(f"ones: {ones}")
print(f"tens: {tens}")
print(f"hundreds: {hundreds}")
print(f"thousands: {thousands}")