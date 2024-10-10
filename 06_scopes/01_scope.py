username = "chaiaurcode"


def func():
    # username = "chai"
    print(username)


print(username)
func()

x = 99


def func2(y):
    z = x + y
    return z


result = func2(1)
print(result)


def f1():
    x = 88

    def f2():
        print(x)

    f2()


f1()


def func(num):
    def actual(x):
        return x**num

    return actual


f = func(2)
g = func(3)

print(f(3))
print(g(3))
