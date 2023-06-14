# your code goes here!
# check for the import at top!
from time import sleep 

# def functions for countdown and countdown_with_sleep


def countdown(number):

# make sure the while and print are correct
    while number:
        print(f'{number} SECOND(S)!')
        number -= 1

    print('HAPPY NEW YEAR!')

def countdown_with_sleep(number):

    while number:
        print(f'{number} SECOND(S)!')
        number -= 1
# make sure this is here and passing an object  
        sleep(1)

    print('HAPPY NEW YEAR!')