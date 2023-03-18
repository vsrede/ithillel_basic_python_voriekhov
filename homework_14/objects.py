class Vehicle:
    species = 'Vehicle'

    def __init__(self, brand, max_speed, color):
        self.brand = brand
        self.max_speed = max_speed
        self.color = color

    def message_tensile_strength(self):
        tensile_strength = self.max_speed * 1.2
        return f'''We do not recommend accelerating the vehicle above the maximum speed, the tensile strength at speed \
{tensile_strength} km/h is 0.5 of the rated'''

    def trigger_mechanism(self):
        return 'Button, key or more complex mechanism'


class AirVehicle(Vehicle):
    moving_environment = 'Sky'

    def __init__(self, *args, max_high, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_high = max_high

    def message_tensile_strength(self):
        tensile_strength = self.max_speed * 1.2 * 0.0008
        return f'''We do not recommend accelerating the vehicle above the maximum speed, the tensile strength at speed \
{tensile_strength} mach is 0.5 of the rated'''

    def trigger_mechanism(self):
        return 'Complex mechanism'


class Plane(AirVehicle):

    def __init__(self, *args, engine_layout, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine_layout = engine_layout


class Helicopter(AirVehicle):
    def __init__(self, *args, amount_blades, **kwargs):
        super().__init__(*args, **kwargs)
        self.amount_blades = amount_blades


class Car(Vehicle):

    def __init__(self, *args, engine_volume, mileage, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine_volume = engine_volume
        self.mileage = mileage

    def trigger_mechanism(self):
        return 'Key or button'


class FrenchCar(Car):

    def __init__(self, *args, suspension, **kwargs):
        super().__init__(*args, **kwargs)
        self.suspension = suspension

    @staticmethod
    def list_auto_repair_shop():
        return 'Nobody wan\'t repair your car'


class GermanyCar(Car):

    def list_auto_repair_shop(self):
        message = 'Your car is beautiful, you don\'t need to go there'

        if self.brand == 'BMW':
            return f'{message}, just change the oil'
        else:
            return message
