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
    bag_dict = {}
    fread = csv.reader(f, delimiter='|')
    for row in fread:
        row = row[0].split('contain')
        containing_bag = re.sub(' bags ', '', row[0])
        outer_bags.append(containing_bag)
        contained_bags = re.findall("[0-9] ([a-z\s]+) bag", row[1])
        number_bags = re.findall(" ([0-9]+) ", row[1])
        numbers_col.append(number_bags)
        inner_bags.append(contained_bags)
        bag_dict[containing_bag] = {}
        for b in range(len(contained_bags)):
            bag_dict[containing_bag][contained_bags[b]] = int(number_bags[b])
    bags = pd.DataFrame([outer_bags, inner_bags, numbers_col]).T
    bags.columns = ['outer_bag', 'inner_bag', 'n_bags']

print(bag_dict)


def get_valid(bag_colours):
    all_valid = []
    while bag_colours:
        mask = bags.inner_bag.apply(lambda x: any(item for item in bag_colours if item in x))
        valid_bags = bags[mask]
        all_valid = all_valid + bag_colours
        all_valid = list(set(all_valid))
        bag_colours = list(valid_bags['outer_bag'])

    return set(all_valid)


#valid = get_valid(["shiny gold"])

def get_count(bag_colour):
    bags_in = bag_dict[bag_colour]
    bag_c = 0
    for b in bags_in.keys():
        kerroin = bags_in[b]
        n_bags = 0

get_count('shiny gold')