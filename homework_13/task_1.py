class Godzilla:

    def __init__(self, stomach_size):
        self.stomach_size = stomach_size

    def eat(self, size_people):
        occupancy_stomach = self.stomach_size
        full_stomach = occupancy_stomach * 0.1
        while occupancy_stomach > full_stomach:
            occupancy_stomach -= size_people
            if occupancy_stomach > full_stomach:
                print('I need more people')

        print('I\'m full, I can\'t eat people anymore')


Egor = Godzilla(100)

Egor.eat(40)
