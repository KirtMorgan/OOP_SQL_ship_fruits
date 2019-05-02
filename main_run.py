from fruit import Fruit
from boat import  Boat


fruit = Fruit()
boat = Boat()

def user_fruit_add():

    input_1 = input('Please state the fruit type')
    input_2 = int(input(f'What is the weight in KG of {input_1}?'))
    input_3 = (input(f'How much is the grade of the {input_1}?'))
    input_4 = input(f'Is the {input_1} treated YES/NO?')
    input_5 = input(f'What is expiration date of {input_1}')
    fruit.save(f'{input_1}', f'{input_2}', f'{input_3}', f'{input_4}', f'{input_5}')

print('Welcome aboard, please select a option below')
while True:

    print('Option - 1 (Add Fruit to the Cargo List) \nOption - 2 (Print Cargo list)\n')
    user_input = int(input('Your selection >>'))

    if user_input == 1:
        user_fruit_add()
        user_input = input('Do you wish to add another item? y/n')

        if user_input == 'y':
            user_fruit_add()
        elif user_input == 'n':
            continue

    elif user_input == 2:
        print('Please see below Cargo list')
        fruit.read_all()

    else:
        print('Invalid entry please select a option from the list')