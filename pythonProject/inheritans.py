
class Humen:
    species = "людина"

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Привіт мене звати {self.name}")

class Student(Humen):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def study(self):
        print(f"{self.name} вчиться в групі {self.group}")

class Worker(Humen):
    def work(self):
        print(f"{self.name} працює")

s = Student("Олена", "ПЗ-21")
s.say_hello()
s.study()
w = Worker("Bob")
w. say_hello()
w. work()
print(s.species)