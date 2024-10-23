import math

def sandbox(val):
    a = val + math.sqrt(abs(val*3)) >= 23
    b = val ** 3 % 2 != 0
    c = val * 6 - 14 < 107
    d = val ** 3 < 0

    print('val:', val)
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)



if __name__ == '__main__':
    val = 19
    sandbox(val)