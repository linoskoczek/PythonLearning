import random


def binary_search_traditional(sequence, key, start, end):
    current = (end + start) // 2
    if len(sequence) == 0 or end - start < 0 or current < 0:
        return -1
    else:
        if sequence[current] == key:
            return current
        if sequence[current] < key:
            return binary_search_traditional(sequence, key, current + 1, end)
        if sequence[current] > key:
            return binary_search_traditional(sequence, key, start, current - 1)


empty = ()
data = random.sample(range(10), 8)
data.sort()
print('Working on: ', data)

# tests

result = binary_search_traditional(empty, 5, 0, len(empty))
print('Search result for 5 (in empty tuple):', result)
assert result == -1

result = binary_search_traditional(data, 5, 0, len(data))
print('Search result for 5:', result)
if 5 in data:
    assert result >= 0
else:
    assert result == -1

result = binary_search_traditional(data, 1, 0, len(data))
print('Search result for 1:', result)
if 1 in data:
    assert result >= 0
else:
    assert result == -1

result = binary_search_traditional(data, -123, 0, len(data))
print('Search result for -123:', result)
assert result == -1
