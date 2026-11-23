import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
        if die1 == die2:
            print("Lucky! You got a double!")
    elif choice == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Invalid input!')
