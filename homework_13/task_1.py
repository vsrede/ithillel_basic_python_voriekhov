"""
Classes:
        Godzilla: represents an object that accepts people and populates its stomach
            Attributes:  stomach_filled(default 0)
                        stomach_size(Stomach volume)

            Methods: eat(takes the volume of a person and fills the object of the class with this volume
                        if the occupancy is less than 90 percent)
            Functions: test(runs tests to find errors in the 'eat' method)
"""


class Godzilla:
    stomach_filled = 0

    def __init__(self, stomach_size):
        self.stomach_size = stomach_size

    def eat(self, human_size):
        max_stomach_filled = self.stomach_size * 0.9
        if self.stomach_filled + human_size > self.stomach_size:
            print(f'I can still eat, but give me a smaller person, my stomach is only full '
                  f'{self.stomach_filled / self.stomach_size * 100}%')
        elif max_stomach_filled < self.stomach_filled:
            print('I\'m full, I can\'t eat people anymore')
        else:
            self.stomach_filled += human_size
            print('I need more peoples')
            print(self.stomach_filled)


def test_godzilla():
    # Test eating a human smaller than stomach capacity
    godzilla = Godzilla(10)
    godzilla.eat(5)
    assert godzilla.stomach_filled == 5

    # Test eating a human larger than stomach capacity
    godzilla.eat(10)
    assert godzilla.stomach_filled == 5

    # Test eating a human that makes the stomach almost full
    godzilla.eat(4)
    assert godzilla.stomach_filled == 9

    # Test eating a human that fills the stomach to capacity
    godzilla.eat(1)
    assert godzilla.stomach_filled == 10

    # Test eating a human when the stomach is already full
    godzilla.eat(2)
    assert godzilla.stomach_filled == 10

    # Test eating multiple humans
    godzilla = Godzilla(15)
    godzilla.eat(5)
    godzilla.eat(5)
    godzilla.eat(3)
    assert godzilla.stomach_filled == 13

    print("__________All tests pass__________")


def main():

    test_godzilla()


if __name__ == '__main__':
    main()


