from Zoo.impl.Cage import Cage


class ZooString:
    def __init__(self, cage: Cage = Cage(0)):
        self.__animals = []
        self.__employees = []
        self.__cage = cage

    def get_animals(self):
        return self.__animals

    def set_animals(self, animal):
        if isinstance(animal, list):
            self.__animals += animal
        else:
            self.__animals.append(animal)

    def get_employees(self):
        return self.__employees

    def set_employees(self, employee):
        if isinstance(employee, list):
            self.__employees += employee
        else:
            self.__employees.append(employee)

    def get_cage(self):
        return self.__cage

    def set_cage(self, cage):
        self.__cage = cage

    def delete_cage(self):
        self.__cage = None

    def show(self):
        print('\nCage code:', self.__cage.code)
        print('Cage number:', self.__cage.name)
        print('\nAnimals:')
        for i in self.__animals:
            print('animal code:', i.code)
            print('kind:', i.name)
            print('food:', i.food)
            print('-' * 10)
        print('\nEmployees:')
        for i in self.__employees:
            print('employee code:', i.code)
            print('name:', i.name)
            print('profession:', i.profession)
            print('-' * 10)
        print('#' * 15)
