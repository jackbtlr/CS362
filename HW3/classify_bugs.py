import json
from tests import check_digit

def classify_bugs(bugs):
    cases = {}
    for k, v in bugs.items():
        cases[k] = {}
        for num in v:
            case = analyze_bug(num)
            if case not in cases[k]:
                cases[k][case] = [num]
            else:
                cases[k][case].append(num)
    return cases

def analyze_bug(num):
    res = ''
    if num[0] == '4':
        res += 'visa,'
    elif num[0:2] == 34 or num[0:2] == 37:
        res += 'amex,'
    elif 51 <= int(num[0:2]) <= 55 or 2221 <= int(num[0:4]) <= 2720:
        res += 'mastercard,'
    else:
        res += 'random,'

    res += f'length={len(num)},'

    if str(check_digit(num[:-1])) == num[-1]:
        res += 'valid'
    else:
        res += 'invalid'
    
    return res


if __name__ == '__main__':
    bugs = {}
    current = ''
    with open('./HW3/bugs.txt', 'r') as f:
        for l in f:
            t = l.strip()
            if t[0] == 'B':
                bugs[t] = []
                current = t
            else:
                bugs[current].append(t)
    cases = classify_bugs(bugs)
    print(json.dumps(cases, indent = 4))
        