import math


def contrived_func(val):

    # a = val + math.sqrt(abs(val*3)) >= 23
    # b = val ** 3 % 2 != 0
    # c = val * 6 - 14 < 107
    # d = val ** 3 < 0
    a = False
    b = True
    c = True
    d = False

    if a or b:
        if (a and b) or (b and c) and d:
            pass
        else:
            pass
    else:
        if (a or b) or (b or c):
            pass
        else:
            pass
    
    if a and b:
        pass
    else:
        pass

if __name__ == '__main__':
    contrived_func(3)