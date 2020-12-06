import string
import re

with open('day6_input.txt', 'r') as f:
    wline = f.readlines()
    wline = ''.join(wline)
    wline = wline.split('\n\n')
    sum_total = 0
    for group in wline:
        person_inputs = re.sub("\n", "", group)
        n_letters = 0
        for letter in string.ascii_lowercase:
            if re.search(letter, person_inputs):
                n_letters += 1
        sum_total = sum_total + n_letters
    print(sum_total)


with open('day6_input.txt', 'r') as f:
    wline = f.readlines()
    wline = ''.join(wline)
    wline = wline.split('\n\n')
    sum_total = 0
    for group in wline:
        print(group)
        n_letters = 0
        person_inputs = group.split("\n")
        clean_group = re.sub("\n", "", group)
        for letter in string.ascii_lowercase:
            print(letter)
            if clean_group.count(letter) == len(person_inputs):
                n_letters += 1
            print(n_letters)
        sum_total = sum_total + n_letters
print(sum_total)


