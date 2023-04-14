# 10-11, 10-12
import json

def fav_num():
    fn = input("What is your favorite number? ")
    filename = 'fav_num.json'
    with open(filename, 'w') as f:
        json.dump(fn, f)

def print_fav_num():
    filename = 'fav_num.json'
    try:
        with open(filename) as f:
            fn = json.load(f)
    except FileNotFoundError:
        fav_num()
    else:
        print(f"I know your favorite number! It's {fn}")

print_fav_num()
