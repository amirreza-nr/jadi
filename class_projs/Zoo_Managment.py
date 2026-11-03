class Animal:
    zoo_name = "eram"

    def __init__(self,name,species,age,sound) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        return self.sound

    def info(self):
        print("name:" ,self.name)
        print("species:",self.species)
        print("age:",self.age)
        print("sound:",self.sound)

    def __str__(self) :
            return f"name: {self.name}, species: {self.species}, age: {self.age}, sound: {self.sound}"

class bird(Animal):
    def __init__(self, name, species, age, sound,wing_span) -> None:
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    def make_sound(self):
        return "some bird sound"


lion = Animal("amirreza","Iranian","20","growl")
parrot = bird("ali","persion","22","bird sound","15")

print("lion sound:",lion.make_sound())
print("info".center(50,'-'))
lion.info()
print("-------------------------------------------------")
print("bird sound:",parrot.make_sound())
print(parrot)
