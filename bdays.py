if __name__ == '__main__':

    birthdays = {
        'John Doe': '01/01/1962',
        'Jane Doe': '06/21/1977',
        'Joe Sixpack': '07/04/1976',
        'Suzy Que': '08/12/1991'}

    print('This is the birthday dictionary. It contains the birthdas of some people:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to know?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('I don\'t know what that is or when their birthday is. Sorry')