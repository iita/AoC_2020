import csv

def count_trees(y, rows = 1):
    with open('day3_input.txt', 'r') as f:
        current_n = 0
        n_trees = 0
        fread = csv.reader(f, delimiter=' ')
        for rown, row in enumerate(fread):
            space = row[0]
            if current_n >= 31:
                space = space * (current_n // 31 + 1)
            if rown % rows == 0:
                tree = space[current_n]
                current_n = current_n + y
                if tree == '#':
                    n_trees = n_trees+1
        print(n_trees)
        return n_trees

print(count_trees(1,1) * count_trees(3,1) * count_trees(5,1) * count_trees(7,1) * count_trees(1,2))


