import csv
import re
import json

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

req_dict = {"byr": ":(19[2-9][0-9]|200[0-2])(\s|$)",
            "iyr": ":(201[0-9]|2020)(\s|$)",
            "eyr": ":(202[0-9]|2030)(\s|$)",
            "hgt": ":((1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in))(\s|$)",
            "hcl": ":#[0-9a-f]{6}(\s|$)",
            "ecl": ":(amb|blu|brn|gry|grn|hzl|oth)(\s|$)",
            "pid": ":[0-9]{9}(\s|$)"}


with open('day4_input.txt', 'r') as f:
    valid_lines = 0
    valid_2 = 0
    wline = f.readlines()
    wline = ''.join(wline)
    wline = wline.split('\n\n')
    for l in wline:
        l = re.sub('\n', ' ', l)
        l = ' ' + l
        sets = set(re.findall('\s([a-z]+):', l))
        if(required_fields.issubset(sets)):
            valid_lines = valid_lines + 1
            required = 0
            for r in required_fields:
                if (re.findall(r + req_dict[r], l)):
                    required = required + 1
            if required == 7:
                valid_2 = valid_2 + 1

print(valid_lines, valid_2)