def get_bit(num, n):
    return (num >> n) & 1


print(get_bit(2, 3))
