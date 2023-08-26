class Vehicle:
    def __init__(
        self, brand: str, model: str, type: str, fuel_tank_size: int, fuel_level: float
    ):
        self.brand = brand
        self.model = model
        # type name conflict in problem statement
        self.type = type
        self.fuel_tank_size = fuel_tank_size
        self.fuel_level = fuel_level

    def Fulltank(self):
        """Fully fill the tank"""

        self.fuel_level = self.fuel_tank_size
        print("Tank is Full")

    def Update_fuel_tank(self, new_level: float):
        """Refuel your vehicle"""

        self.fuel_level = new_level

        if self.fuel_level <= 3:
            print("Warning! Your vehicle's fuel level is below 3 Litres.")
            print("Consider refueling your vehicle.")

    def Get_fuel(self, amount: float):
        new_fuel_level = self.fuel_level + amount
        if new_fuel_level > self.fuel_tank_size:
            print(
                f"Warning! You are exceeding your vehicle's fuel tank capacity of {self.fuel_tank_size} Litres."
            )
        else:
            self.fuel_level = new_fuel_level

    def Drive(self):
        print(f"WOW! I am Driving a {self.model}.")


class Sedan(Vehicle):
    def __init__(self, brand: str, model: str, fuel_tank_size: int, fuel_level: float):
        Vehicle.__init__(self, brand, model, "Sedan", fuel_tank_size, fuel_level)

    def Drive(self):
        print(
            f"WOW! I am Driving a {self.brand} {self.model} Sedan. It's so sleek and comfy."
        )


class SUV(Vehicle):
    def __init__(self, brand: str, model: str, fuel_tank_size: int, fuel_level: float):
        Vehicle.__init__(self, brand, model, "SUV", fuel_tank_size, fuel_level)

    def Drive(self):
        print(
            f"WOW! I am Driving a {self.brand} {self.model} SUV. It's so big and brawny."
        )


def main():
    vehicle_1 = Vehicle("Hyundai", "Creta", "Compact SUV", 42, 22)
    vehicle_2 = Vehicle("Suzuki", "Swift", "Compact Sedan", 27, 15)

    vehicle_1.Fulltank()
    vehicle_1.Update_fuel_tank(new_level=1)
    vehicle_1.Get_fuel(amount=56)
    vehicle_1.Drive()

    vehicle_2.Fulltank()
    vehicle_2.Update_fuel_tank(new_level=0.5)
    vehicle_2.Get_fuel(amount=73)
    vehicle_2.Drive()

    a_sedan = Sedan("Hyundia", "Elantra", 33, 12)
    a_sedan.Drive()

    a_suv = SUV("Mahindra", "Scorpio N", 48, 35)
    a_suv.Drive()


if __name__ == "__main__":
    main()
