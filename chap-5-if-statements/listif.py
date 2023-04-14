# 5-8 5-12
usernames = ['admin', 'Chen', 'kai', 'noah', 'nick']
if usernames:
    for name in usernames:
        if name == 'admin':
            print('Hello admin, wanna see the status report?')
        else:
            print(f'Hello, {name}')
else:
    # 5-9
    print('We need to find some users!')
# usernames = []
print(usernames)

# 5-10
current_users = usernames.copy()
current_users_lowercase = []
for name in current_users:
    current_users_lowercase.append(name.lower())

current_users[0] = 'Dao'
new_users = ['Hu', 'Ma', 'CHEN']

for new_user in new_users:
    if new_user.lower() in current_users or new_user.lower() in current_users_lowercase:
        print('Named occupied. Enter a new name.')
    else:
        print('The user name is available!')

# 5-11
ordinals = range(1, 10)
for ordinal in ordinals:
    if ordinal == 1:
        suffix = 'st'
    elif ordinal == 2:
        suffix = 'nd'
    elif ordinal == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(f'{ordinal}{suffix}')
