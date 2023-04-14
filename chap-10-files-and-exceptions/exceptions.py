# 10-6, 10-7
while(True):
    try:   
        first = (int)(input("First number: "))
        second = (int)(input("Second number: "))
        result = first + second
    except ValueError:
        print("Input must be a number!")
    else:
        print(f"Sum: {first + second}")
        break

# 10-8
try:
    cats = open('cats.txt')
except FileNotFoundError:
    pass
    # 10-9
    # print("File cats.txt does not exist!")
else:
    contents = cats.read()
    print(contents)

# 10-10
try:
    text = open('text.txt')
except FileNotFoundError:
    print("File does not exist!")
else:
    text_contents = text.read()
    count_the = text_contents.count('the ')
    print(f"Occurences of the: {count_the}")
    
    