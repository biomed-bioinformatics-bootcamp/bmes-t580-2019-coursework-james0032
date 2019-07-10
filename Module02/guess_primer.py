import random
import re

print('---------------------------------')
print('   GUESS THAT PRIMER GAME')
print('---------------------------------')
print()

primer_length = 5
goal = ''.join(random.choice(['A', 'C', 'G', 'T']) for idx in range(primer_length))
print(goal)

guess = ''

name = input('Player what is your name? ')
guess = input('Guess a 5 bp sequence (only capital letter [ACGT] will be allowed): ')
while guess != goal:
    guess = input('Not right. Try again: ')
    misses = 0
    letter_check = re.compile('^[ACGT]*$')

    assert letter_check.match(guess)
    for il, gl in zip(guess, goal):
        if il != gl:
            misses+=1
    if misses == 0:
        pass
print('Congrats! The primer sequence is %s!' % goal)

print('done')