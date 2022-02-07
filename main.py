import random
import string
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'furry', 'troublesome',
              'noble', 'phone', 'banana', 'teacher', 'alphabetical', 'wavy',
              'frustrating', 'knighted', 'calm', 'abnormal', 'naked', 'coloquial',
              'sensless', 'unarmed', ' anemic', 'golden']

colours = ['green', 'red', 'orange', 'yellow', 'blue', 'purple', 'white']

nouns = ['apple', 'dinosaur', 'ball',
         'toaster', 'goat', 'dragon',
         'hammer', 'duck', 'panda', 'friend', 'being']

print('Welcome to your password selector!')

while True:

    for num in range(3):
        adjective = random.choice(adjectives)
        colour = random.choice(colours)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)

        password = adjective + colour + noun + str(number) + special_char
        print('Your new password is: %s' % password)

    response = input('Do you want another password? Anwser y or n: ')
    if response == 'n':
        break