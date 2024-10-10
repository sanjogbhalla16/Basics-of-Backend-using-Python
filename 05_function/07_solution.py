def sum_all(*args):
    print(args)  # this is a tuple
    for i in args:
        print(i * 2)
    return sum(args)


print(sum_all(1, 2, 3))
