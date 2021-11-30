class FizzBuzz():
    def game(self,liczba):
        if type(liczba)!=int:
            raise TypeError("Wrong data type")
        if liczba % 15 == 0:
            return ('"FizzBuzz"')
        elif liczba % 5 == 0:
            return ('"Buzz"')
        elif liczba % 3 == 0:
            return ('"Fizz"')
        elif liczba%15!=0 and liczba%5!=0 and liczba%3!=0:
            return ('"' + str(liczba) + '"')



import unittest

class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.temp=FizzBuzz()

    def test_FizzBuzz(self):
        self.assertEqual('"FizzBuzz"',self.temp.game(30))
    def test_Fizz(self):
        self.assertEqual('"Fizz"',self.temp.game(33))
    def test_Buzz(self):
        self.assertEqual('"Buzz"',self.temp.game(25))
    def test_Number(self):
        self.assertEqual('"' + str(22) + '"',self.temp.game(22))
    def test_exeption_list(self):
        self.assertRaises(TypeError,self.temp.game, [10])
    def test_exeption_str(self):
        self.assertRaises(TypeError,self.temp.game, "15")
    def test_exeption_None(self):
        self.assertRaises(TypeError,self.temp.game, None)
    def test_Float(self):
        self.assertRaises(TypeError,self.temp.game,None)
    def test_Minus(self):
        self.assertEqual('"FizzBuzz"',self.temp.game(-30))
    def test_FizzBuzz2(self):
        self.assertEqual('"FizzBuzz"',self.temp.game(30))
    def test_FizzBuzz3(self):
        self.assertEqual('"FizzBuzz"',self.temp.game(105))
    def test_FizzBuzz4(self):
        self.assertEqual('"FizzBuzz"',self.temp.game(-45))
    def test_FizzBuzz5(self):
        self.assertEqual('"FizzBuzz"',self.temp.game(120))
    def test_Fizz2(self):
        self.assertEqual('"Fizz"',self.temp.game(-9))
    def test_Fizz3(self):
        self.assertEqual('"Fizz"',self.temp.game(108))
    def test_Fizz4(self):
        self.assertEqual('"Fizz"',self.temp.game(-33))
    def test_Buzz2(self):
        self.assertEqual('"Buzz"',self.temp.game(500))
    def test_Buzz3(self):
        self.assertEqual('"Buzz"',self.temp.game(-25))
    def test_Buzz4(self):
        self.assertEqual('"Buzz"',self.temp.game(125))
    def test_Number2(self):
        self.assertEqual('"' + str(72139) + '"',self.temp.game(72139))
    def test_Number3(self):
        self.assertEqual('"' + str(92899) + '"',self.temp.game(92899))
    def test_Number4(self):
        self.assertEqual('"' + str(-104729) + '"',self.temp.game(-104729))


    def tearDown(self):
        self.temp=None