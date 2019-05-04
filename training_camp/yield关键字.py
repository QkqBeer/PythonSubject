# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         #print(b)
#         yield b
#         a,b = b,a+b
#         n += 1
#
# f = fib(5)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())


# def fib():
#     a, b = 0, 1
#     while 1:
#         print(b)
#         yield b
#         a, b = b, a + b
#
# f = fib()
# f.__next__()
# f.__next__()
# f.__next__()
# f.__next__()
# f.__next__()
# f.__next__()
# f.__next__()

def fibb():
    a,b=0,1
    while 1:
        print(b)
        yield b
        a,b = b, a + b
f = fibb()
f.__next__()
f.__next__()
f.__next__()
f.__next__()
f.__next__()
f.__next__()
f.__next__()