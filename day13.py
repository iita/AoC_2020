
with open('day13_test.txt', 'r') as f:
    timestamp = int(f.readline())
    buses = f.readline()
    buses = buses.split(',')
    print(buses)

buses_ = [int(b) for b in buses if b!= 'x']
arrival_times = {}
for b in buses_:
    b_t = b
    while b_t <= timestamp:
        b_t += b
    arrival_times[b_t] = b

earliest = min(arrival_times.keys())
total = (earliest-timestamp)*arrival_times[earliest]

