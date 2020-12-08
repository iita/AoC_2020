import csv
import re
import pandas as pd
import math

with open('day7_input_test.txt', 'r') as f:
    current_n = 0
    outer_bags = []
    inner_bags = []
    numbers_col = []
    n_trees = 0
    fread = csv.reader(f, delimiter='|')
    for row in fread:
        row = row[0].split('contain')
        containing_bag = re.sub(' bags ', '', row[0])
        outer_bags.append(containing_bag)
        contained_bags = re.findall("[0-9] ([a-z\s]+) bag", row[1])
        number_bags = re.findall(" ([0-9]+) ", row[1])
        numbers_col.append(number_bags)
        inner_bags.append(contained_bags)
    bags = pd.DataFrame([outer_bags, inner_bags, numbers_col]).T
    bags.columns = ['outer_bag', 'inner_bag', 'n_bags']



def get_valid(bag_colours):
    all_valid = []
    while bag_colours:
        mask = bags.inner_bag.apply(lambda x: any(item for item in bag_colours if item in x))
        valid_bags = bags[mask]
        all_valid = all_valid + bag_colours
        all_valid = list(set(all_valid))
        bag_colours = list(valid_bags['outer_bag'])

    return set(all_valid)



valid = get_valid(["shiny gold"])
print(len(valid))

print(bags.head())
bags['count_col'] = bags['inner_bag'].apply(len)
print(bags.head())

def get_tuple(bag_colour):
    bag_tuples = []
    valid_bags = bags[bags['outer_bag'] == bag_colour]
    bag_colours = valid_bags.inner_bag.explode().tolist()
    bag_numbers = valid_bags.n_bags.explode().tolist()
    count_col = valid_bags.count_col.explode().tolist()
    for x in range(count_col[0]):
        bag_tuples.append((bag_colours[x], bag_numbers[x]))
    return bag_tuples

n = get_tuple("faded blue")
print(n)

def count_bags(bag_colour):
    bag_total = 0
    bag_tuple = get_tuple(bag_colour)
    n_bags = bags.loc[bags['outer_bag'] == bag_colour, 'count_col']
    while bag_tuple:
        print(bag_tuple)
        for x in bag_tuple:
            print(x[0])
            bag_total = bag_total + n_bags * int(x[1])
            count_bags(x[0])
            print(bag_total)
    print(n_bags)


#count_bags("shiny gold")

