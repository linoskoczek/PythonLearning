import time
start_time = time.time()


def get_bit(num, n):
    return (num >> n) & 1


def sum_w_v(vector):
    sum_values = 0
    sum_weights = 0
    for b in range(item_number):
        if get_bit(vector, b) == 1:
            sum_values += items[b][0]
            sum_weights += items[b][1]

    if sum_weights > capacity:
        return None
    return sum_values


capacity = None

items = []

# load items

for i, line in enumerate(open('15small')):
    if i == 0:
        capacity = int(line.rstrip())
    else:
        data = line.rstrip().split(' ')
        data[0] = int(data[0])
        data[1] = int(data[1])
        items.append(data)

# generate characteristic vector parameters

item_number = len(items)
possibilities = 2 ** item_number

print("Capacity:", capacity)
print("Items:", items)

# generate characteristic vector and find maximum value

current_max = 0
current_best_solution = None

for v in range(possibilities):
    result = sum_w_v(v)
    if result is not None and result > current_max:
        current_max = result
        current_best_solution = v

print("Best solution is ", bin(current_best_solution), "with value of", current_max)

print("it took %s seconds for a program" % (time.time() - start_time))
