class Animal:
    def __init__(self, name, weight):
        self.name = name
	    self.weight = weight

	def eat(self):
        print('{0} накормлен'.format(self.name))
	

    def say(self):
    pass
    def get(self):
    pass

class Korova(Animal):
    def say(self):
        print('{0} сказала Myyy'.format(self.name))
    def get(self):
        print('{0) подоена'.format(self.name))

class Gus(Animal):
    def say(self):
        print('{0} сказала Гыл-Гыл'.format(self.name))
    def get(self):
        print('Собраны яйца у {0)'.format(self.name))

class Sheep(Animal):
    def say(self):
        print('{0} сказала Бее'.format(self.name))
    def get(self):
        print('{0) подстрижена'.format(self.name))

class Utka(Amimal):
    def say(self):
        print('{0} сказала Кря-Кря'.format(self.name))
    def get(self):
        print('Собраны яйца у {0)'.format(self.name))

class Chiken(Animal):
    def say(self):
        print('{0} сказала Ко-Ко'.format(self.name))
    def get(self):
        print('Собраны яйца у {0)'.format(self.name))

class Goat(Animal):
    def say(self):
        print('{0} сказала Ге-Ге'.format(self.name))
    def get(self):
        print('Подстригли {0}'.format(self.name))

gus1 = Gus('Серый', 4)
gus2 = Gus('Белый', 3)
korova = Korova('Маньку', 300)
sheep1 = Sheep('Барашек', 75)
sheep2 = Sheep('Кудрявый', 79)
utka = Utka('Кряква', 5)
chiken1 = Chiken('Ко-Ко', 4)
chiken2 = Chiken('Кукареку', 3)
goat1 = Goat('Рога', 80)
goat2 = Goat('Рога', 75)

all_animals = [gus1, gus2, korova, sheep1, sheep2, utka, chiken1, chiken2, goat1, goat2]

weight = 0
for animal in all_animals:
        weight += animal.weight
        animal.eat()
        animal.say()
        animal.get()
print(weight)
        
        
        
        

        
                
