# 7-8
sandwich_orders = ['s1', 's2', 's3']
finished_sandwiches = []
while sandwich_orders:
    s = sandwich_orders.pop()
    print(f"I made your {s} sandwich")
    finished_sandwiches.append(s)
for s in finished_sandwiches:
    print(f"{s}")

# 7-9
sandwich_orders = ['pastrami', 'chicken', 'beans', 'pastrami', 'pastrami']
print("Deli has run out of pastrami!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 7-10
poll_active = True
locations = []
while poll_active:
    locations.append(input("If you could visit one place in the world, where would you go?\n"))
    if input('continue to poll(yes/no): ') == 'no':
        poll_active = False
for location in locations:
    print(f"{location}")
    