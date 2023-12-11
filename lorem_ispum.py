# version 1 - genereting random sentences using random created words
import random as rd

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

parameter = int(input('Enter the number of sentences: '))   

empty_line_after = rd.randint(1, parameter)

with open('output.txt', 'w') as f:
    for i in range(parameter):
        sentence = ''
        for _ in range(rd.randint(5, 15)):
            word = ''
            for _ in range(rd.choices([1,2,3,4,5,6,7,8,9], [1,2,5,20,25,60,60,30,25])[0]):
                syllable = ''.join(rd.choice(abc) for _ in range(rd.randint(1, 3)))
                word = syllable + rd.choice(vowels)
            sentence += word + ' '
        final = sentence[0].upper() + sentence[1:-1] + '.'
        f.write(final + '\n')
        if i+1 == empty_line_after:
            f.write("\n")
            empty_line_after += rd.randint(4, 8)