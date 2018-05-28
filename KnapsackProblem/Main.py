import time
start_time = time.time()


def get_bit(num, n):
    return (num >> n) & 1


def sum_of(bits, items, column):
    _sum = 0
    for n, v in enumerate(bits):
        if v:
            _sum += items[n][column]
    return _sum


def sum_weights(bits, items):
    return sum_of(bits, items, 1)


def sum_values(bits, items):
    return sum_of(bits, items, 0)


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

char_vector = []

print("Capacity:", capacity)
print("Items:", items)

# generate characteristic vector and find maximum value

current_max = 0
current_best_solution = None

for v in range(possibilities):
    binary = bin(v)
    bits = [False for i in range(item_number)]
    t_vector = v
    for i in range(item_number):
        bits[item_number - 1 - i] = True if t_vector & 1 else False
        t_vector = t_vector >> 1
    sum_of_weights = sum_weights(bits, items)
    if sum_of_weights < capacity:
        char_vector.append(v)
        sum_of_values = sum_values(bits, items)
        if sum_of_values > current_max:
            current_max = sum_of_values
            current_best_solution = bits

print("New vector: \n", char_vector)
print("Removed", possibilities - len(char_vector), "potential solutions")
print("Best solution is ", current_best_solution, "with value of", current_max)

print("it took %s seconds for a program" % (time.time() - start_time))
