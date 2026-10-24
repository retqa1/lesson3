class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __inint__(self, brand):
        self.brand = brand
        self.spassenger = []


    def add_passengers(self, *humans):
        for h in humans:
        self.passengers.append(h)


    def print_passengers(self):
        if not self.spassenger:
            print(f"В авто {self.brand} немає пасажирів!")
            return
    print(f"Пасажири {self.brand}:")
    for p in self.passengers:
        print(" -", p.name)

car = Auto("Toyota")
bob = Human("Bob")
kate = Human("Kate")
car.print_passengers()
car.add_passengers(bob, kate)
car.print_passengers()