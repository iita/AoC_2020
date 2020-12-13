def get_direction(current_direction, amount, turn):
    directions = ['N', 'E', 'S', 'W']
    n_turns = amount // 90
    if turn == 'R':
        current_index = (directions.index(current_direction) + n_turns) % 4
    else:
        current_index = (directions.index(current_direction) - n_turns) % 4
    new_direction = directions[current_index]
    return new_direction


with open('day12_input.txt', 'r') as f:
    x = 0
    y = 0
    current_direction = 'E'
    while True:
        line = f.readline()
        if not line:
            break
        direction = line[0]
        amount = int(line[1:])
        if direction == 'F':
            direction = current_direction
        if direction == 'E':
            x += amount
        elif direction == 'N':
            y += amount
        elif direction == 'W':
            x -= amount
        elif direction == 'S':
            y -= amount
        elif direction in ['R', 'L']:
            current_direction = get_direction(current_direction, amount, direction)
        print(line, current_direction, x,y)
    print(abs(x) + abs(y))
