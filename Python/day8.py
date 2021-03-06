import csv
import pandas as pd

with open('day8_input.txt', 'r') as f:
    list_of_lists = []
    fread = csv.reader(f, delimiter=' ')
    for rown, row in enumerate(fread):
        new_row = [rown, row[0], int(row[1])]
        list_of_lists.append(new_row)
    df = pd.DataFrame(list_of_lists)
    df.columns = ['rown', 'instruct', 'nrs']

def do_things(rown, accumulator):
    instruction = df.loc[df['rown']==rown, 'instruct'].iloc[0]
    numbers = df.loc[df['rown']==rown, 'nrs'].iloc[0]
    accumulator = accumulator
    if instruction == "jmp":
        rown = rown + numbers
    elif instruction == "acc":
        rown += 1
        accumulator += numbers
    else:
        rown += 1
    return rown, accumulator

used_numbers = []
accumulated = 0
rown = 0

last_nr = len(df)-1

def get_things(rown, accumulator):
    while (rown not in used_numbers) and (rown<=last_nr):
        used_numbers.append(rown)
        rown, accumulator = do_things(rown, accumulator)
    if rown > last_nr:
        print('last_row')
        print(accumulator)
        return False
    return rown, accumulator


def change_things(n):
    current_instruct = df.loc[df['rown'] == n, 'instruct'].iloc[0]
    if current_instruct == "nop":
        df.loc[(df['rown'] == n), 'instruct'] = "jmp"
    elif current_instruct == "jmp":
        df.loc[(df['rown'] == n), 'instruct'] = "nop"


print(df.head(10))
for n in range(len(df)):
    print(n)
    used_numbers = []
    change_things(n)
    if get_things(0,0) == False:
        print('found ', n)
        break
    else:
        change_things(n)

