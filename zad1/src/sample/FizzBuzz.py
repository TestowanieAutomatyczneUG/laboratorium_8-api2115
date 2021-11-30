class FizzBuzz():
    def game(self,liczba):
        if liczba % 15 == 0:
            return ('"FizzBuzz"')
        elif liczba % 5 == 0:
            return ('"Buzz"')
        elif liczba % 3 == 0:
            return ('"Fizz"')
        elif liczba%15!=0 and liczba%5!=0 and liczba%3!=0:
            return ('"' + str(liczba) + '"')
        else:
            raise Exception("Error in FizzBuzz")