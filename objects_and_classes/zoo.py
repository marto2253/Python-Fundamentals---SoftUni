class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"{species.capitalize()}es in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"

    # def get_info(self, species):
    #     result = ""
    #     if species == "mammal":
    #         result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
    #     elif species == "fish":
    #         result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
    #     elif species == "bird":
    #         result += f"Birds in {self.name}: {', '.join(self.birds)}"
    #
    #     result += f"\nTotal animals: {Zoo.__animals}"
    #     return result


name_of_the_zoo = input()
zoo = Zoo(name_of_the_zoo)
number = int(input())

for i in range(number):
    animal_info = input().split(" ")
    species = animal_info[0]
    name = animal_info[1]
    zoo.add_animal(species, name)

species_type = input()
print(zoo.get_info(species_type))
