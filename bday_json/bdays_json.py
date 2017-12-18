import json

birthday = {}
with open('bdays.json', 'r') as f:
    birthday = json.load(f)

def add_bday():
    name = input('Who do you want to add to the dictionary?\n').title()
    date = input('When was {} born?\n.'.format(name))
    birthday[name] = date
    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f)
    print('{} added to the list\n'.format(name))

def find_bday():
    name = input('Who\'s birthday do you want to know?')
    try :
        if birthday[name]:
            print('{} was born on {}\n'.format(name, birthday[name]))
    except KeyError:
        print('{} ain\'t in the b-day dictionary')
