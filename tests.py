from credit_card_validator import credit_card_validator
import unittest
import random


class TestCase(unittest.TestCase):
    def test1(self):
        credit_card_validator('9694216571825987')
    
    def test2(self):
        credit_card_validator('2333014828757943')
    
    def test3(self):
        credit_card_validator('1114567890223455')
    
    def test4(self):
        credit_card_validator('1184567890223450')

if __name__ == '__main__':
    unittest.main()
