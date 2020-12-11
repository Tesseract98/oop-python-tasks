from Zoo.impl.Cage import Cage
from Zoo.impl.Animal import Animal
from Zoo.impl.Employee import Employee
from Zoo.ZooString import ZooString
from Zoo.ZooXml import DataXml
from Zoo.Zoo import Zoo
from Zoo.ZooSql import DataSql
from copy import deepcopy


def main():
    zoo = Zoo()
    cage = Cage(1)
    empl = Employee('Max', 'breadwinner')
    # empl2 = Employee('Max', 'cleaner')
    num1 = ZooString(cage)
    num1.set_animals([Animal('zebra', 'fruit'), Animal('elephant', 'fruit')])
    num1.set_employees(empl)
    cage = Cage(2)
    num = ZooString(cage)
    num.set_animals([Animal('tiger', 'meat'), Animal('tiger', 'meat')])
    num.set_employees(empl)
    zoo.zoo_string = num
    zoo.zoo_string = num1

    zoo_clone = deepcopy(zoo)
    DataSql.write('init.sqlite', zoo_clone)
    DataXml.write('init.xml', zoo)
    for i in zoo.zoo_string:
        i.show()


if __name__ == '__main__':
    main()
