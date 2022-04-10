class Person:  # Person is class, obj is an object and age, names are attributes
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.both_names = self.first_name + self.last_name


obj = Person("Ivan", "Petrov")

print(obj)