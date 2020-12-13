import re

with open('day10_input.txt', 'r') as f:
    wline = f.readlines()
    input_nrs = [int(re.sub('\n', '', x)) for x in wline]
    input_nrs.sort()
    print(input_nrs)

last_adapter = max(input_nrs)
current_jolts = 0
checked_adapters = []
not_ready = True
while not_ready:
    for adapter in input_nrs:
        print(checked_adapters)
        joltage_diff = adapter - current_jolts
        if joltage_diff in [1,2,3]:
            checked_adapters.append(joltage_diff)
            current_jolts = current_jolts + joltage_diff
            input_nrs.remove(adapter)
            print(adapter)
            if adapter == last_adapter:
                print(checked_adapters.count(1)*(checked_adapters.count(3)+1))
                not_ready = False
            break
