def my_fun(arg1,*argv):
    print("primul argument",arg1)
    for arg in argv:
        print("next argument through *argv:",arg)


my_fun('halo','world','to','python')


def my_func(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

my_func(first='B', mid='to', last='C')

fib = lambda n : n if n <= 1 else fib(n-1)+fib(n-2)
result=fib(10)
print(result)


def ultimul_fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a

rezultat = ultimul_fibonacci(10)
print(rezultat)