import pandas as pd

input_ = pd.read_csv('1974.txt', header=None)
print(input_)
input_.columns = ['nr']
input_large = input_[input_['nr']>1000]
input_small = input_[input_['nr']<=1000]

for i in input_small['nr']:
    for x in input_small['nr']:
        if i + x == 2020:
            print(i*x)
        for y in input_small['nr']:
            if i+x+y == 2020:
                print(i*x*y)

