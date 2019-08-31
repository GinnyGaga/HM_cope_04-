import sys

def func2(a):
    print("in func2 1111: %d, value: %d" % (id(a), a ))
    a += 1
    print("in func2 2222: %d, value: %d, size: %d" % (id(a), a, sys.getsizeof(a) ))

def func1(a):
    print("in func 1111: %d, value: %d" % (id(a), a ))
    a += 1
    print("in func 2222: %d, value: %d, size: %d" % (id(a), a, sys.getsizeof(a) ))
    func2(a)

if __name__ == '__main__':
    i = 1
    print("in main 1111: %d, value: %d" % (id(i), i ))
    func1(i)
    print("in main 2222: %d, value: %d" % (id(i), i))
    j = 1
    print("in main 3333: %d, value: %d" % (id(j), j))
    k = 2
    print("in main 4444: %d, value: %d" % (id(k), k))



