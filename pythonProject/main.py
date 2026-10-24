# print("Hello")

# name = "DIMA"
# print(int(name)*10)

# age = 15
# print(age)

class Stdent:
    def __inif__(self, name="Невідомий", height=160):
        self.name = name
        self.name = height

    def grow(self, cm):
        self.height += cm
        print(f"{self.name} виріс, зріс {self.height}")

    def __str__(self):
        return f"Студент {self. name}, його зріст - {self. height}"

    def __del__(self):
        print(f"Студент {self.name} видалено!")

Bob = Stdent("Bob", 150)
Kate = Stdent("Kate", 160)