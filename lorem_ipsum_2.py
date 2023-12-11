# Version 2 - Generates random sentences using words from JSON file
# words.json from https://github.com/dwyl/english-words/tree/master


import random as rd
import json

#opening json file
with open('words.json', 'r') as f:
    words = json.load(f)

parameter = int(input('Enter the number of sentences: '))

empty_line_after = rd.randint(4, 8)

with open('output.txt', 'w') as f:
    for i in range(parameter):
        sentence = ''
        for _ in range(rd.randint(5, 15)):
            word = rd.choice(list(words.keys()))  # Get a random key from the dictionary
            sentence += word + ' '
        final = sentence[0].upper() + sentence[1:-1] + '.'
        f.write(final + '\n')
        if i+1 == empty_line_after:
            f.write("\n")
            empty_line_after += rd.randint(4, 8)