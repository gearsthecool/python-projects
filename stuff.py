score = 0

def nc_capital():

    print (''' What is the capital of North Carolina? ''')
    answer = input('> ')

    if answer == 'Charlotte':
        print( 'Wrong, but a lot of people think that.')
    elif answer == 'Durham':
        print('''Nope, but it's close.''')
    elif answer == 'Raleigh':
        print("Correct! You actually know something.")
        return 1
    else:
        print('Incorrect.')
        return 0
        
def favorite_color ():

    print('''
    What is your favorite color?
    ''')

    answer = input('> ')

    if answer == 'red':
        print('Correct')
        return 1
       
    elif answer == 'what is your quest?':
        print('You got the reference')
    else:
        print('Incorrect.')
        return 0
        

quiz_items = [
    favorite_color,
    nc_capital
]

import random

while quiz_items:
    quiz_item = random.choice(quiz_items)
    correct = quiz_item()
    if correct:
        quiz_items.remove(quiz_item)
    if points:
        score += points
        quiz_items.remove(quiz_item)
