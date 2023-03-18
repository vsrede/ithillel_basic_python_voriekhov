from objects import Vehicle, AirVehicle, Plane, Helicopter, Car, FrenchCar, GermanyCar


def test_vehicle():
    example = Vehicle('BMW', 100, 'grey')
    assert example.brand == 'BMW', 'Result must be "BMW"'
    assert example.max_speed == 100, 'Result must be "100"'
    assert example.color == 'grey', 'Result must be "grey"'

    assert example.message_tensile_strength() == '''We do not recommend accelerating the vehicle above the maximum \
speed, the tensile strength at speed 120.0 km/h is 0.5 of the rated''', \
        '''Result must me "We do not recommend accelerating the vehicle above the maximum \
speed, the tensile strength at speed 120.0 km/h is 0.5 of the rated"'''

    assert example.trigger_mechanism() == 'Button, key or more complex mechanism'


def test_air_vehicle():
    example = AirVehicle('Airbus', 100, 'white', max_high=1000)
    assert example.brand == 'Airbus', 'Result must be "Airbus"'
    assert example.max_speed == 100, 'Result must be "100"'
    assert example.color == 'white', 'Result must be "white"'
    assert example.max_high == 1000, 'Result must be "1000"'
    assert example.message_tensile_strength() == '''We do not recommend accelerating the vehicle above the maximum \
speed, the tensile strength at speed 0.096 mach is 0.5 of the rated''', \
        '''Result must me "We do not recommend accelerating the vehicle above the maximum \
speed, the tensile strength at speed 0.096 mach is 0.5 of the rated"'''

    assert example.trigger_mechanism() == 'Complex mechanism', 'Result must be "Complex mechanism"'


def test_plane():
    example = Plane('Airbus', 100, 'white', max_high=1000, engine_layout='on the wing')
    assert example.brand == 'Airbus', 'Result must be "Airbus"'
    assert example.max_speed == 100, 'Result must be "100"'
    assert example.color == 'white', 'Result must be "white"'
    assert example.max_high == 1000, 'Result must be "1000"'
    assert example.engine_layout == 'on the wing', 'Result must be "on the wing"'


def test_helicopter():
    example = Helicopter('AK1-3', 100, 'black', max_high=1000, amount_blades=3)
    assert example.brand == 'AK1-3', 'Result must be "Airbus"'
    assert example.max_speed == 100, 'Result must be "100"'
    assert example.color == 'black', 'Result must be "white"'
    assert example.max_high == 1000, 'Result must be "1000"'
    assert example.amount_blades == 3, 'Result must be "3"'


def test_car():
    example = Car('daewoo', 100, 'green', engine_volume=1.5, mileage=1000000)
    assert example.brand == 'daewoo', 'Result must be "daewoo"'
    assert example.max_speed == 100, 'Result must be "100"'
    assert example.color == 'green', 'Result must be "green"'
    assert example.engine_volume == 1.5, 'Result must be "1.5"'
    assert example.mileage == 1000000, 'Result must be "1000000"'

    assert (example.trigger_mechanism()) == 'Key or button', 'Result must be "Key or button"'


def test_french_car():
    example = FrenchCar('renault', 100, 'green', engine_volume=1.5, mileage=1000000, suspension='air suspension')
    assert example.brand == 'renault', 'Result must be "daewoo"'
    assert example.max_speed == 100, 'Result must be "100"'
    assert example.color == 'green', 'Result must be "green"'
    assert example.engine_volume == 1.5, 'Result must be "1.5"'
    assert example.mileage == 1000000, 'Result must be "1000000"'
    assert example.suspension == 'air suspension', 'Result must be "air suspension"'

    assert (example.list_auto_repair_shop()) == 'Nobody wan\'t repair your car', \
        'Result must be "Nobody wan\'t repair your car"'


def test_germany_car():
    example = GermanyCar('volkswagen', 100, 'green', engine_volume=1.5, mileage=1000000)
    assert example.brand == 'volkswagen', 'Result must be "volkswagen"'
    assert example.max_speed == 100, 'Result must be "100"'
    assert example.color == 'green', 'Result must be "green"'
    assert example.engine_volume == 1.5, 'Result must be "1.5"'
    assert example.mileage == 1000000, 'Result must be "1000000"'

    assert (example.list_auto_repair_shop()) == '''Your car is beautiful, you don't need to go there''', \
        '''Result must be "Your car is beautiful, you don't need to go there"'''

    example = GermanyCar('BMW', 100, 'green', engine_volume=1.5, mileage=1000000)
    assert example.brand == 'BMW', 'Result must be "BMW"'
    assert example.max_speed == 100, 'Result must be "100"'
    assert example.color == 'green', 'Result must be "green"'
    assert example.engine_volume == 1.5, 'Result must be "1.5"'
    assert example.mileage == 1000000, 'Result must be "1000000"'

    assert (example.list_auto_repair_shop()) == '''Your car is beautiful, you don't need to go there, \
just change the oil''',\
        '''Result must be "Your car is beautiful, you don't need to go there, just change the oil"'''

    print('___________tests passed___________')


if __name__ == "__main__":
    # test_vehicle()
    # test_air_vehicle()
    # test_plane()
    # test_helicopter()
    # test_car()
    # test_french_car()
    test_germany_car()
    example = GermanyCar('volkswagen', 100, 'green', engine_volume=1.5, mileage=1000000)
