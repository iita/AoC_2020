import csv

with open('day2_input.txt', 'r') as f:
    total_count = 0
    total_count_2 = 0
    fread = csv.reader(f, delimiter=' ')
    for row in fread:
        min_ = int(row[0].split('-')[0])
        max_ = int(row[0].split('-')[1])
        letter = row[1].split(':')[0]
        pwd = row[2]
        result_ = pwd.count(letter)
        if( result_>= min_ and result_ <= max_):
            total_count = total_count + 1
        if (pwd[min_-1]==letter or pwd[max_-1]==letter) and not (pwd[min_-1]==letter and pwd[max_-1]==letter):
            total_count_2 = total_count_2 + 1
    print(total_count, total_count_2)


