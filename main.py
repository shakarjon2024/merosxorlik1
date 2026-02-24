
# 1
class Vehicle:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model= model
        self.year= year
        self.color = color

    def start_engine(self):
        return f"{self.brand} {self.model} dvigateli ishga tushdi"


    def stop_engine(self):
        return f"{self.brand} {self.model} dvigateli ochirildi"


    def get_info(self):
        return f"Yil: {self.year}, Modeli: {self.model}, Brendi: {self.brand}, Rang: {self.color}."


    def honk(self):
        return f"{self.brand} {self.model} signal chaldi"


class Car(Vehicle):
    def __init__(self, brand, model, year, color,  fuel_type, doors):
        super().__init__(brand, model, year, color)
        self.fuel_type = fuel_type
        self.doors = doors


    def honk(self):
        return f"{self.brand} {self.model}"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, color,  has_sidecar, engine_type):
        super().__init__(brand, model, year, color)
        self.has_sidecar = has_sidecar
        self.engine_type = engine_type


    def honk(self):
        return f"{self.brand} {self.model}"



class Truck(Vehicle):
    def __init__(self, brand, model, year, color, load_capacity, trailer_attached):
        super().__init__(brand, model, year, color)
        self.load_capacity = load_capacity
        self.trailer_attached = trailer_attached


    def honk(self):
        return f"{self.brand} {self.model}"


car1 = Car('bmw', 'M5', 1970, 'qora', 'Elektir', 4)
car2 = Car('mers', '2', 1956, 'oq', 'Benzin', 3)

moto1 = Motorcycle("....",  "...", 2026, 'qora', '..', 'Sport')
moto2 = Motorcycle("....",  "...", 2016, 'qora', '..', 'Sport')

truck1 = Truck("....", "....", 2010, "seriy", '...', '.....')
truck2 = Truck("....", "....", 2000, "kok", '...', '.....')


vehicles = [car1, car2, moto1, moto2, truck1, truck2]

for v in vehicles:
    v.start_engine()
    v.honk()
    v.get_info()
    print(",,,")






# 2
class Animal:
    def __init__(self, name, age, species, habitat):
        self.name = name
        self.age = age
        self.species = species
        self.habitat = habitat


    def make_sound(self):
        return f"Ovozi: {self.species}"

    def eat(self):
        return f"Ovqatlanish usuli: {self.habitat}"

    def slepp(self):
        return f"Uxlash joyi: {self.habitat}"

    def move(self):
        return f"Harakatlanishi: "


class Dog(Animal):
    def __init__(self, name, age, species, habitat, breed, is_trained):
        super().__init__(name, age, species, habitat)
        self.breed = breed
        self.is_trained = is_trained


    def move(self):
        return f"{self.name}, {self.age}"


class Cat(Animal):
    def __init__(self, name, age, species, habitat, color, is_indoor):
        super().__init__(name, age, species, habitat)
        self.color = color
        self.is_indoor = is_indoor


    def move(self):
        return f"{self.name}, {self.age}"



class Bird(Animal):
    def __init__(self, name, age, species, habitat, can_fly, wing_span):
        super().__init__(name, age, species, habitat)
        self.can_fly = can_fly
        self.wing_span = wing_span


    def move(self):
        return f"{self.name}, {self.age}"



class Fish(Animal):
    def __init__(self, name, age, species, habitat, water_type, tank_size):
        super().__init__(name, age, species, habitat)
        self.water_type = water_type
        self.tank_size = tank_size


    def move(self):
            return f"{self.name}, {self.age}"



dog = Dog('Reks', 3, ',,,', ',,,', '...', '..')

cat = Cat('Masha', 2, '...', '...',  "oq", '...')

bird = Bird('Bobby', 4, "....", '...', ',,,,', ',,,')

fish = Fish('Suzy', 1, ',,,', "...", '...', "...")


animal = [dog, cat, bird, fish]


for a in animal:
    print(a.eat())
    print(a.make_sound())
    print(a.slepp())
    print(a.move())
