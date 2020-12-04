import csv
import re
import json


with open('day4_input.txt', 'r') as f:
    list_of_sets = []
    wline = f.readlines()
    wline = ''.join(wline)
    wline = wline.split('\n\n')
    for l in wline:
        l = re.sub('\n', ' ', l)
        l = ' ' + l
        sets = set(re.findall('\s([a-z]+):', l))
        list_of_sets.append(sets)

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
n_sets = 0
for s in list_of_sets:
    if(required_fields.issubset(s)):
        n_sets = n_sets + 1
    print(n_sets)

