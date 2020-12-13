import csv
import pandas as pd

with open('day11_input.txt', 'r') as f:
    list_all = []
    fread = csv.reader(f, delimiter=' ')
    for row in fread:
        list_all.append([char for char in row[0]])

input_df = pd.DataFrame(list_all)

print(input_df.head(200))


def adjust_seats():
    to_occupied = []
    to_empty = []
    for x in range(len(input_df)):
        for y in range(len(input_df.columns)):
            current_state = input_df.iloc[x,y]
            if current_state == '.':
                continue
            nearby_seats_x = range(x-1, x+2)
            nearby_seats_y = range(y-1, y+2)
            potential_x = [val for val in nearby_seats_x if (val>=0 and val < len(input_df))]
            potential_y = [val for val in nearby_seats_y if( val>=0 and val < len(input_df.columns))]
            seat_vals = ([item for sublist in input_df.iloc[potential_x, potential_y].values for item in sublist])
            seat_vals.remove(current_state)
            empty_adjacent = seat_vals.count('L')
            occupied_adjacent = seat_vals.count('#')
            if current_state == 'L' and occupied_adjacent==0:
                to_occupied.append((x,y))
            elif current_state == '#' and occupied_adjacent>=4:
                to_empty.append((x,y))
    for seat in to_empty:
        input_df.iloc[seat] = 'L'
    for seat in to_occupied:
        input_df.iloc[seat] = '#'
    if to_empty or to_occupied:
        return True
    return False

change_seats = True
iterations = 0
while change_seats:
    iterations +=1
    print(iterations)
    change_seats = adjust_seats()
print(input_df)


all_seats = [item for sublist in input_df.values for item in sublist]
final_occupied = all_seats.count('#')
print(final_occupied)