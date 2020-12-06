import csv

def find_relevant_half(lower_, upper_, letter_):
    numbers_line = list(range(lower_, upper_+1))
    midway = numbers_line[len(numbers_line)//2]
    if letter_ in ['F', 'L']:
        midway = midway-1
        upper_ = midway
    else:
        lower_ = midway
    return(lower_, upper_, midway)

with open('day5_input.txt', 'r') as f:
    fread = csv.reader(f, delimiter=';')
    all_nrs = []
    for row in fread:
        lower_ = 0
        upper_ = 127
        for lettern, letter in enumerate(row[0]):
            if lettern == 7:
                row_n = new_
                lower_ = 0
                upper_ = 8
            lower_, upper_, new_ = find_relevant_half(lower_, upper_, letter)
        all_nrs.append(row_n * 8 + new_)
    all_nrs.sort()
    for x in range(1, len(all_nrs)):
        if all_nrs[x]-1 != all_nrs[x-1]:
                print(all_nrs[x-1] + 1)


