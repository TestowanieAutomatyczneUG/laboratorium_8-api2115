import unittest
from sample.FizzBuzz import *
from parameterized import parameterized, parameterized_class

class FizzBuzz_Test1(unittest.TestCase):

    def setUp(self):
        self.tmp = FizzBuzz()

    @parameterized.expand([
        (-5, '"Buzz"'),
        (-3, '"Fizz"'),
        (-45, '"FizzBuzz"'),
        (198,'"Fizz"'),
        (230, '"Buzz"'),
        (300,'"FizzBuzz"'),
        (22,'"22"'),
        (-131,'"-131"')
    ])
    def test_one(self,number, expected):
        self.assertEqual(self.tmp.game(number), expected)

    @parameterized.expand([
        ("a",Exception),
        ([15],Exception),
        (set(),Exception)
    ])
    def test_two(self,item,error):
        self.assertRaises(error,self.tmp.game,item)

#dodatkowe
@parameterized_class(('number', 'expected'), [
    (5, '"Buzz"'),
    (3, '"Fizz"'),
    (15, '"FizzBuzz"'),
    (21,'"Fizz"'),
    (100, '"Buzz"'),
    (101, '"101"'),
    (-15,'"FizzBuzz"'),
    (-151, '"-151"')
])
class FizzBuzz_Test_Class1(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.game(self.number), self.expected)

@parameterized_class(('number',"error"),[
    ("15", Exception),
    ([],Exception),
    (None,Exception)
])
class FizzBuzz_Test_ClassError(unittest.TestCase):
    def setUp(self):
        self.tmp=FizzBuzz()

    def test_FizzBuzz_Error(self):
        self.assertRaises(self.error,self.tmp.game,self.number)


