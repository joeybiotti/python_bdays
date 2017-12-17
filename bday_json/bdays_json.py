import json

answer = 'yes'

while answer != 'no':
    with open ('birthdays.json', 'r') as f_r:
        data =  json.load(f_r)

        print('Here\'s the people that are in the Birthday Dictionary...')
        for i in data:
            print ("\n" + i)

        ans = input("1: Find someone's birthday. \n OR! \n 2: Add a new person's birthday. \n")

        if ans == "1":
            name = input("Enter the person's name: ")
            print ("The birthday for {} is {}".format(name, data.get(name, "Ain't in the database.")))

        elif ans == "2":
            n = int(input("How many birthdays you wanna add?"))
            i = 0
            while i < n:
                print("\nName", i+1)
                new_name = input("\nEnter name: ")
                new_bd = input("\nEnter their birthday (mm/dd/yyyy): ")

                data[new_name] = new_bd

                with open('birthdays.json', 'w') as f_w:
                    json.dump(data, f_w)

                print ('Birthday added! ')

                i += 1

            else:
                print('\nInvalid choice. DO IT AGAIN! ')

            answer = input('Do you want to add more people?')