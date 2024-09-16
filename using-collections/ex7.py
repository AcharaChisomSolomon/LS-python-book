info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# new_info = '+'.join(info.split(':'))
# print(new_info)

new_info = info.replace(':', '+')
print(new_info)  # xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh