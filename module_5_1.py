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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

