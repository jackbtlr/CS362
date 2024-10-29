from credit_card_validator import credit_card_validator
import unittest
import random

class TestCase(unittest.TestCase):
    pass

def generate_testcases(tests_to_generate=1000):
    pre = ['random.randint(4000,4999)', 'random.randint(5100,5599)', 'random.randint(2221,2720)', 'random.randint(3400,3799)', 'random.randint(0000,9999)']
    lengths = [14,15,16,17]
    for i in range(tests_to_generate):
        num = ''
        pre_index = random.randint(0,4)
        prefix = str(eval(pre[pre_index]))
        num += prefix
        
        length = lengths[random.randint(0,3)]
        while len(num) < length - 1:
            digit = random.randint(0,9)
            num += str(digit)
        
        check_sum = check_digit(num)
        # Add valid check digit 75% of the time, else invalid
        if random.random() > 0.25:
            num += str(check_sum)
        else:
            num += str((check_sum + 1) % 10)

        if random.random() > 0.95:
            num = ''

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