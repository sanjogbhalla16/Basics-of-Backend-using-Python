# print even numbers in range


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        return i


print(even_generator(10))  # this will only print 2 read notes


def even_generator1(limit):
    for i in range(2, limit + 1, 2):
        yield i


for num in even_generator1(10):
    print(num)  # this will yield all the values
