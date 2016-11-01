# Created on 1 Nov 2016
# Created by: Matthew Lourenco
# this is a program that takes your name and arranges it.

def arrange_name(first, last, initial = ''):
    #arranges and prints name
    if initial == '':
        print(first + ' ' + last)
    else:
        print(first + ' ' + initial + '. ' + last)

first_name = raw_input('Enter your first name: ')
last_name = raw_input('Enter your last name: ')
while True:
    initial_choice = raw_input('Do you want to enter your middle initial? (y/n) ')
    if initial_choice == 'y':
        initial_name = raw_input('Enter your middle initial: ')
        arrange_name(first_name, last_name, initial = initial_name)
        break
    elif initial_choice == 'n':
        arrange_name(first_name, last_name)
        break
    else:
        print('Enter "y" or "n".')
