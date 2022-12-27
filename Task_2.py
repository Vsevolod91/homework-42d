from functools import reduce

#1
def moving_zero(numbers):

    for n in numbers:
        if n == 0:
            numbers.pop(numbers.index(n))
            numbers.append(0)

    return numbers

#2
def row_sum_of_pyramid_1(num_row):
    return num_row**3

def row_sum_of_pyramid_2(num_row):
    numbers = (x for x in range(1, 1_000_000_000) if x % 2 != 0)
    quantity = reduce(lambda x, y: x + y, [x for x in range(1, num_row)])

    sum = 0
    for i in range(1, quantity + num_row + 1):
        if i <= quantity:
            next(numbers)
            continue
        sum += next(numbers)

    return sum

assert moving_zero([10, 0, 22, 0, 0, 15, 15, 2, 7, 0, 13, 0, 12]) == [10, 22, 15, 15, 2, 7, 13, 12, 0, 0, 0, 0, 0]
assert row_sum_of_pyramid_1(100) == row_sum_of_pyramid_2(100)
assert row_sum_of_pyramid_1(5) == row_sum_of_pyramid_2(5)
print("Succesfully")


