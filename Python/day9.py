import csv

test_n = 5

with open('day9_test.txt', 'r') as f:
    current_n = 0
    previous_numbers = []
    all_numbers = []
    fulfills_rule = True
    fread = csv.reader(f, delimiter=' ')
    for rown, row in enumerate(fread):
        current_n = int(row[0])
        if rown <= test_n-1:
            previous_numbers.append(current_n)
            all_numbers.append(current_n)
        else:
            for prev_n in range(test_n):
                if current_n - previous_numbers[prev_n] in previous_numbers[prev_n:]:
                    break
                if prev_n == test_n-1:
                    print(current_n)
                    valid_numbers = []
                    for c_nr in range(len(all_numbers)):
                        pass
                    break
            previous_numbers.pop(0)
            previous_numbers.append(current_n)
            all_numbers.append(current_n)
