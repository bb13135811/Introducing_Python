6.1
class Thing():
    pass
print(Thing)
example = Thing()
print(example)

6.2
class Thing2():
    letters = 'abc'
print(Thing2.letters)

6.3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'
a = Thing3()
print(a.letters)

6.4
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
hydrogen = Element('Hydrogen', 'H', 1)

6.5
dict_1 = {
    'name': 'Hydrogen',
    'symbol': 'H',
    'number': 1,
    }
hydrogen = Element(dict_1['name'], dict_1['symbol'], dict_1['number'])
hydrogen = Element(**dict_1)
hydrogen.name
hydrogen.symbol
hydrogen.number

6.6
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name=%s, symbol=%s, number=%s' %
            (self.name, self.symbol, self.number))
hydrogen = Element(**dict_1)
hydrogen.dump()

6.7
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' %
        (self.name, self.symbol, self.number))
hydrogen = Element(**dict_1)
print(hydrogen)

6.8
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def get_name(self):
        return self.__name
    @property
    def get_symbol(self):
        return self.__symbol
    @property
    def get_number(self):
        return self.__number
hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.get_name
hydrogen.get_symbol
hydrogen.get_number

6.9
class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Oc():
    def eats(self):
        return 'campers'
a = Bear()
b = Rabbit()
c = Oc()
print(a.eats())
print(b.eats())
print(c.eats())

6.10
class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class Smartphone:
    def does(self):
        return 'ring'
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()
    def does(self):
        return '''the functions are:
The Laser is to %s.
The Claw is to %s.
The Smartphone is to %s''' %(
            self.laser.does(),
            self.claw.does(),
            self.smartphone.does())
robot = Robot()
print(robot.does())
