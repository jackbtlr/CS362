from credit_card_validator import credit_card_validator
import unittest
import random

class TestCase(unittest.TestCase):
    pass

def generate_testcases(tests_to_generate=1000):
    card_types = ['visa', 'mc', 'amex', 'random']
    hashmap  = {
        'visa': {
            'prefix': ['random.randint(4000,4999)'],
            'length': {
                'valid': [16],
                'invalid': [15, 17]
            }
        },
        'mc': {
            'prefix': ['random.randint(5100,5599)', 'random.randint(2221,2720)'],
            'length': {
                'valid': [16],
                'invalid': [15, 17]
            }
        },
        'amex': {
            'prefix': ['random.randint(3400,3499)', 'random.randint(3700,3799)'],
            'length': {
                'valid': [15],
                'invalid': [14, 16]
            }
        },
        'random': {
            'prefix': ['5099', '5600', '2220', '2721', '3399', '3500', '3699', '3800'],
            'length': {
                'valid': [14,15,16,17],
                'invalid': [14,15,16,17]
            }
        }
        
    }

    for i in range(tests_to_generate):
        num = ''
        card = random.choice(card_types)
        prefix = str(eval(random.choice(hashmap[card]['prefix'])))
        num += prefix
        
        # 80% chance length is correct
        if random.random() > 0.2:
            length = random.choice(hashmap[card]['length']['valid'])
        else:
            length = random.choice(hashmap[card]['length']['invalid'])
        
        while len(num) < length - 1:
            digit = random.randint(0,9)
            num += str(digit)
        
        check_sum = check_digit(num)
        # Add valid check digit 75% of the time, else invalid
        if random.random() > 0.25:
            num += str(check_sum)
        else:
            num += str((check_sum + 1) % 10)

        new_test = build_test_func(num, credit_card_validator)
        setattr(TestCase, 'test_{}'.format(num), new_test)

def build_test_func(test_case, func_under_test):
    def test(self):
        func_under_test(test_case)
    return test
        

def check_digit(num):
    sum = 0
    i = len(num) - 1
    double = True
    while i >= 0:
        digit = int(num[i])
        if double:
            digit = str(digit * 2)
            if len(digit) == 2:
                sum += int(digit[0]) + int(digit[1])
            else:
                sum += int(digit)
        else:
            sum += digit
        double = not double
        i -= 1
    check_digit = (10 - (sum % 10)) % 10
    return check_digit    


if __name__ == '__main__':
    generate_testcases()
    unittest.main()