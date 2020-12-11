from Zoo.impl.Animal import Animal
from Zoo.Zoo import Zoo
from Zoo.ZooXml import DataXml


def main():
    zoo = Zoo()
    DataXml.read('init.xml', zoo)
    zoo.delete_animal(3)
    zoo.zoo_string[1].set_animals(Animal('lion', 'meat'))
    DataXml.write('transformed.xml', zoo)
    for i in zoo.zoo_string:
        i.show()


if __name__ == '__main__':
    main()
