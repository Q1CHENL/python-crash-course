# 10-1, 10-2
with open('learning_python.txt') as file:
    lines = file.readlines()
    #contents = file.read()
    
# for _ in range(3):
#     print(contents)

for line in lines:
    # replace() is tmp
    print(line.replace('python', 'C').rstrip())

# 10-3
usrname = input("Enter your user name:")
with open('guest.txt', 'a') as guest_file:
    guest_file.write(usrname)

# 10-4
while(True):
    name = input("Please enter user name: (q to quit) ")
    if name == 'q': break
    with open('guest_book.txt', 'a') as gb:
        gb.write(f"User [{name}] added!\n") 
# 10-5
while(True):
    reason = input("Why do you like programming? (q to quit) ")
    if reason == 'q': break
    with open('poll_responses.txt', 'a') as pr:
        pr.write(f"{reason.strip()}\n")