from Zoo.impl.Animal import Animal
from Zoo.Zoo import Zoo
from Zoo.ZooSql import DataSql


def main():
    zoo = Zoo()
    DataSql.read('init.sqlite', zoo)
    zoo.delete_animal(3)
    zoo.zoo_string[1].set_animals(Animal('lion', 'meat'))
    DataSql.write('transformed.sqlite', zoo)
    for i in zoo.zoo_string:
        i.show()


if __name__ == '__main__':
    main()
