class House:
    def __init__(self,name,floor):
        self.name=name
        self.number_of_floors=floor
    def go_to(self,floor):
        if 1 <= floor <= self.number_of_floors:
            for i in range(floor):
                print(f'{i}-й этаж')
        else:
            print('Такого этажа не существует!')
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __eq__(self, other):
        if isinstance(other,House):
            return self.number_of_floors == other.number_of_floors
        else:
            raise TypeError
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            raise TypeError
    def __gt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors > other.number_of_floors
        else:
            raise TypeError
    def __ge__(self, other):
        if isinstance(other,House):
            return self.number_of_floors >= other.number_of_floors
        else:
            raise TypeError
    def __lt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors == other.number_of_floors
        else:
            raise TypeError
    def __le__(self, other):
        if isinstance(other,House):
            return self.number_of_floors == other.number_of_floors
        else:
            raise TypeError
    def __add__(self, other):
        if isinstance(other,int):
            self.number_of_floors+=other
            return self
        else:
            raise TypeError('Требуется тип операнда int')
    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            raise TypeError('Требуется тип операнда int')
    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            raise TypeError('Требуется тип операнда int')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
h2 = 1.5 + h2
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__