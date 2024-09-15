def return_uppercase(s):
    return s.upper() if len(s) > 10 else s

print(return_uppercase('hello world'))
print(return_uppercase('goodbye'))