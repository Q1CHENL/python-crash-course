# 8-1
def display_message():
    print("Learning function!")

display_message()

# 8-2
def favorite_book(title):
    print(f"One of my favorite book is {title}")

favorite_book('pcc')

# 8-3, 8-4
def make_shirt(size='L', text='I love Python'):
    print(f"The shirt is in size {size} with text {text}")

make_shirt('XL', 'Yo')
make_shirt(size='XXL', text='YOLO')
make_shirt()
make_shirt('M')
make_shirt('XXXL', 'SUPER LARGE')

# 8-5
def describe_city(name, country='Germany'):
    print(f"{name} is in {country}")
describe_city('Munich')
describe_city('Karlsruhe')
describe_city('ChangAn', 'China')

# 8-6
def city_country(name, country):
    return f"{name}, {country}"

munich = city_country('Munich', 'Germany')
la = city_country('LA', 'USA')
lodon = city_country('London', 'UK')
print(munich)
print(la)
print(lodon)

# 8-7
def make_album(artist, title, number_of_songs = None):
    album = {'Artist': artist, 'Title': title}
    if number_of_songs:
        album['Number of songs'] = number_of_songs
    return album

folklore = make_album('Taylor', 'folklore')
evermore = make_album('Taylor', 'evermore')
dawn_fm = make_album('The Weeknd', 'DAWN FM')
print(folklore)
print(evermore)
print(dawn_fm)
after_hours = make_album('The Weeknd', 'After Hours', 14)
print(after_hours)

# 8-8
while True:
    artist = input("Enter album's artist: \n(Enter 'q' at any time to quit)\n")
    if artist == 'q':
        break
    title = input("Enter album's title: ")
    album = make_album(artist, title)
    print(album)
    
# 8-9
messages = ['Hallo', 'what', 'up']
def show_messages(message_list):
    for msg in message_list:
        print(msg)
show_messages(messages)

# 8-10
def send_messages(messages_list, sent_messages):
    show_messages(messages_list)
    while messages_list:
        sent_messages.append(messages_list.pop())

sent_msges = []
send_messages(messages, sent_msges)
print(messages)
print(sent_msges)

# 8-11
msgs = ['a', 'b', 'c']
sent_msges = []
send_messages(msgs[:], sent_msges)
print(msgs)
print(sent_msges)
    